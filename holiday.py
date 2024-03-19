
"""
This is a python program that will calculate a user's total holiday cost, viz; the plane cost, hotel cost, and car-rental cost.
• START
• Create a Python file called holiday.py
• Create a class named Holiday
    • Initialise the class by defining a constructor __init__
    • Define __str__ function that will return default values for the __init__ arguemnts
    • Create the following dictionaries:
        •   city_flight_cost for the flight destinations
        •   hotel_price_list for the hotel room types
        •   car_rental_price_list for the car rental type, respectively.
    • Create static methods for the following variable to ensure only integer values are entered:
        •   num_nights
        •   rental_days
    • Define the following menus:
        •   Main menu()
        •   Hotel room types menu room_types_menu()
        •   Car rental types menu car_rental_menu()
    • Create text file to read from as follows:
        •   List of selected city destination to choose from
        •   List of hotel room types to choose from
        •   List of car rental types to choose from
    • Define the following functions to read the text file above
        •   destination_list() to read city flight destinations text file
        •   hotel_room_type_list() to read the hotel room types text file
        •   car_rental_list() to read the car rental types text file
    • Define the following methods to compute hotel, plane, and car rental cost from the respective dictionaries
        •   hotel_cost() method to compute hotel cost from the city_flight_cost dictionary
        •   plane_cost() method to compute flight cost from the hotel_price_list dictionary
        •   car_rental() method to compute rental cost from the car_rental_price_list dictionary
        •   holiday_cost() method to compute the total holiday cost
    •  From here the main program starts:
        •   Call the main menu()
        •   Input a user's flight destination
        •   Validate a users choice of destionation
        •   while user's input for a destination is True:
            •   Call the Hotel room types menu - room_types_menu()
            •   Input a user's choice of hotel room type
            •   Validate a user's choice of hotel room
            •   Input a user's number of nights to stay in the hotel room - this is validated using the @staticMethod - get_integer_num_nights()
            •   Call the car rental type menu - car_rental_menu()
            •   Input a user's choice of rental car
            •   Validate a user's choice of rental car
            •   Input a user's number of days for the rental - this is validated using the @staticMethod - get_integer_rental_days()
            •   Break out of the while loop
        •   Call an instance of the holiday cost menthod:
        •   Holiday.holiday_cost()
        •   print a Goodbye! message.
        •   End while loop
    •   End Holiday Class
END Program
"""


