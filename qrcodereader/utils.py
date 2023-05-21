import qrcode


def generate_qrcode(data):
    content = ''
    for key in data.keys():
        content += data[key]
        
    qr = qrcode.QRCode(version=1, box_size=15)
    qr.add_data(content)
    
    filename = 'tempqrcode.png'
    img = qr.make_image()
    img.save('qrcodereader/static/images/' + filename)
    
    return filename