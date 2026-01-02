import qrcode

data = input("Enter URL or text : ").strip()
filename = input("Enter the filename : ").strip()

qrcode.QRcode(box_size=10, border=4)
qr.add_data(data)
qr.make_image(fill_color='black' , back_color='white' )
image.save(filename)
print(f"QR code saved as {filename}.jpg")