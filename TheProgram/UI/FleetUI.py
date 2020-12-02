#from UI.UIMain import UIMain
from Logic.LogicMain import LogicMain
from Models.Vehicle import Vehicle

class FleetUI():
    def __init__(self):
        #self.uimain = UIMain()
        self.logic = LogicMain()

    def fleet_loop(self):
        ''' Skv. wireframe. Valmynd fyrir UIFleet - klasann. Út frá þessu er hægt
        að fara í "Manage employee, All employees o.s.frv." '''
        while True:
            fleet_choice = input('''----------- Manage vehicle fleet ------------
1. Edit vehicle
2. All vehicles
3. <- Go back 

--------------------------------------------
chocie: ''')
            if fleet_choice == "1":
                self.edit_vehicle()
            elif fleet_choice == "2":
                self.all_vehicles()
            elif fleet_choice == "3":
                break
            else:
                ("Invalid entry")

    def edit_vehicle(self):
        while True:
            edit_choice = input('''----------- Edit Vehicle ------------------
1. Add vehicle
2. Remove vehicle
3. Update vehicle information
4. Update Vehicle condition
5. <- Go back

--------------------------------------------
chocie: ''')
            if edit_choice == "1":
                self.add_vehicle()
            elif edit_choice == "2":
                self.remove_vehicle()
            elif edit_choice == "3":
                self.update_vehicle_information()
            elif edit_choice == "4":
                break
            else:
                ("Invalid entry")
    
    def add_vehicle(self):
        while True:
            print('''------------- Add Vehicle ------------------
------------ Insert Information ------------
Status:
Vehicle type:
Rate:
Manufacturer:
Condition:
Model year:
Color:
Number plate:
Required license:
Rent:
Airport:
Country:
--------------------------------------------''')
            status = input("Status: ")
            type_of_vehicle = input("Vehicle type: ")
            rate = input("Rate: ")
            manufacturer = input("Manufacturer: ")
            condition = input("Condition: ")
            age = input("Model year: ")
            color = input("Color: ")
            number_plate = input("Number plate: ")
            driving_license = input("License required: ")
            rent_counter = input("Rent: ")
            name_of_airport = input("Airport: ")
            country = input("Country: ")
            the_vehicle = Vehicle(status, type_of_vehicle, rate, manufacturer, condition, age, color, number_plate, driving_license, rent_counter, name_of_airport, country)

            print('''------------- Add Vehicle ----------------
        """Insert information"""
Status:             {}
Vehicle type:       {}
Rate:               {}
Manufacturer:       {}
Condition:          {}
Model year:         {}
Color:              {}
Number plate:       {}
Required license:   {}
Rent:               {}
Airport:            {}
Country:            {}
--------------------------------------------'''.format(status, type_of_vehicle, rate, manufacturer, condition, age, color, number_plate, driving_license, rent_counter, name_of_airport, country))
            add_choice = input("ARE YOU SURE YOU WANT TO SAVE INFO AND CONTINUE Y/N: ").lower()
            if add_choice == "y":
                self.logic.vehicle(2, None, None, the_vehicle)
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
1. Manufacturer:
2. Model:
3. Type:
4. Status:
5. Year:
6. Color:
7. License:
8. Location:
9. Rate:
10. Condition
--------------------------------------------
choice(Enter the number): ''')
            
            if attribute == "1":
                attribute = "Manufacturer"
            elif attribute == "2":
                attribute = "Model"
            elif attribute == "3":
                attribute = "Type"
            elif attribute == "4":
                attribute = "Status"
            elif attribute == "5":
                attribute = "Year"
            elif attribute == "6":
                attribute = "Color"
            elif attribute == "7":
                attribute = "License"
            elif attribute == "8":
                attribute = "Location"
            elif attribute == "9":
                attribute = "Rate"
            elif attribute == "10":
                attribute = "Condition"
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