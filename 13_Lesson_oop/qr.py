import qrcode

def generate_qr_code(data, filename):
    # QR Code Settings
    qr = qrcode.QRCode(
        version=1, # The Size of the symbols (From 1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H, # correcting Errors to ensure readability
        box_size=10, # The Size of the Square
        border=4, # The Size of the border
    )
    
    # Adding Data
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image and color it Tip(You can change its color according to the design)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save Image
    img.save(filename)
    print(f"تم إنشاء الـ QR Code وحفظه باسم: {filename}")

# Trying the program
user_data = input("Enter the Link or the Text to convert it into a barcode:  ")
generate_qr_code(user_data, "my_qrcode.png")