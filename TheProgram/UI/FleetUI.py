from Logic.LogicMain import LogicMain
from Models.Vehicle import Vehicle
from UI.LocationUI import LocationUI

class FleetUI():
    def __init__(self):
        self.logic = LogicMain()
        self.locationUI = LocationUI()

    def fleet_loop(self):
        ''' Here we go from the main menu to the main menu for the Vehicles '''
        while True: 
            fleet_choice = input('''\n -----------------------------------------------------------------------------
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
                print(" | Invalid choice !")
                input(" | Press any key to continue")

    def edit_vehicle(self):
        while True:
            edit_choice = input('''\n -----------------------------------------------------------------------------
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
                print(" | Invalid choice !")
                input(" | Press 'Enter' to continue")

    def add_vehicle(self):
        while True:
            print('''\n -----------------------------------------------------------------------------
 | -> -> Edit vehicles -> Add vehicle                                        |
 -----------------------------------------------------------------------------
 | "Insert Information"                                                      |
 | Vehicle type:                                                             |
 | Model:                                                                    |
 | Rate:                                                                     |
 | Manufacturer:                                                             |
 | Model year:                                                               |
 | Color:                                                                    |
 | Number plate:                                                             |
 | Required license:                                                         |
 | Airport:                                                                  |
 -----------------------------------------------------------------------------''')
            
            status = "available"
            type_of_vehicle = input(" | Vehicle type: ").capitalize()
            model = input(" | Model: ").capitalize()
            rate = input(" | Rate: ")
            manufacturer = input(" | Manufacturer: ").capitalize()
            condition = "Good"
            model_year = input(" | Model year: ")
            
            while self.logic.input_checking(8, model_year) == False:
                print("Model year has to be of length 4 and only numbers, fx: 1234")
                model_year = input(" | Model year: ")

            color = input(" | Color: ").capitalize()

            number_plate = input(" | Number plate: ").upper()
            
            while self.logic.input_checking(11, number_plate) == False:
                print(" | Number plate has to be two letters and three numbers: 'AA 123'")
                number_plate = input(" | Number plate: ").upper()
            driving_license = input(" | License required: ")
            
            while self.logic.input_checking(4, driving_license) == False:
                print(" | Drivers license has to be 'a', 'b' or 'c' or a combination of any of the three!").upper()
                driving_license = input(" | License required: ")
            rent_counter = "0"
            
            print(''' | Please select an airport from the following locations: ''')
            all_locations = self.locationUI.all_locations()
            while all_locations != 0:
                name_of_airport = input(" | Enter name of Airport: ").capitalize()
                for location in all_locations:
                    if location.name_of_airport == name_of_airport:
                        all_locations = 0
                        break
            the_vehicle = Vehicle(status, type_of_vehicle, model, rate, manufacturer, condition, model_year, color, number_plate, driving_license, rent_counter, name_of_airport)

            print('''\n -----------------------------------------------------------------------------
 | -> -> Edit vehicles -> Add vehicle                                        |
 -----------------------------------------------------------------------------
 |                                                                           |
 | Available:           {:40s}             |
 | Vehicle type:        {:40s}             |
 | Model:               {:40s}             |
 | Rate:                {:40s}             |
 | Manufacturer:        {:40s}             |
 | Condition:           {:40s}             |
 | Model year:          {:40s}             |
 | Color:               {:40s}             |
 | Number plate:        {:40s}             |
 | Required license:    {:40s}             |
 | Rent:                {:40s}             |
 | Airport:             {:40s}             |
 -----------------------------------------------------------------------------'''.format(status, type_of_vehicle, model, rate, manufacturer, condition, model_year, color, number_plate, driving_license, rent_counter, name_of_airport))
            input(" | Push 'Enter' to continue")

            add_choice = input(" | Do you want to save and continue? (Y / N): ").lower()
            if add_choice == "y":
                self.logic.vehicle(2, None, None, the_vehicle)
                print('''\n ------------------------------------------------------------------------------
 | -> -> Edit vehicles -> Add vehicle                                         |
 ------------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |              The following vehicle has been added to the fleet:            |
 |              {:62s}|
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(number_plate))
                input(" | Press 'Enter' to continue")
                break
            elif add_choice == "n":
                print('''\n -----------------------------------------------------------------------------
 | -> -> Edit vehicles -> Add vehicle                                         |
 ------------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |            The following vehicle has not been added to the fleet:          |
 |            {:64s}|
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(number_plate))
                input(" | Press 'Enter' to continue")
                break
            else:
                return None

    def remove_vehicle(self):
        '''Takes vehicle name input from user, and compares it
        to list of all vehicles. If name exists it will delete
        if the user wishes to do so'''

        while True:
            find_vehicle = input(" | Enter vehicle plate number: ").upper()
            if self.logic.input_checking(11, find_vehicle) == False:
                print(" | No vehicle with this number plate")
                break

            remove_choice = input(" | Are you sure you want to remove '{}'? (Y / N): ".format(find_vehicle)).lower()
            if remove_choice == "y":
                self.logic.vehicle(3, find_vehicle, None, None)
                print('''\n -----------------------------------------------------------------------------
 | -> Manage vehicles -> Remove vehicle                                      |
 -----------------------------------------------------------------------------
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                  The following vehicle has been removed:                  |
 |                  {:57s}|                                                  
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------'''.format(find_vehicle))
                input(" | Press 'Enter' to continue ")
                break
            elif remove_choice == "n":
                print('''\n -----------------------------------------------------------------------------
 | -> Manage vehicles -> Remove vehicle                                      |
 -----------------------------------------------------------------------------
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                 The following vehicle has not been removed:               |
 |                 {:58s}|                                                  
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------'''.format(find_vehicle))
    

    def update_vehicle_information(self):
        while True:
            find_vehicle = input(" | Enter vehicle plate number: ").upper()
            print("----")
            while self.logic.input_checking(11, find_vehicle) == False:
                print(" | Input has to be of format, fx: AA 111")
                find_vehicle = input(" | Enter vehicle plate number: ").upper()
            chosen_vehicle = self.logic.vehicle(0, find_vehicle, "number_plate", None)
            if chosen_vehicle == []:
                print(" | No vehicle with this number plate")
                input(" | Press 'Enter to continue")
                continue

            attribute = input('''\n -----------------------------------------------------------------------------
 | -> -> Edit vehicles -> Update vehicle information                         |
 -----------------------------------------------------------------------------
 | "Select attribute would you like to change: "                             |
 |                                                                           |
 | 1. Status:            {:52s}|
 | 2. Vehicle type:      {:52s}|
 | 3. Model:             {:52s}|
 | 4. Rate:              {:52s}|
 | 5. Manufacturer:      {:52s}|
 | 6. Condition:         {:52s}|
 | 7. Model year:        {:52s}|
 | 8. Color:             {:52s}|
 | 9. Number plate:      {:52s}|
 | 10. Required license: {:52s}|
 | 11. Rent:             {:52s}|
 | 12. Airport:          {:52s}|
 -----------------------------------------------------------------------------
 | choice: '''.format(chosen_vehicle[0].status, chosen_vehicle[0].type_of_vehicle, chosen_vehicle[0].model, chosen_vehicle[0].rate, chosen_vehicle[0].manufacturer, chosen_vehicle[0].condition, chosen_vehicle[0].model_year, chosen_vehicle[0].color, chosen_vehicle[0].number_plate, chosen_vehicle[0].driving_license, chosen_vehicle[0].rent_counter, chosen_vehicle[0].name_of_airport))

            if attribute == "1":
                attribute = "status"
                new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "2":
                attribute = "type_of_vehicle"
                new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "3":
                attribute = "model"
                new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "4":
                attribute = "rate"
                new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "5":
                attribute = "manufacturer"
                new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "6":
                attribute = "condition"
                new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "7":
                attribute = "model_year"
                new_vehicle_info = input(" | Enter new information: ")
                while self.logic.input_checking(8, new_vehicle_info) == False:
                    print(" | Model year has to be of length 4 and only numbers, fx: 1234")
                    new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "8":
                attribute = "color"
                new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "9":
                attribute = "number_plate"
                new_vehicle_info = input(" | Enter new information: ")
                while self.logic.input_checking(11, new_vehicle_info) == False:
                    print(" | First 2 entrys must be a character then a space then 3 digits, fx. DA 123.")
                    new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "10":
                attribute = "driving_license"
                new_vehicle_info = input(" | Enter new information: ")
                while self.logic.input_checking(4, new_vehicle_info) == False:
                    print(" | Drivers license has to be 'a', 'b' or 'c' or a combination of any of the three!")
                    new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "11":
                attribute = "rent_counter"
                new_vehicle_info = input(" | Enter new information: ")

            elif attribute == "12":
                attribute = "name_of_airport"
                new_vehicle_info = input(" | Enter new information: ")

            else:
                print("Wrong input")
                continue

            self.logic.vehicle(1, find_vehicle, attribute,  new_vehicle_info)
            print('''\n -----------------------------------------------------------------------------
 | -> Manage vehicles -> Remove vehicle                                      |
 -----------------------------------------------------------------------------
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                       "Vehicle {:6s} has been updated"                   |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------'''.format(find_vehicle))
            input(" | Press 'Enter' to continue ")
            if new_vehicle_info == "Stolen":
                print(" | Would you like to report the grand theft auto? ") 
                report_incident = input(" | Y/N: ")
                if report_incident == "Y": 
                    chosen_vehicle = self.logic.vehicle(0, find_vehicle, "number_plate", new_vehicle_info)
                    Incident_airport_filter = chosen_vehicle[11]
                    Incident_country_list = self.logic.location(0, Incident_airport_filter, "country", None)
                    Incident_country = Incident_country_list[1]
                    print(" | Police department of {} has been alerted. Pending investigation. | ").format(Incident_country)
                else: 
                    break
            else:
                break

    def all_vehicles(self):
        get_all = self.logic.vehicle(0, None, None, None)
        print('''\n ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
 |  -> Manage vehicles -> All vehicles                                                                                                                                |
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
 |    Status    | Type of vehicle |     Model     | Rate |   Manufacturer  | Condition | Model year |   Color    | Number plate | License | Counter | Name of airport |
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------''')

        for vehicle in get_all:
            print(" | {} | ".format(str(vehicle)))
        print(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        input(" | Press 'Enter' to continue ")