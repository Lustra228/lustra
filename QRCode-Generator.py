import qrcode as qr

data = input('Data of qrcode: ')
name = input('Save name: ')

qrcode = qr.QRCode(
    version = 1,
    box_size = 10,
    border = 4
)

qrcode.add_data(data)
qrcode.make(fit = 1)

qr_img = qrcode.make_image(
    fill_color = 'black',
    back_color = 'white'
)

qr_img.save(name)