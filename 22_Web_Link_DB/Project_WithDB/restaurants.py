import sqlite3 as sql  # استيراد مكتبة sqlite3 للتعامل مع قواعد البيانات وإعطائها اسم مستعار sql
import os  # استيراد مكتبة os للتعامل مع مسارات الملفات ونظام التشغيل

# تحديد مسار قاعدة البيانات
DB_NAME = os.path.join(os.path.dirname(__file__), "Restaurants.db")  # إنشاء المسار الكامل لملف قاعدة البيانات في نفس مجلد السكربت
def get_db_connection():  # تعريف دالة لإنشاء اتصال بقاعدة البيانات
    conn = sql.connect(DB_NAME)  # فتح اتصال مع قاعدة البيانات المحددة بالمسار
    conn.row_factory = sql.Row  # إعداد الاتصال ليرجع النتائج على شكل قواميس (للوصول للأعمدة بالاسم)
    conn.execute("PRAGMA foreign_keys = ON")  # تفعيل دعم المفاتيح الأجنبية لضمان تكامل البيانات
    return conn  # إرجاع كائن الاتصال لاستخدامه

def add_restaurant(name, cuisine_type):  # تعريف دالة لإضافة مطعم جديد تستقبل اسم المطعم ونوعه
    """إضافة مطعم جديد"""  # وصف الدالة
    conn = get_db_connection()  # فتح اتصال جديد بقاعدة البيانات
    cur = conn.cursor()  # إنشاء مؤشر (Cursor) لتنفيذ أوامر SQL
    try:  # بدء كتلة التجربة للتعامل مع الأخطاء المحتملة
        cur.execute("INSERT INTO restaurants (name, cuisine_type) VALUES (?, ?)", (name, cuisine_type))  # تنفيذ أمر إدخال بيانات المطعم الجديد
        conn.commit()  # حفظ التغييرات في قاعدة البيانات
        return f"Restaurant '{name}' added successfully."  # إرجاع رسالة بنجاح إضافة المطعم
    except sql.IntegrityError:  # التقاط خطأ تكرار البيانات (مثلاً إذا كان الاسم موجوداً مسبقاً)
        return f"Restaurant '{name}' already exists."  # إرجاع رسالة بأن المطعم موجود بالفعل
    finally:  # كتلة تنفذ دائماً سواء نجحت العملية أم فشلت
        conn.close()  # إغلاق الاتصال بقاعدة البيانات

def add_rating(name, rating_value):  # تعريف دالة لإضافة تقييم لمطعم معين
    """إضافة تقييم جديد للقائمة"""  # وصف الدالة
    try:  # بدء كتلة تجربة لتحويل قيمة التقييم
        rating_value = float(rating_value)  # تحويل التقييم المدخل إلى رقم عشري
        if not (0 <= rating_value <= 5):  # التحقق مما إذا كان التقييم خارج النطاق من 0 إلى 5
            return "Rating must be between 0 and 5."  # إرجاع رسالة خطأ إذا كان التقييم خارج النطاق
    except ValueError:  # التقاط خطأ فشل تحويل النص إلى رقم
        return "Invalid rating value."  # إرجاع رسالة بأن قيمة التقييم غير صالحة

    conn = get_db_connection()  # فتح اتصال بقاعدة البيانات
    cur = conn.cursor()  # إنشاء مؤشر لتنفيذ الأوامر
    cur.execute("SELECT id FROM restaurants WHERE name = ?", (name,))  # البحث عن معرّف المطعم باستخدام اسمه
    row = cur.fetchone()  # جلب النتيجة الأولى من الاستعلام
    if not row:  # التحقق مما إذا لم يتم العثور على المطعم
        conn.close()  # إغلاق الاتصال بقاعدة البيانات
        return f"Restaurant '{name}' not found."  # إرجاع رسالة بأن المطعم غير موجود
    
    cur.execute("INSERT INTO ratings (restaurant_id, rating_value) VALUES (?, ?)", (row['id'], rating_value))  # إدخال التقييم الجديد في جدول التقييمات بربطه بمعرف المطعم
    conn.commit()  # حفظ التغييرات
    conn.close()  # إغلاق الاتصال
    return f"Rating added to restaurant '{name}' successfully."  # إرجاع رسالة تفيد بنجاح إضافة التقييم

