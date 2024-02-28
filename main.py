import qrcode
import requests
from PIL import Image
from io import BytesIO
import re


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

    img = qr.make_image(fill_color="black", back_color="white")

    # Extract the URL without special characters
    clean_url = re.sub(
        r"(^https?://)?[^a-zA-Z0-9_~]", r"_", url).replace(".", "")

    # Save the image
    img.save(f"qr_code_{clean_url}.png")


url = input('Enter a URL: ')
generate_qr(url)
