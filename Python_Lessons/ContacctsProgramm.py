Contacts={}
while True:
    print('Choose An Option:')
    print('1- Add New Contact')
    print('2- Search For Contact')
    print('3- Delete Contact')
    print('4- Show All Contacts')
    print('5- Update Contact')
    print('6- Exit')
    option=int(input('Enter Your Option:').strip())
    if option==1:
        name=input('Enter The Name:').capitalize()
        phone=input('Enter phone Number:')
        Contacts.update({name:phone})
        print('Added Successfull')
        print(len(Contacts))
    elif option==2:
        name=input('Enter The Name You Want To Found:').capitalize()
        if name in Contacts.keys():
            print('We Found The Name')
            print(f"{name} {Contacts[name]}")
        else:
            print("Sorry We Can Not Found")
    elif option==3:
        name=input('Enter The Name You Want To Delete:').capitalize()
        if name in Contacts:
            del Contacts[name]
            print('Deleted Successfull')
        else:
            print("Sorry We Can Not Found")
    elif option==4:
        if len(Contacts)<=0:
            print('Empty Contacts ')
        else:
            for key,value in Contacts.items():
                print(f'{key} {value}')
    elif option==5:
        name=input('Enter The Name You Want To Delete:')
        if name in Contacts:
            newvalue=input('Enter New phone Number:')
            Contacts.update({name:newvalue})
            print('Updated Successfull')
        else:
            print("Sorry We Can Not Found")
    else:
        break
print('Come back Soon ^__^')
