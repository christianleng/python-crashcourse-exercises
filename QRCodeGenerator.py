import qrcode


def generateQrCode():
    inputURL = input("Enter the text or URL for the QR code:")
    img = qrcode.make(inputURL)
    type(img)
    qrcodeName = input("Enter the filename:")
    img.save(f"{qrcodeName}.png")
    print(f"QR code saved as {qrcodeName}.png")


generateQrCode()
