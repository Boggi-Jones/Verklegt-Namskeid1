from Logic.LogicMain import LogicMain
from Models.Vehicle import Vehicle

class FleetUI():
    def __init__(self):
        self.logic = LogicMain()

    def fleet_loop(self):
        ''' Here we go from the main menu to the main menu for the Vehicles '''
        while True:
            fleet_choice = input(''' -----------------------------------------------------------------------------
 | Welcome to NaN Air -> Manage vehicles                                     | 
 -----------------------------------------------------------------------------
 | "Choose number to continue to next window"                                |
 | "Choose "3" to go back"                                                   |
 |                                                                           |
 | 1. Edit vehicle                                                           |
 | 2. All vehicles                                                           |
 | 3. <- Go back                                                             |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice: ''')
            if fleet_choice == "1":
                self.edit_vehicle()
            elif fleet_choice == "2":
                self.all_vehicles()
            elif fleet_choice == "3":
                break
            else:
                print(''' -----------------------------------------------------------------------------
 | Welcome to NaN Air -> Manage vehicles                                     | 
 -----------------------------------------------------------------------------
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                              "Invalid entry"                              |
 |                       "You need to choose one of the                      |
 |                         correct options available"                        |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------''')
                input(" | Press any key to continue: ")

    def edit_vehicle(self):
        while True:
            edit_choice = input(''' -----------------------------------------------------------------------------
 | -> Manage vehicles -> Edit vehicles                                       | 
 -----------------------------------------------------------------------------
 | "Choose number to continue to next window"                                |
 | "Choose "4" to go back"                                                   |
 |                                                                           |
 | 1. Add vehicle                                                            |
 | 2. Remove vehicle                                                         |
 | 3. Update vehicle information                                             |
 | 4. <- Go back                                                             |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice: ''')
            if edit_choice == "1":
                self.add_vehicle()
            elif edit_choice == "2":
                self.remove_vehicle()
            elif edit_choice == "3":
                self.update_vehicle_information()
            elif edit_choice == "4":
                break
            else:
                print(''' -----------------------------------------------------------------------------
 | Welcome to NaN Air -> Manage vehicles                                     | 
 -----------------------------------------------------------------------------
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                              "Invalid entry"                              |
 |                       "You need to choose one of the                      |
 |                         correct options available"                        |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------''')
                input(" | Press any key to continue: ")
    def add_vehicle(self):
        while True:
            print(''' -----------------------------------------------------------------------------
 | -> -> Edit vehicles -> Add vehicle                                        | 
 -----------------------------------------------------------------------------
 | "Insert Information"                                                      |
 | Status:                                                                   |
 | Vehicle type:                                                             |
 | Model:                                                                    |
 | Rate:                                                                     |
 | Manufacturer:                                                             |
 | Condition:                                                                |
 | Model year:                                                               |
 | Color:                                                                    |
 | Number plate:                                                             |
 | Required license:                                                         |
 | Rent:                                                                     |
 | Airport:                                                                  |
 -----------------------------------------------------------------------------''')
            status = input(" | Status: ")
            type_of_vehicle = input(" | Vehicle type: ")
            model = input(" | Model: ")
            rate = input(" | Rate: ")
            manufacturer = input(" | Manufacturer: ")
            condition = input(" | Condition: ")
            model_year = input(" | Model year: ")
            color = input(" | Color: ")
            number_plate = input(" | Number plate: ")
            driving_license = input(" | License required: ")
            rent_counter = input(" | Rent: ")
            name_of_airport = input(" | Airport: ")
            the_vehicle = Vehicle(status, type_of_vehicle, model, rate, manufacturer, condition, model_year, color, number_plate, driving_license, rent_counter, name_of_airport)

            print(''' -----------------------------------------------------------------------------
 | -> -> Edit vehicles -> Add vehicle                                        | 
 -----------------------------------------------------------------------------
 |                                                                           |
 | Status:              {}                                                   |
 | Vehicle type:        {}                                                   |
 | Model:               {}                                                   |
 | Rate:                {}                                                   |
 | Manufacturer:        {}                                                   |
 | Condition:           {}                                                   |
 | Model year:          {}                                                   |
 | Color:               {}                                                   |
 | Number plate:        {}                                                   |
 | Required license:    {}                                                   |
 | Rent:                {}                                                   |
 | Airport:             {}                                                   |
 -----------------------------------------------------------------------------'''.format(status, type_of_vehicle, model, rate, manufacturer, condition, model_year, color, number_plate, driving_license, rent_counter, name_of_airport))
            add_choice = input(" | Do you want to save and continue (Y / N) : ").lower()
            if add_choice == "y":
                self.logic.vehicle(2, None, None, the_vehicle)
                break
            elif add_choice =="n":
                return
            else:
                return None

    def remove_vehicle(self):
        '''Takes employee name input from user, and compares it
        to list of all employee. If name exists it will delete
        if the user wishes to do so'''
        find_vehicle = input("Enter employee name: ")
        self.logic.vehicle(1, find_vehicle, None, None)
        print("Vehicle has been removed!")

    def update_vehicle_information(self):
        while True:
            find_vehicle = input("Enter employee SSN: ")
            attribute = input('''--------------------------------------------
 What attribute would you like to change: 
1. Status:
2. Vehicle type:
3. Rate:
4. Manufacturer:
5. Condition:
6. Model year:
7. Color:
8. Number plate:
9. Required license:
10. Rent:
11. Airport:
--------------------------------------------
choice(Enter the number): ''')
            
            if attribute == "1":
                attribute = "Status"
            elif attribute == "2":
                attribute = "Vehicle type"
            elif attribute == "3":
                attribute = "Rate"
            elif attribute == "4":
                attribute = "Manufacturer"
            elif attribute == "5":
                attribute = "Condition"
            elif attribute == "6":
                attribute = "Model year"
            elif attribute == "7":
                attribute = "Color"
            elif attribute == "8":
                attribute = "Number plate"
            elif attribute == "9":
                attribute = "Required license"
            elif attribute == "10":
                attribute = "Rent"
            elif attribute == "11":
                attribute = "Airport"
            else:
                print("Wrong input")
                continue    
            new_vehicle_info = input("Enter new information: ")
            self.logic.vehicle(3, find_vehicle, attribute,  new_vehicle_info)
            break

    def all_vehicles(self):
        get_all = self.logic.vehicle(0, None, None, None)
        print("\n------------ All Vehicles ------------------")
        for vehicle in get_all:
            print(vehicle)
        print("--------------------------------------------")