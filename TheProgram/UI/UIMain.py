#from UI.ContractUI import ContractUI
from UI.EmployeeUI import EmployeeUI
#from UI.LocationUI import LocationUI
#from UI.FleetUI import FleetUI
from Logic.LogicMain import LogicMain

class UIMain():
    def __init__(self):
        print("Welcome to NaN Air")
        self.logic = LogicMain()
        self.UILoop()

    def UILoop(self):
        while True:
            choice = input('''# Veldu nr. til að fara áfram í valmynd
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
            if choice == "1":
                EmployeeUI().employee_loop()
            elif choice == "2":
                #FleetUI()
                pass
            elif choice == "3":
                #LocationUI()
                pass
            elif choice == "4":
                #ContractUI()
                pass
            elif choice == "5":
                pass            # Þurfum að bæta við klasa
            elif choice == "q":
                break
            else:
                print("Invalid entry")