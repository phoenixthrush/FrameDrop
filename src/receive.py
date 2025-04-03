import qrcode

qr = qrcode.QRCode(
    version=40,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

qr.add_data('Aylin Bayram')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()
