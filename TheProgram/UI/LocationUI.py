#from UI.UIMain import UIMain
from Logic.LogicMain import LogicMain

class UILocation():
    def __init__(self):
        self.logic = LogicMain()
        #self.ui = UIMain()

    def location_loop(self):
        while True:
            choice = input("""# -------Rental Location information ---------
# 1. Edit rental location
# 2. All locations
#
#
#
#
#
# <- Back
# Choice:__
# --------------------------------------------""")

            if choice == "1":
                self.edit_location()
            elif choice == "2":
                self.all_locations()
            else:
                print("Invalid choice!")

    def edit_location(self):
        while True:
            choice = input(''' ------- Edit rental location ---------
 1. Add location
 2. Remove location
 3. Update location information
 4. Go Back



 <- Back
 Choice:__
 --------------------------------------------''')

            if choice == "1":
                self.add_location()
            elif choice == "2":
                self.remove_location()
            elif choice == "3":
                self.update_location()
            elif choice == "4":
                break
            else:
                print("Invalid choice")

    def add_location(self):
        print('''----------- Add location ------------------
        """Insert information"""
Country:
Location:
Airport Name(city):
Opening hours:
Phone number:

--------------------------------------------''') # Þurfum að finna betri leið til að útfæra
        country = input("Country: ")
        location = input("Location: ")
        airport_name = input("Airport name: ")
        opening_hours = input("Opening hours: ")
        phone_number = input("Phone number: ")
        the_location = Location(country, location, airport_name, opening_hours, phone_number)

        print('''----------- Add employee ------------------
        """Insert information"""
Country:                 {}
Location:                {}
Airport name(city):      {}
Opening hours:           {}
Phone number:            {}

--------------------------------------------'''.format(country, location, airport_name, opening_hours, phone_number))
        choice = input("ARE YOU SURE YOU WANT TO SAVE INFO AND CONTINUE Y/N: ").lower()
        if choice == "y":
            self.logic.location(2, None, None, the_location)
        elif choice =="n":
            return
        else:
            return None

    def remove_location(self):
        location_name = input(""" ------- Remove location ---------
 Enter location name: <- Insert location name





 <- Back
 --------------------------------------------""")
        choice = input("""# ------- Remove location ---------
# Enter location name: {}
#
#
# |Are you sure you want to remove this location?|
# | Y/N:__ |
#
#
#
# <- Back
# --------------------------------------------""".format(location_name)).lower()
        if choice == "y":
            self.logic.location(2, location_name, None, None)
            print("{} has been removed!".format(location_name))
        elif choice == "n":
            return
        else:
            return None

    def update_location(self):
        while True:
            find_location = input("Enter airport name: ")
            attribute = input('''--------------------------------------------
 What attribute would you like to change:
1. Opening hours:
2. Phone number:

--------------------------------------------
chocie(Enter the number): ''')

            if attribute == "1":
                attribute = "opening hours"
            elif attribute == "2":
                attribute = "phone number"
            else:
                print("Wrong input")
                continue
            new_info = input("Enter new information: ")
            self.logic.location(3, find_location, attribute,  new_info)
            break

    def all_locations(self):
        results = self.logic.all_locations(0, None, None, None)
        print("\n------- All locations ---------- ")
        for location in results:
            print(location)
        print("-----------------------------------")