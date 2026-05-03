'''
Docstring for 8_Lesson_Dictionaries.Practice_Dictionaries.2_Location_Coordinates
'''
#boolean checker
Exit = True

#cities coordinates
CitiesCoordinates = {
    "Sana'a":(12,65),
    "Ibb":(98,45), 
    "Taz":(65,98),
    "Lahg":(65,12)
    }
#while loop that checks the whole program
while Exit:
    #Inputing the name of the city to get its coordinates
    print("-------------------- City Coordinates --------------------")
    NameOfTheCity = input("Enter the name of the City: ").capitalize()

    #Condition For checking the City
    if NameOfTheCity in CitiesCoordinates.keys():
        print("********* City has been found. *********")
        print(f"The city is {NameOfTheCity}.\n and its coordinates are\n \tX: {CitiesCoordinates[NameOfTheCity][0]}\n \tY: {CitiesCoordinates[NameOfTheCity][1]}")
    else:
        print("Couldn't find the city you are looking for!.")
    Exit = input("Do you wanna exit the program press anykey if not type (no): ").lower()=='no'
  

# print(f"The city is {NameOfTheCity}.\n and its coordinates are\n \tX: {CitiesCoordinates['Ibb'][0]}\n \tY: {CitiesCoordinates['Ibb'][1]}")
