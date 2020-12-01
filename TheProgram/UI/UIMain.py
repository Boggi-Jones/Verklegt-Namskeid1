from UI.ContractUI import ContractUI
from UI.EmployeeUI import EmployeeUI
from UI.LocationUI import LocationUI
from UI.FleetUI import FleetUI

class UIMain():
    def __init__(self):
        print("Welcome to NaN Air")
        self.Logic = LogicMain()
        self.UILoop()

    def UILoop(self):
        while True:
            choice = print_menu()
            if choice == "1":
                EmployeeUI()
            elif choice == "2":
                FleetUI()
            elif choice == "3":
                LocationUI()
            elif choice == "4":
                ContractUI()
            elif choice == "5":
                pass            # Þurfum að bæta við klasa
            elif choice == "q":
                break
            else:
                print("Invalid entry")

    def print_menu(self):
        MENU_choice = input('''# Veldu nr. til að fara áfram í valmynd
# Veldu "q" til að hætta
#
# 1. Employee accounts
# 2. Manage vehicle fleet
# 3. Rental Locations
# 4. Contracts
# 5. Business reports
# Q. Quit
--------------------------------------------
# choice: ''')
        return MENU_choice