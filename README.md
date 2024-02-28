# QR Code Generator

This Python script generates a QR code image from a provided URL. It removes special characters from the URL to ensure compatibility with various file systems while still maintaining relevant information.

**Features:**

- Generates QR codes from URLs
- Handles invalid URLs gracefully
- Saves QR code as a PNG image
- Saves QR code as an SVG image
- Creates filename with URL information, removing special characters

**Usage:**

1. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

   - On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script:**

   ```bash
   python main.py
   ```

   You will be prompted to enter a URL.

5. **Enter a valid URL and press Enter.**

   The script will generate and save the QR code image with a descriptive filename based on the URL.

**Example:**

If you enter the URL "https://hashir.blog", the script will generate files named "qr_code_hashir_blog.png" and "qr_code_hashir_blog.svg".

**Requirements:**

- Python 3.x
- Libraries:
  - qrcode
  - requests
  - Pillow
  - svgwrite