# Holiday Class created
class Holiday():

    # A constructor __init__ defined to initialise Holiday Class
    def __init__(self, city_flight, hotel_room_type, num_nights, car_rental_type, rental_days) -> None:
        self.city_flight = city_flight
        self.hotel_room_type = hotel_room_type
        self.num_nights = num_nights
        self.car_rental_type = car_rental_type
        self.rental_days = rental_days

    # Defined __str__ function to return default values for the __init__ arguemnts
    def __str__(self) -> str:
        return f'''
                City of Flight : {self.city_flight}
                Hotel Room Type : {self.hotel_room_type}
                Number of Nights : {self.num_nights}
                Type of Car Rental : {self.car_rental_type}
                Number of Rental Days : {self.rental_days}
            '''
    # Dictionary containing city_flight_cost for the different destinations
    city_flight_cost = {
            "Argentina": 3111.00,
            "India": 3912.00,
            "Japan": 1190.00,
            "South Africa": 3024.00,
            "Spain": 6235.00,
            "Washington": 2454.00,
            "London": 2343.00,
            "Aberdeen": 4444.00,
            "Manchester": 2343.00,
            "Abuja": 2311.00
        }

    # Dictionary containing hotel_price_list for the hotel room types
    hotel_price_list = {
            "Standard": 150.00,
            "Deluxe": 200.00,
            "Executive": 250.00,
            "Suite": 400.00,
            "Presidential": 1000.00,
            "Family": 600.00,
            "Connecting": 700.00,
            "Penthouse": 2000.00,
            "Accessible": 350.00
        }

    # Dictionary containing car_rental_price_list for the car rental types  
    car_rental_price_list = {
            "Suv": 150.00,
            "Coupe": 50.00,
            "Saloon": 100.00,
            "Lemousine": 250.00,
            "None":0.00
        }
    
    @staticmethod
    def get_integer_num_nights(prompt):
        while True:
            try:
                num_nights = int(input(prompt))
                return num_nights
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    @staticmethod
    def get_integer_rental_days(prompt):
        while True:
            try:
                rental_days = int(input(prompt))
                return rental_days
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    # Main Menu
    def menu():
        menu_note = """
        This is an exciting time to embark on your journey and we have you covered for the following destinations. 
        Try us and you will be glad you did!

        Please, choose your destination from the following options:
        """
        print(menu_note)
        Holiday.destination_list() # calling the city flight function

    # Hotel room types menu
    def room_types_menu():
        room_type_note = """
        To ease your journey and enhance a good experience, we have a variety 
        of hotel reservations for you.

        Please, choose from the list of luxury hotel rooms that fits your budget:
        """
        print(room_type_note)
        Holiday.hotel_room_type_list() # Calling hotel room types function

    # Car rental types menu
    def car_rental_menu():
        car_rental_note = """
        To further ease your journey and enhance a good experience, we have a variety 
        of car rental options.

        Please, choose a car rental that fits your budget:
        """
        print(car_rental_note)
        Holiday.car_rental_list() # calling the car rental list function

    def destination_list():

        # for key in Holiday.city_flight_cost.keys():
        #     print(key)
        # Open the file "cities_to_visit.txt" in read mode using a with statement
        with open("cities_to_visit.txt", "r") as cities:
            # Initialize an empty list to store the cities
            city_list = []

            # Iterate through each line in the file
            for lines in cities:
                # Remove newline characters from the line
                temp = lines.strip('\n')

                # Split the line into words
                temp = temp.split()

                # Join the words into a single string separated by spaces
                joined = " ".join(temp)

                # Append the joined string to the city_list
                city_list.append(joined)

            # Iterate through each city in the list and print it on a separate line
            for city in city_list:
                print(city)

    def hotel_room_type_list():
        
        with open("hotel_room_types.txt", "r") as hotel_rooms:
            
            hotel_room_list = []

            for lines in hotel_rooms:

                temp = lines.strip('\n')

                temp = temp.split()

                joined = " ".join(temp)

                hotel_room_list.append(joined)

            for room in hotel_room_list:
                print(room)

    def car_rental_list():
       
        with open("car_rental_list.txt", "r") as car_rental_types:
            
            car_rental_type_list = []

            for lines in car_rental_types:
                
                temp = lines.strip('\n')

                temp = temp.split()

                joined = " ".join(temp)

                car_rental_type_list.append(joined)

           
            for car in car_rental_type_list:
                print(car)

    # hotel_cost() method to compute hotel cost from the city_flight_cost dictionary   
    def hotel_cost(self, num_nights):
        total_hotel_stay_cost = 0
        for key, value in Holiday.hotel_price_list.items():
            if key == hotel_room_type:
                total_hotel_stay_cost = num_nights * value
        return total_hotel_stay_cost

    # plane_cost() method to compute flight cost from the hotel_price_list dictionary
    def plane_cost(self):
        total_plane_cost = 0
        for key, value in Holiday.city_flight_cost.items():
            
            if key == city_flight:
                total_plane_cost = value
        return total_plane_cost

    # car_rental() method to compute rental cost from the car_rental_price_list dictionary
    def car_rental(self, rental_days):
        total_rental_cost = 0
        for key, value in Holiday.car_rental_price_list.items():
            if key == car_rental_type:
                total_rental_cost = rental_days * value
        return total_rental_cost

    # holiday_cost() method to compute the total holiday cost by creating an instance of the holiday class
    def holiday_cost():
        holiday_instance = Holiday(city_flight, hotel_room_type, num_nights, car_rental_type, rental_days)
        hotel_cost = Holiday.hotel_cost(holiday_instance, num_nights)
        plane_cost = Holiday.plane_cost(holiday_instance)
        rental_cost = Holiday.car_rental(holiday_instance, rental_days)

        total_holiday_cost = hotel_cost + plane_cost + rental_cost
        print(f"""The cost of your flight to {city_flight} is £{plane_cost}, the hotel cost is £{hotel_cost}, and your car rental cost is £{rental_cost}. Therefore, your total Holiday cost is £{total_holiday_cost}.
              """)
        print()


Holiday.menu()

city_flight = input("Please, enter your destination: ").capitalize()


while not city_flight.isalpha() or city_flight not in Holiday.city_flight_cost:
     print("Invalid input. Please enter a valid destination.")
     Holiday.menu()
     city_flight = input("Please, enter your destination: ").capitalize()

# Check while user's input for a destination is True:
while not city_flight == 'none':
    
    
    Holiday.room_types_menu()
    hotel_room_type = input("Please, enter a hotel room type: ").capitalize()

    while not hotel_room_type.isalpha() or hotel_room_type not in Holiday.hotel_price_list:
        print("Invalid input. Please enter a valid hotel room type.")
        Holiday.room_types_menu()
        hotel_room_type = input("Please, enter a hotel room type: ").capitalize()

    
    num_nights = Holiday.get_integer_num_nights("Please, enter the number of nights: ")
    print()

    
    Holiday.car_rental_menu()

    
    car_rental_type = input("Please, enter the type of car to rent: ").capitalize()

    
    while not car_rental_type.isalpha() or car_rental_type not in Holiday.car_rental_price_list:
        print("Invalid input. Please enter a valid type of car to rent.")
        Holiday.car_rental_menu()
        car_rental_type = input("Please, enter a hotel room type: ").capitalize()

    
    rental_days = Holiday.get_integer_rental_days("Enter the number of days for the car rental: ")
    print()
    break


Holiday.holiday_cost()


print("Thank you for using our booking calculator. Goodbye!")
print()

#END