import qrcode as qr # type: ignore
img = qr.make("https://www.facebook.com/prateema.dhakal.18")
img.save("qr_code.png")
