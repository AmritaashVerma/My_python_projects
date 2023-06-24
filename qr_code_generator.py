import pyqrcode
from pyqrcode import QRCode 
import png

input_link = input("Enter the link or text you want the qr code of: ")

code = pyqrcode.create(input_link)

code.png("myqrc.png", scale = 8)

