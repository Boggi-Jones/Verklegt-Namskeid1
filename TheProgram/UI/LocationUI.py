from Logic.LogicMain import LogicMain
from Models.Location import Location

class LocationUI():
    def __init__(self):
        self.logic = LogicMain()

    def location_loop(self):
        while True:
            choice = input("""\n -----------------------------------------------------------------------------
 | Welcome to NaN Air -> Rental Location information                         |
 -----------------------------------------------------------------------------
 | "Choose number to continue to next window"                                |
 | "Choose "4" to Go back"                                                   |
 |                                                                           |
 | 1. Edit rental location                                                   |
 | 2. All locations                                                          |
 | 3. Search Location                                                        |
 | 4. <- Go back                                                             |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice: """)

            if choice == "1":
                self.edit_location()
            elif choice == "2":
                self.all_locations()
            elif choice == "3":
                self.search_location()
            elif choice == "4":
                break
            else:
                print("Invalid choice!")

    def edit_location(self):
        while True:
            choice = input('''\n -----------------------------------------------------------------------------
 | -> Rental Location information -> Edit rental location                    |
 -----------------------------------------------------------------------------
 | "Choose number to continue to next window"                                |
 | "Choose "4" to Go back"                                                   |
 |                                                                           |
 | 1. Add location                                                           |
 | 2. Remove location                                                        |
 | 3. Update location information                                            |
 | 4. <- Go Back                                                             |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice: ''')

            if choice == "1":
                self.add_location()
            elif choice == "2":
                self.remove_location()
            elif choice == "3":
                self.update_location()
            elif choice == "4":
                break
            else:
                print("Invalid choice!")

    def add_location(self):
        print('''\n -----------------------------------------------------------------------------
 | -> -> Edit rental location -> Add location                                |
 -----------------------------------------------------------------------------
 | "Insert the following information"                                        |
 |                                                                           |
 | Airport Name(city):                                                       |
 | Country:                                                                  |
 | Opening hours:                                                            |
 | Phone number:                                                             |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------''')
        name_of_airport = input(" | Airport name: ").capitalize()
        while self.logic.input_checking(10, name_of_airport) == False:
            print(" | Only characters are viable for input!")
            name_of_airport = input(" | Airport name: ")
        country = input(" | Country: ")
        while self.logic.input_checking(10, country) == False:
            print(" | Only characters are viable for input!")
            country = input(" | Country: ")
        opening_hours = input(" | Opening hours: ")
        while self.logic.input_checking(9, opening_hours) == False:
            print(" | Input must be of format, fx. 01:00-20:00.")
            opening_hours = input(" | Opening hours: ")
        phone_number = input(" | Phone number: ")
        while self.logic.input_checking(2, phone_number) == False:
            print(" | Input must contain 7 digits.")
            phone_number = input(" | Phone number: ")
        the_location = Location(name_of_airport, country, opening_hours, phone_number)

        print('''\n -----------------------------------------------------------------------------
 | -> -> Edit location -> Add location                                       |
 -----------------------------------------------------------------------------
 |                     "New location information"                            |
 |                                                                           |
 | Country:             {:25s}                            |
 | Airport Name:        {:25s}                            |
 | Opening hours:       {:25s}                            |
 | Phone number:        {:25s}                            |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------'''.format(country, name_of_airport, opening_hours, phone_number))
        input(" | Push 'Enter' to continue")

        choice = input(" | Do you want to save and continue? (Y / N): ").lower()
        if choice == "y":
            self.logic.location(1, None, None, the_location)
            print('''\n ------------------------------------------------------------------------------
 | -> -> Edit location -> Add location                                        |
 ------------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                The following location has been added:                      |
 |                {:48s}            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(name_of_airport))
            input(" | Push 'Enter' to continue")
        elif choice =="n":
            print('''\n -----------------------------------------------------------------------------
 | -> -> Edit location -> Add location                                        |
 ------------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |               The following location has not been added:                   |                
 |               {:48s}             |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(name_of_airport))
            input(" | Push 'Enter' to continue")
        else:
            return None

    def remove_location(self):
        location_name = input(" | Enter airport name: ").capitalize()

        while self.logic.input_checking(10, location_name) == False:
            print(" | Only characters are viable for input!")
            location_name = input(" | Enter airport name: ")

        result = self.logic.location(0, location_name, "name_of_airport", None)
        while result == []:
            print(" | This airport is not registered!")
            location_name = input(" | Enter airport name: ")
            result = self.logic.location(0, location_name, "name_of_airport", None)

        choice = input(" | Are you sure you want to remove '{}' ? (Y / N): ".format(location_name)).lower()
        if choice == "y":
            self.logic.location(2, location_name, None, None)
            print('''\n -----------------------------------------------------------------------------
 | -> -> Edit Location -> Remove location                                     |
 -----------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                The following location has been removed:                    |
 |                {:48s}            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(location_name))
            input("Press 'Enter' to continue")
        elif choice == "n":
            print('''\n -----------------------------------------------------------------------------
 | -> -> Edit Location -> Remove location                                     |
 -----------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                The following location has not been removed:                |
 |                {:48s}            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(location_name))
            input("Press 'Enter' to continue")
            return
        else:
            return None

    def update_location(self):
        while True:
            find_location = input(" | Enter airport name: ").capitalize()
            while self.logic.input_checking(10, find_location) == False:
                print(" | Only characters are viable for input!")
                find_location = input(" | Enter airport name: ")
            the_airport = self.logic.location(0, find_location, "name_of_airport", None)
            if the_airport == []:
                print("This airport is not registered!")
                input("Press 'Enter to continue")
                continue

            attribute = input('''\n -----------------------------------------------------------------------------
 | -> -> Edit Location -> Update location                                     |
 |                                                                            |
 | What attribute would you like to change:                                   |
 | 1. Opening hours:           {:26s}                     |
 | 2. Phone number:            {:26s}                     |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
  -----------------------------------------------------------------------------
 | Choice: '''.format(the_airport[0].opening_hours, the_airport[0].phone_number))

            if attribute == "1":
                attribute = "opening_hours"
                new_info = input(" | Enter new information: ")
                while self.logic.input_checking(9, new_info) == False:
                    print(" | Input must be of format, fx. 01:00-20:00.")
                    new_info = input(" | Enter new information: ")
            elif attribute == "2":
                attribute = "phone_number"
                new_info = input(" | Enter new information: ")
                while self.logic.input_checking(2, new_info) == False:
                    print(" | Input must contain 7 digits.")
                    new_info = input(" | Enter new information: ")
            else:
                print(" | Wrong input!")
                continue

            updated_airport = self.logic.location(3, find_location, attribute,  new_info)
            print('''\n -----------------------------------------------------------------------------
 | -> -> Edit Location -> Update location                                     |
 |                                                                            |
 | "New info"                                                                 |
 | 1. Aiport name:        {:31s}                     |
 | 2. Country:            {:31s}                     |
 | 3. Opening hours:      {:31s}                     |
 | 4. Phone number:       {:31s}                     |
 |                                                                            |
 |                                                                            |
 |                                                                            |
  ------------------------------------------------------------------------------
  '''.format(updated_airport.name_of_airport, updated_airport.country, updated_airport.opening_hours, updated_airport.phone_number))
            input(" | Press 'Enter' to continue")
            break

    def all_locations(self):
        results = self.logic.location(0, None, None, None)
        print('''\n -----------------------------------------------------------------------------
 | Rental Locations -> All location                                          |
 -----------------------------------------------------------------------------
 |  Airport name:              | Country:        | Opening hours:      | Phone number:      |''')
        print(" ---------------------------------------------------------------------------------------------------------------------------------")
        for location in results:
            print(''' |  {}  |'''.format(str(location)))
        print(" ---------------------------------------------------------------------------------------------------------------------------------")
        input(" | Press 'Enter' to continue")
        return results


    def search_location(self):
        location = input(" | Enter airport name: ")

        while self.logic.input_checking(10, location) == False:
            print(" | Only characters are viable for input!")
            location = input(" | Enter airport name: ")
        result = self.logic.location(0, location, "name_of_airport", None)

        if result == []:
            print(" | This airport is not registered!")
            input(" | Press 'Enter' to continue")

        else:
            print("""\n -----------------------------------------------------------------------------
 | Rental Location information -> Search location                            |
 -----------------------------------------------------------------------------""")
        for airport in result:
            print(''' | 'Location information'                                                    |
 | Airport name:  {:53s}      |
 | Country:       {:53s}      |
 | Opening hours: {:53s}      |
 | Phone number:  {:53s}      |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 ----------------------------------------------------------------------------- '''.format(airport.name_of_airport, airport.country, airport.opening_hours, airport.phone_number))
            input(" | Press 'Enter' to continue ")

