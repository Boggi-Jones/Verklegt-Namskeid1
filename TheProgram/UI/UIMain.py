from UI.ContractUI import ContractUI
from UI.EmployeeUI import EmployeeUI
from UI.LocationUI import LocationUI
from UI.FleetUI import FleetUI
from Logic.LogicMain import LogicMain

class UIMain():
    def __init__(self):
        self.logic = LogicMain()
        self.UILoop()

    def UILoop(self):
        while True:
            choice = input('''\n ---------------------------------------------------------------------------------------------------------------------
 |                             Welcome to NaN Air                                                                    | 
 ---------------------------------------------------------------------------------------------------------------------
 | "Choose number to continue to next window"                                                                        |
 | "Choose "q" to quit"                                                                                              |
 |                                                                                                                   |
 | 1. Employee accounts                                                                                              |
 | 2. Manage vehicles                                                                                                |
 | 3. Rental Locations                                                                                               |
 | 4. Contracts                                                                                                      |
 | 5. Business reports                                                                                               |
 | q. Quit                                                                                                           |
 |                                                                                                                   |
 |                                                                                                                   |
 |                                                                                                                   |
 ---------------------------------------------------------------------------------------------------------------------
 | Choice: ''').lower()
            if choice == "1":
                EmployeeUI().employee_loop()
            elif choice == "2":
                FleetUI().fleet_loop()
            elif choice == "3":
                LocationUI().location_loop()
            elif choice == "4":
                ContractUI().contract_loop()
            elif choice == "5":
                pass            # Þurfum að bæta við klasa
            elif choice == "q":
                break
            else:
                print(" | Invalid entry")