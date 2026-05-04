import random 
import string

first_names = ['John', 'Jane', 'Alex', 'Emily', 'Michael', 'Sarah', 'David', 'Jessica', 'Chris', 'Amanda', 'Daniel', 'Ashley', 'James', 'Megan', 'Robert', 'Lauren', 'William', 'Nicole', 'Joseph', 'Rachel', 'Andrew', 'Samantha', 'Matthew', 'Stephanie', 'Anthony', 'Brittany', 'Mark', 'Heather', 'Steven', 'Amber', 'Kevin', 'Melissa', 'Brian', 'Tiffany', 'Jason', 'Kimberly', 'Justin', 'Elizabeth', 'Ryan', 'Megan', 'Brandon', 'Emily', 'Jacob', 'Lauren', 'Nicholas', 'Hannah', 'Tyler', 'Kayla', 'Zachary', 'Victoria','Christopher', 'Brianna', 'Alexander', 'Samantha']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts', 'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes', 'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 'Cooper', 'Peterson', 'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox']

street_names = ['Main St', 'Oak St', 'Pine St', 'Maple St', 'Cedar St', 'Elm St', 'Washington St', 'Lake St', 'Hill St', 'Sunset Blvd', 'Broadway', 'High St', 'Park Ave', '2nd St', '3rd St', '4th St', '5th St', '6th St', '7th St', '8th St', '9th St', '10th St', '11th St', '12th St', '13th St', '14th St', '15th St', '16th St', '17th St', '18th St', '19th St', '20th St', '21st St', '22nd St', '23rd St', '24th St', '25th St', '26th St', '27th St', '28th St', '29th St', '30th St', '31st St', '32nd St', '33rd St', '34th St', '35th St', '36th St', '37th St', '38th St', '39th St', '40th St', '41st St', '42nd St', '43rd St', '44th St', '45th St', '46th St', '47th St', '48th St', '49th St', '50th St', '51st St', '52nd St', '53rd St', '54th St', '55th St', '56th St', '57th St', '58th St', '59th St', '60th St', '61st St', '62nd St', '63rd St', '64th St', '65th St', '66th St', '67th St', '68th St', '69th St', '70th St']

real_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte', 'San Francisco', 'Indianapolis', 'Seattle', 'Denver', 'Washington D.C.', 'Boston', 'El Paso', 'Nashville', 'Detroit', 'Oklahoma City', 'Portland', 'Las Vegas', 'Memphis', 'Louisville', 'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Mesa', 'Kansas City', 'Atlanta', 'Long Beach', 'Colorado Springs', 'Raleigh', 'Miami', 'Virginia Beach', 'Omaha', 'Oakland', 'Minneapolis', 'Tulsa', 'Arlington', 'New Orleans', 'Wichita', 'Cleveland', 'Tampa', 'Bakersfield', 'Aurora', 'Honolulu', 'Anaheim', 'Santa Ana', 'Corpus Christi', 'Riverside', 'Lexington', 'St. Louis', 'Stockton', 'Pittsburgh', 'Saint Paul', 'Cincinnati', 'Anchorage', 'Henderson', 'Greensboro', 'Plano', 'Newark']

fake_cities = ['Springfield', 'Rivendell', 'Gotham', 'Metropolis', 'Hogsmeade', 'Atlantis', 'El Dorado', 'Zion', 'Narnia', 'Wakanda', 'Asgard', 'Camelot', 'Mordor', 'Hyrule', 'Krypton', 'Pandora', 'Neverland', 'Emerald City', 'Sunnydale', 'Hill Valley', 'Bikini Bottom', 'Duckburg', 'Bedrock', 'Springfield', 'Quahog', 'South Park', 'Arlen', 'Langley Falls', 'Pawnee', 'Eureka', 'Stars Hollow', 'Cabot Cove', 'Bon Temps', 'Mystic Falls', 'Sunnydale', 'Tree Hill', 'Rosewood', 'Beacon Hills', 'Mystic Falls', 'Sunnydale', 'Tree Hill', 'Rosewood', 'Beacon Hills', 'Mystic Falls', 'Sunnydale', 'Tree Hill', 'Rosewood', 'Beacon Hills', 'Mystic Falls', 'Sunnydale', 'Tree Hill', 'Rosewood', 'Beacon Hills', 'Mystic Falls', 'Sunnydale', 'Tree Hill', 'Rosewood', 'Beacon Hills', 'Mystic Falls', 'Sunnydale', 'Tree Hill', 'Rosewood', 'Beacon Hills']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV','WI','WY', 'YM', 'SK']

# def generate_password( length = 8):
#     if length < 8:
#         print("Password should be at least 8 characters long.")
#         return None
    
#     # Define the character sets
#     uppercase_letters = string.ascii_uppercase
#     lowercase_letters = string.ascii_lowercase
#     digits = string.digits
#     punctuation = string.punctuation
    
#     # Ensure the password includes at least one character from each set
#     password = [
#         random.choice(uppercase_letters),
#         random.choice(lowercase_letters),
#         random.choice(digits),
#         random.choice(punctuation)
#     ]
    
#     # Fill the remaining length with a mix of all character sets
#     all_characters = uppercase_letters + lowercase_letters + digits + punctuation
#     password += random.choices(all_characters, k=length - 4)
    
#     # Shuffle the password list to avoid predictable patterns
#     random.shuffle(password)
    
#     # Join the list into a string and return it
#     return ''.join(password)

def generate_password(length = 8):
    if length < 8:
        print("Password should be at least 8 characters long.")
        return None 
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(punctuation)
    ]
    all_characters = uppercase_letters + lowercase_letters + digits + punctuation
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)
    

for number in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone_number = f"77{random.randint(100, 999)}{random.randint(100, 999)}"

    street_number = random.randint(1000, 9999)
    street= random.choice(street_names)
    # city = random.choice(real_cities + fake_cities)
    city = random.choice(real_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f"{street_number} {street}, {city}, {state} {zip_code}"

    email = f"{first.lower()}{last.lower()}@gmail.com"

    password = generate_password(12)

    print("----------------------------------------------------")
    print(f"{number}.{first} {last}\nPhone: {phone_number}\nAddress: {address}\nEmail: {email}\nPassword: {password}\n")
