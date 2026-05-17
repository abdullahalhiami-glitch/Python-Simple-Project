#برنامج جهات الاتصال
contacts={
    'Ali':'778266532',
    'sami':'73364321'
}
#دالة لأضافة جهة اتصال 
def add_contact(name,phone):
    if name in contacts:
        print('the name already exists')
    else:
        contacts[name]=phone
        print('the contact has been successfully added')
#دالة عرض جهات الاتصال
def get_all_contacts():
    return contacts
#دالة البحث
def seach_by_name(keyword):
    result={}

    for name,phone in contacts.items():
        if keyword.lower() in name.lower():
            result[name]=phone
    return result
#دالة تقوم بتحديث الرقم
def update_phone(name,new_phone):
    if name in contacts:
        contacts[name]=new_phone
        print('the number has been update')
    else:
        print('the name does not exist')
#دالة تقوم بحذف جهة الاتصال 
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print('the contact haa been deleted')
    else:
        print('the name does not exist')
#دالة التحقق من الرقم المكرر
def is_duplicate_phone(phone):
    return phone in contacts.values()
#دالة تقوم بعد جهات الاتصال
def count_contacts():
    return len(contacts)
#دالة ترتيب جهات الاتصال
def get_contacts_sorted():
    return sorted(contacts.items())

