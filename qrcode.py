import qrcode

data = "https://www.iba-suk.edu.pk/"

qr = qrcode.make(data)

qr.save("qrcode.png")

print("QR code saved as qrcode.png")