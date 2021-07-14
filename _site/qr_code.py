import qrcode
qr = qrcode.QRCode(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_Q,
box_size=10,
border=4,
)
qr.add_data('https://www.rosecersonsky.com')
qr.make(fit=True)

image = qr.make_image(fill_color="#003c71", back_color="white")
image.save('website-qr.png')
