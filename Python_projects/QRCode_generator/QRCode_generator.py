#Generate QRCode for Gpay UPI ID and Gpay Phone no.
import qrcode
import image
from qrcode import QRCode

qr = qrcode.QRCode(version=15, box_size=10, border=5)

data ="UPI ID"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("UPI_ID.png")

data2 = "PHONE NUMBER"
qr.add_data(data2)
qr.make(fit=True)
img1 = qr.make_image(fill="black",back_color="white")
img1.save("GPayNumber.png")
