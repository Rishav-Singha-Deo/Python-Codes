import pyqrcode
import os

s=input("Enter your message : ")
q=pyqrcode.create(s)
q.png("QR 1.png",scale=50)
os.system("QR 1.png")
