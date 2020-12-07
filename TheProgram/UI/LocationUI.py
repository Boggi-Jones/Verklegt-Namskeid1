from Logic.LogicMain import LogicMain
from Models.Location import Location

class LocationUI():
    def __init__(self):
        self.logic = LogicMain()
        #self.ui = UIMain()

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
 | Country:                                                                  |
 | Airport Name(city):                                                       |
 | Opening hours:                                                            |
 | Phone number:                                                             |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------''')
        country = input(" | Country: ")
        name_of_airport = input(" | Airport name: ")
        opening_hours = input(" | Opening hours: ")
        phone_number = input(" | Phone number: ")
        the_location = Location(name_of_airport, country, opening_hours, phone_number)

        print('''\n -----------------------------------------------------------------------------
 | -> -> Edit location -> Add location                                     |
 -----------------------------------------------------------------------------
 |                                                                           |
 |                                                                           |
 | Country:             {:25s}                            |
 | Airport Name(city):  {:25s}                            |
 | Opening hours:       {:25s}                            |
 | Phone number:        {:25s}                            |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------'''.format(name_of_airport, country, opening_hours, phone_number))
        choice = input("Do you want to save and continue? (Y / N): ").lower()
        if choice == "y":
            self.logic.location(1, None, None, the_location)
        elif choice =="n":
            return
        else:
            return None

    def remove_location(self):
        location_name = input("""\n  -----------------------------------------------------------------------------
 | -> -> Edit Location -> Remove location                               |
 -----------------------------------------------------------------------------
 | "Insert the following information"                                        |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 Enter location name: """)
        choice = input("""\n -----------------------------------------------------------------------------
 | -> -> Edit location -> Remove location                                    |
 -----------------------------------------------------------------------------
 | "Insert the following information"                                        |
 |                                                                           |
 | Enter location name: {:25s}                            |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Are you sure you want to remove this location? (Y / N): """.format(location_name)).lower()
        if choice == "y":
            self.logic.location(2, location_name, None, None)
            print('''\n -----------------------------------------------------------------------------
 | -> -> Edit Location -> Remove location                                     |
 -----------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                "{}" has been removed from the system:{:27s}|
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(location_name, ""))
        elif choice == "n":
            print('''\n -----------------------------------------------------------------------------
 | -> -> Edit Location -> Remove location                                     |
 -----------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                "{}" has not been removed from the system:{:23s}|
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(location_name, ""))
            return
        else:
            return None

    def update_location(self):
        while True:
            find_location = input(" | Enter airport name: ")
            the_airport = self.logic.location(0, find_location, "name_of_airport", None)
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
  ------------------------------------------------------------------------------
 | Choice: '''.format(the_airport[0].opening_hours, the_airport[0].phone_number))

            if attribute == "1":
                attribute = "opening_hours"
            elif attribute == "2":
                attribute = "phone_number"
            else:
                print(" | Wrong input")
                continue
            new_info = input(" | Enter new information: ")
            updated_airport = self.logic.location(3, find_location, attribute,  new_info)
            print('''\n -----------------------------------------------------------------------------
 | -> -> Edit Location -> Update location                                     |
 |                                                                            |
 | "New info"                                                                 |
 | 1. Aiport name:        {:30s}                     |
 | 2. Country:            {:30s}                     |
 | 3. Opening hours:      {:30s}                     |
 | 4. Phone number:       {:30s}                     |
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
 -----------------------------------------------------------------------------''')
        for location in results:
            print(" |  " , location , "  |")
        print(" -----------------------------------------------------------------------------")
        input(" | Press 'Enter' to continue")


    def search_location(self):
        location = input(" | Enter airport name: ")
        result = self.logic.location(0, location, "name_of_airport", None)
        print("""\n -----------------------------------------------------------------------------
 | Rental Location information -> Search location                            |
 -----------------------------------------------------------------------------""")
        for airport in result:
            print(" | Location information: ", airport, '''
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 ----------------------------------------------------------------------------- ''')
        input(" | Press 'Enter' to continue ")
        #for airport in result:
        #    print("\n--------------- Location Result: -----------------","\n" "Location information: ", airport)
        #print("--------------------------------------------------")

