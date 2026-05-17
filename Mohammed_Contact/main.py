import contacts1 as con
while True:
    print('********contacts*******\n')
    print('1-Add contact')
    print('2-Show contacts')
    print('3-Search contact')
    print('4-Upadte phone')
    print('5-Delete contact')
    print('6-Check Duplicate phone')
    print('7-Count contacts')
    print('8-Sorted contacts')
    print('9-Exit')

    option=input('choose from the previous options: ').strip()

    if option=='1':
        name=input('Enter the name:').lower()
        phone=input('Enter the phone:').strip()
        con.add_contact(name,phone)
    elif option=='2':
        print(con.get_all_contacts())
    elif option=='3':
        keyword=input('Search the name: ').lower()
        print(con.seach_by_name(keyword))
    elif option=='4':
        name=input('Enter the name:').lower()
        new_phone=input("Enter new phone: ").strip()
        con.update_phone(name,new_phone)
    elif option=='5':
        name=input('Enter name to delete: ').lower()
        con.delete_contact(name)
    elif option=='6':
        phone=input('Enter phone: ')
        print(con.is_duplicate_phone(phone))
    elif option=='7':
        print(f'Total contacts: {con.count_contacts()}')
    elif option=='8':
        print(con.get_contacts_sorted())
    elif option=='9':
        print('Good Bye *_^')
        break
    else:
        print('Invalid Choice *_*')



