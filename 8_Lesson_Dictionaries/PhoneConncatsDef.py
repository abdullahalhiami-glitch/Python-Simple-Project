Conntact = {}

while True:
    print("------------------- Choose an option ----------------------")
    print("1.Add New Conntact. ---------------------------------------")
    print("2.Search For a Conntact. ----------------------------------")
    print("3.Delete a Conntact. --------------------------------------")
    print("4.Show All Conntacts. -------------------------------------")
    print("5.Update Conntact. ----------------------------------------")
    print("6.EXIT. ---------------------------------------------------")

    option = int(input("Enter an option to select an operation: "))
    if option == 1:
        name = input("Enter the name of the conntact: ").capitalize()
        phoneNumber = input("Enter phone number right here: ").strip()
        Conntact.update({name:phoneNumber})
        print(len(Conntact))
        print("Conntact was added successfully.")
    elif option == 2:
        name = input("Enter a conntact name to search for: ").capitalize()
        if name in Conntact.keys():
            print('The name was found')
            print(f'{name}: {Conntact[name]}')
        else:
            print("Sorry We Couldn't find your Conntact!")
    elif option == 3:
        name = input("Enter a name to delete").capitalize()
        if name in Conntact:
            del Conntact[name]
            print("Deleted successfully")
        else:
            print("Sorry We Couldn't find your Conntact!")
    elif option == 4:
        if len(Conntact)<=0:
            print("Conntact list is Empty.")
        else:
            for key,value in Conntact.items():
                print(f'{key} {value}')
    elif option == 5:
        name = input("Enter a name to delete").capitalize()
        NewPhoneNumber = input("Enter the new phone number: ").strip()
        Conntact.update({name:NewPhoneNumber})
        print("Updated successfully")   
    elif option == 6:
        print("Goodbye!")
        break