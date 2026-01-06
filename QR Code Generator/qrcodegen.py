import qrcode

data = input("Enter URL or text: ").strip()
filename = input("Enter the filename: ").strip()

# 1. Initialize the QRCode object and assign it to 'qr'
qr = qrcode.QRCode(
    version=1,
    box_size=10, 
    border=4
)

# 2. Add the data
qr.add_data(data)
qr.make(fit=True)

# 3. Create the image and assign it to 'image'
image = qr.make_image(fill_color='black', back_color='white')

# 4. Save the image
image.save(filename)

print(f"QR code saved as {filename}")