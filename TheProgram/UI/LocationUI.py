from UI.UIMain import UIMain
from Logic.LogicMain import LogicMain

class UILocation():
    def __init__(self):
        self.logic = LogicMain()
        self.ui = UIMain()

    def location_loop(self):
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
        edit_location()
    elif choice == "2":
        all_locations()
    else:
        print("Invalid choice!")

    def edit_location():


    def all_locations():
        results = self.logic.all_locations()
        print("\nAll locations: ")
        for location in results:
            print(location)