'''
Docstring for Python_Projects.11_Bus_Reservation_System.11_Bus_Reservation_System
'''

sum = 0
ID = "R"
IDS= []
for i in range(10):
    new = str(sum + i)
    IDS.append(ID + new) 
print(IDS)

yemen_cities = [
    "Sanaa",
    "Aden",
    "Taiz",
    "Ibb",
    "Al Hudaydah",
    "Mukalla",
    "Dhamar",
    "Amran",
    "Saada",
    "Marib",
    "Al Bayda",
    "Hajjah",
    "Al Jawf",
    "Shabwah",
    "Lahij",
    "Abyan",
    "Raymah",
    "Mahwit",
    "Socotra"
]

Transportation_Data = [
    {
        "Route_Id":IDS,
        "Destination": yemen_cities,
        "Capacity" : 30,
        "Booked": []
    }
]

def Add_Route(destination, capacity):



