import qrcode

def generate_qr_code(data, filename):
    # إعداد خصائص الـ QR Code
    qr = qrcode.QRCode(
        version=1, # حجم الرمز (من 1 إلى 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H, # تصحيح الأخطاء لضمان القراءة
        box_size=10, # حجم كل مربع
        border=4, # حجم الإطار الأبيض
    )
    
    # إضافة البيانات
    qr.add_data(data)
    qr.make(fit=True)

    # إنشاء الصورة وتلوينها (يمكن تغيير الألوان حسب التصميم)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # حفظ الصورة
    img.save(filename)
    print(f"تم إنشاء الـ QR Code وحفظه باسم: {filename}")

# تجربة البرنامج
user_data = input("أدخل الرابط أو النص الذي تريد تحويله: ")
generate_qr_code(user_data, "my_qrcode.png")