import qrcode
import requests
from PIL import Image
from io import BytesIO
import re
import svgwrite


def generate_qr(url):
    # Check if URL is valid
    try:
        request = requests.get(url)
        request.raise_for_status()
    except (requests.HTTPError, requests.ConnectionError):
        print('Invalid URL. Please enter a valid URL.')
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create PNG image
    img_png = qr.make_image(fill_color="black", back_color="white")

    # Create SVG image
    matrix = qr.get_matrix()
    size = len(matrix)
    img_svg = svgwrite.Drawing(
        f"qr_code_{url}.svg", (size * 10, size * 10), debug=True)
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell:
                img_svg.add(img_svg.rect(
                    (c * 10, r * 10), (10, 10), fill="black"))

    # Extract the URL without special characters
    clean_url = re.sub(
        r"(^https?://)?[^a-zA-Z0-9_~]", r"_", url).replace(".", "")

    # Save the images
    img_png.save(f"qr_code_{clean_url}.png")
    img_svg.saveas(f"qr_code_{clean_url}.svg")


url = input('Enter a URL: ')
generate_qr(url)
