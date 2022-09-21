
def genQR(path,name):
    # import pyqrcode
    # from pyqrcode import QRCode
    import qrcode
    # from svglib.svglib import svg2rlg
    # from reportlab.graphics import renderPM
    try:
        text_file = open(path,'r')
        data = text_file.read()
        text_file.close()
        #qr_location = r'{}\{}'.format(path,name_qr)
        qr = qrcode.make(data)
        qr.save(name)
        # drawing = svg2rlg(r'{}.svg'.format(qr_location))
        # renderPM.drawToFile(drawing, qr_location+'.png', fmt='PNG')
    except Exception as Ex:
        return Ex
genQR(path='D:/kunal/new 2.txt',name='data.png')