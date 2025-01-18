import qrcode as qr # type: ignore
url= input("Enter the URL: ")
file_name = input("Enter the name for the QR code file (without extension): ")
img = qr.make(url)
img.save(f"{file_name}.png")
