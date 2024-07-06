import qrcode
def make_QR(link,color,background_color,size,Border_size):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=size, border= Border_size)

    qr.add_data(link)
    qr.make(fit=True)

    image = qr.make_image(fill_color=color, back_color=background_color)
    image.save("QR_linked.png")

link = input("Enter your link : ")
color = input("Enter the color of the QR: ")
Back_color = input("Enter the background color : ")
size = int(input("Enter the size of the QR: "))
Bsize = int(input("Enter the Border size: "))
make_QR(link,color,Back_color,size,Bsize)