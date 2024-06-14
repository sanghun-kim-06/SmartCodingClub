import qrcode
file_path = r'QRcode\\qrList.txt'
f = open(file_path, 'rt', encoding='UTF-8')
lines = f.readlines()
for line in lines :
    line = line.strip()
    qr_data = line
    qr_img = qrcode.make(qr_data)

    save_path = '.\\' + qr_data + '.png'
    qr_img.save(save_path)
f.close()