def get_restaurant_info(name):  # تعريف دالة لجلب معلومات مطعم معين
    """عرض نوع المطعم وتقييماته"""  # وصف الدالة
    conn = get_db_connection()  # فتح اتصال بقاعدة البيانات
    cur = conn.cursor()  # إنشاء مؤشر لتنفيذ الأوامر
    cur.execute("SELECT id, cuisine_type FROM restaurants WHERE name = ?", (name,))  # جلب معرّف ونوع طعام المطعم بناءً على اسمه
    row = cur.fetchone()  # استخراج صف البيانات
    if not row:  # إذا لم يتم إيجاد المطعم
        conn.close()  # إغلاق الاتصال
        return f"Restaurant '{name}' not found."  # إرجاع رسالة تفيد بعدم العثور على المطعم
    
    cur.execute("SELECT rating_value FROM ratings WHERE restaurant_id = ?", (row['id'],))  # استعلام لجلب جميع تقييمات هذا المطعم
    ratings = [r['rating_value'] for r in cur.fetchall()]  # تكوين قائمة تحتوي على جميع التقييمات المجلوبة
    conn.close()  # إغلاق الاتصال
    return f"Cuisine: {row['cuisine_type']}, Ratings: {ratings}"  # إرجاع نص يحتوي على نوع المطعم وقائمة تقييماته

def calculate_average_rating(name):  # تعريف دالة لحساب متوسط تقييمات مطعم
    """تُرجع متوسط تقييم المطعم من 5"""  # وصف الدالة
    conn = get_db_connection()  # فتح اتصال بقاعدة البيانات
    cur = conn.cursor()  # إنشاء المؤشر
    cur.execute("SELECT id FROM restaurants WHERE name = ?", (name,))  # البحث عن المطعم وجلب معرّفه
    row = cur.fetchone()  # جلب نتيجة البحث
    if not row:  # في حال لم يتم العثور عليه
        conn.close()  # إغلاق الاتصال
        return f"Restaurant '{name}' not found."  # إرجاع رسالة بعدم وجود المطعم
    
    cur.execute("SELECT AVG(rating_value) as avg_rating FROM ratings WHERE restaurant_id = ?", (row['id'],))  # حساب متوسط التقييمات لهذا المطعم عبر دالة AVG في SQL
    result = cur.fetchone()  # جلب نتيجة الحساب
    conn.close()  # إغلاق الاتصال
    
    if result and result['avg_rating'] is not None:  # التحقق من وجود نتيجة فعلية (أي يوجد تقييمات)
        return round(result['avg_rating'], 2)  # إرجاع المتوسط مقرباً إلى خانتين عشريتين
    return "No ratings for this restaurant yet."  # إرجاع رسالة تفيد بعدم وجود تقييمات للمطعم حتى الآن

def search_by_cuisine(cuisine_type):  # تعريف دالة للبحث عن المطاعم حسب نوع الطعام
    """تُرجع المطاعم من فئة معينة"""  # وصف الدالة
    conn = get_db_connection()  # فتح اتصال بقاعدة البيانات
    cur = conn.cursor()  # إنشاء المؤشر
    cur.execute("SELECT name FROM restaurants WHERE LOWER(cuisine_type) = LOWER(?)", (cuisine_type,))  # جلب أسماء المطاعم التي يتطابق نوعها مع المدخل (مع تجاهل حالة الأحرف)
    rows = cur.fetchall()  # جلب كل النتائج المطابقة
    conn.close()  # إغلاق الاتصال
    
    found = [r['name'] for r in rows]  # تكوين قائمة بأسماء المطاعم المستخرجة
    if not found:  # إذا كانت القائمة فارغة
        return f"No restaurants found for cuisine '{cuisine_type}'."  # إرجاع رسالة بأنه لم يتم العثور على أي مطعم
    return found  # إرجاع قائمة المطاعم التي تم إيجادها

