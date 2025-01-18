import qrcode  # Import the QR Code module

# Get user input for URL and file name
url = input("Enter the URL: ").strip()
file_name = input("Enter the name for the QR code file (without extension): ").strip()

# Validate input
if not url:
    print("Error: URL cannot be empty!")
elif not file_name:
    print("Error: File name cannot be empty!")
else:
    try:
        # Create a QR code with custom settings #Creates an empty QR code object.

        qr = qrcode.QRCode(
            version=1,  # QR code version (controls the size (1 to 40))
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level:determines how much data can be recovered if the QR code is damaged.
            box_size=10,  # Size of each box in the QR code grid
            border=4  # Border size
        )
        qr.add_data(url) #stores the actual data (URL, text, etc.).
        qr.make(fit=True)  # Adjust size automatically

        # Generate and save the QR code
        img = qr.make_image(fill="black", back_color="white")
        img.save(f"{file_name}.png")

        print(f"✅ QR Code successfully saved as {file_name}.png")
    except Exception as e:
        print(f"An error occurred: {e}")


