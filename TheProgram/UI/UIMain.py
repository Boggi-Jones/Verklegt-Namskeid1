from UI.ContractUI import ContractUI
from UI.EmployeeUI import EmployeeUI
from UI.LocationUI import LocationUI
from UI.FleetUI import FleetUI
from UI.ReportsUI import ReportsUI
from Logic.LogicMain import LogicMain


class UIMain():
    def __init__(self):
        self.logic = LogicMain()
        self.UILoop()

    def UILoop(self):
        print(" | You must enter your credentials to login the system: ")
        choice = input(" | Press 1 to continue or press 2 for the list of employees: ") 
        if choice == "2":
            employees = self.logic.roles(0, None, None)
            for emp in employees:
                print(emp)
        username = input(" |Enter username: ")
        #logic something username
        password = input(" |Enter password): ")
        #logic something password
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
                ReportsUI().reports_loop()            
            elif choice == "q":
                break
            else:
                print(" | Invalid entry")