def get_top_rated_restaurants(min_rating):  # تعريف دالة لجلب المطاعم ذات التقييم المرتفع
    """تُرجع المطاعم التي متوسطها أعلى من رقم محدد"""  # وصف الدالة
    try:  # محاولة تحويل الحد الأدنى للتقييم المدخل
        min_rating = float(min_rating)  # تحويل المدخل إلى رقم عشري
    except ValueError:  # التقاط خطأ التحويل
        return "Invalid rating value."  # إرجاع رسالة بخطأ الإدخال
    
    conn = get_db_connection()  # فتح اتصال
    cur = conn.cursor()  # إنشاء مؤشر
    cur.execute('''  # تنفيذ استعلام مركب
        SELECT r.name, AVG(rt.rating_value) as avg_rating  # جلب اسم المطعم وحساب متوسط تقييماته
        FROM restaurants r  # من جدول المطاعم كجدول أساسي
        JOIN ratings rt ON r.id = rt.restaurant_id  # ربطه بجدول التقييمات بناءً على معرّف المطعم
        GROUP BY r.id  # تجميع النتائج لكل مطعم على حدة
        HAVING avg_rating >= ?  # تصفية النتائج لتبقى المطاعم التي متوسط تقييمها أكبر من أو يساوي الحد الأدنى
    ''', (min_rating,))  # تمرير الحد الأدنى كمعامل للاستعلام
    rows = cur.fetchall()  # جلب جميع السجلات المطابقة
    conn.close()  # إغلاق الاتصال
    
    top_rated = [(r['name'], round(r['avg_rating'], 2)) for r in rows]  # تكوين قائمة تحتوي على أزواج (اسم المطعم، ومتوسط تقييمه المقرب)
    if not top_rated:  # إذا لم يتم العثور على مطاعم تطابق الشرط
        return f"No restaurants found with average rating >= {min_rating}."  # إرجاع رسالة بعدم وجود مطاعم بهذا التقييم
    return top_rated  # إرجاع قائمة المطاعم الأعلى تقييماً

def update_restaurant_cuisine(name, new_cuisine):  # تعريف دالة لتحديث نوع مطعم
    """تعديل نوع المطعم"""  # وصف الدالة
    conn = get_db_connection()  # فتح الاتصال بقاعدة البيانات
    cur = conn.cursor()  # إنشاء مؤشر
    cur.execute("UPDATE restaurants SET cuisine_type = ? WHERE name = ?", (new_cuisine, name))  # تنفيذ أمر تحديث نوع المطعم بناءً على اسمه
    if cur.rowcount == 0:  # التحقق من عدد الصفوف التي تأثرت بالتحديث (إذا كان 0 يعني المطعم غير موجود)
        conn.close()  # إغلاق الاتصال
        return f"Restaurant '{name}' not found."  # إرجاع رسالة بعدم وجود المطعم
    conn.commit()  # حفظ التعديلات في قاعدة البيانات
    conn.close()  # إغلاق الاتصال
    return f"Restaurant '{name}' cuisine updated to '{new_cuisine}' successfully."  # إرجاع رسالة بنجاح التحديث

def delete_restaurant(name):  # تعريف دالة لحذف مطعم
    """شطب المطعم من الدليل"""  # وصف الدالة
    conn = get_db_connection()  # فتح اتصال
    cur = conn.cursor()  # إنشاء مؤشر
    cur.execute("DELETE FROM restaurants WHERE name = ?", (name,))  # تنفيذ أمر الحذف للمطعم بالاسم المحدد
    if cur.rowcount == 0:  # التحقق إذا لم يتم حذف أي صف (المطعم غير موجود)
        conn.close()  # إغلاق الاتصال
        return f"Restaurant '{name}' not found."  # إرجاع رسالة تفيد بأن المطعم غير موجود
    conn.commit()  # تأكيد عملية الحذف بقاعدة البيانات
    conn.close()  # إغلاق الاتصال
    return f"Restaurant '{name}' deleted successfully."  # إرجاع رسالة بنجاح عملية الحذف

def get_all_restaurants():  # تعريف دالة لجلب كل المطاعم
    """إرجاع جميع المطاعم في الدليل"""  # وصف الدالة
    conn = get_db_connection()  # فتح اتصال بقاعدة البيانات
    cur = conn.cursor()  # إنشاء المؤشر
    cur.execute("SELECT id, name, cuisine_type FROM restaurants")  # استعلام لجلب جميع السجلات من جدول المطاعم
    rows = cur.fetchall()  # استخراج كل الصفوف المجلوبة
    
    if not rows:  # التحقق مما إذا لم يكن هناك مطاعم مسجلة
        conn.close()  # إغلاق الاتصال
        return "No restaurants found in the directory."  # إرجاع رسالة بعدم وجود مطاعم
    
    directory = {}  # إنشاء قاموس فارغ لتخزين البيانات بالهيكل المطلوب
    for r in rows:  # المرور على كل مطعم في السجلات
        cur.execute("SELECT rating_value FROM ratings WHERE restaurant_id = ?", (r['id'],))  # استعلام لجلب تقييمات هذا المطعم الحالي
        ratings = [rt['rating_value'] for rt in cur.fetchall()]  # وضع التقييمات في قائمة
        directory[r['name']] = {"cuisine": r['cuisine_type'], "ratings": ratings}  # إضافة المطعم وبياناته وتقييماته كعنصر في القاموس
        
    conn.close()  # إغلاق الاتصال
    return directory  # إرجاع القاموس النهائي الذي يحتوي كل المطاعم
