'''
Docstring for Python_Projects.My_Project_Transportation_Tickets.Main
This program is for booking a transportation delivery for certain customers.
Author is Abdullah Al-Hiami any change in this program will make it unstable. So, please don't steal my head work only use it as it is.
'''
import Module_Transportation as mt

mt.transportation_data #calling our Dictionary list from our Module

exit = True

while exit:
    print("---------------------------- Transportation ----------------------------")
    print("Choose An Option For The Wanted Operation By Its Number.----------------")
    print("Enter \'1\' To Add Transportation Data Route, Destination, and Capacity.")
    print("Enter \'2\' To Get The Availble Routes.---------------------------------")
    print("Enter \'3\' To Book For A Passenger By The Route Id.--------------------")
    print("Enter \'4\' To Cancel Booking For A Passenger.--------------------------")
    print("Enter \'5\' To Check For Availble Seats By Route Id.--------------------")
    print("Enter \'6\' To Get All Passenges Inside A List, By Destination.---------")
    print("Enter \'7\' To Get The Transportation Revenue, By Destination.----------")
    print("Enter \'8\' To Search For A Specific Route, By Destination.-------------")
    print("Enter \'9\' To Search For A Specific Route ID.--------------------------")
    print("Enter \'10\' To Search For A Specific Destintation.---------------------")
    print("Enter \'11\' Print All Transportation Data.-----------------------------")
    print("This Program Designed By Abdullah Al-Hiami Thank You for using it-------")
    option = input("\tSelect An Option: ")
    if option.isdigit():
        option = int(option)
    else:
        print("Selecting Operation Error, Try Numbers Instead!")
  
    if  option == 1:
        print("------------------- Enter Your Data Here. --------------------------")
        route_id = input("\tEnter Your Route Id Here: ")
        destination = input("\tEnter The Destination Here: ")
        capacity = input("\tEnter The Capacity Of the Destination Here: ")

        if capacity.isdigit():
            capacity = int(capacity)
            print(mt.add_route(route_id,destination,capacity))
            print("********************************************************************")

        else:
            print("Capacity Error. Please Try Inputting Numbers")

    elif option == 2:
        print("-------------------- Avaible Routes Are. ---------------------------")
        print(mt.get_available_routes())
        print("********************************************************************")

    elif option == 3:
        print("------------------- Enter Ticket Info To book. ---------------------")
        route_id = input("\tEnter Your Route Id Here: ")
        passenger_name = input("\tEnter The Name Of The Passenger:")
        print(mt.book_ticket(route_id,passenger_name))
        print("********************************************************************")

    elif option == 4:
        print("------------------------- Cancel Ticket. ---------------------------")
        route_id = input("\tEnter Your Route Id Here: ")
        passenger_name = input("\tEnter The Name Of The Passenger:")
        print(mt.cancel_booking(route_id,passenger_name))
        print("********************************************************************")

    elif option == 5:
        print("----------------------- Get Avaible Seats. -------------------------")
        route_id = input("\tEnter Your Route Id Here: ")
        print(f"Avaible seats in {route_id} is {mt.check_seat_availability(route_id)}")
        print("********************************************************************")

    elif option == 6:
        print("------------------------ Get Passengers. ---------------------------")
        route_id = input("\tEnter Your Route Id Here: ")
        print(f'All Passengers In Route {route_id} Are:\n {mt.get_passenger_list(route_id)} ')
        print("********************************************************************")

    elif option == 7:
        print("-------------------- Get Total Route Revenue. ----------------------")
        ticket_price = input("\tEnter Ticket Price Here: ")
        if ticket_price.isdigit():
            ticket_price = float(ticket_price)
            route_id = input("\tEnter Your Route Id Here: ")
            print(f'The Total Of The Price Is {mt.calculate_route_revenue(route_id,ticket_price)}')
            print("********************************************************************")
        else:
            print("Invaild Input For The Price, It Must Be Numbers!")

    elif option == 8:
        print("------------------- Get Route By Destination. ----------------------")
        destination = input("\tEnter The Destination Here: ")
        print(f"Your Route Are\n {mt.search_route_by_destination(destination)}")
        print("********************************************************************")
    elif option == 9:
        print("------------------- Get Specific Route Info. -----------------------")
        route_id = input("\tEnter Your Route Id Here: ")
        print(f'The Route Information Is \n {mt.find_route(route_id)}')
        print("********************************************************************")
    elif option == 10:
        print("----------------- Get Specific Destination Info. -------------------")
        destination = input("\tEnter The Destination Here: ")
        print(f'The Route Information Is \n {mt.find_destination(destination)}')
        print("********************************************************************")
    elif option == 11:
        print("------------------------- Print All Info ---------------------------")
        mt.print_all_routes()
        print("********************************************************************")
    else:
        print("The Number Of The Operation Doesn't Exist, Try Again With A Vaild Number!")
    exit = input("Do You Want To Exit The Program Type \"No\" Or Anything Else TO Exit? ").lower() == "no"


