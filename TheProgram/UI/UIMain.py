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
        '''User must first login with credentials. Then that users permissions will depend on his role'''
        print(" | You must enter your credentials to login the system: ")
        choice = input(" | Press 1 to continue or press 2 for the list of employees: ") 
        if choice == "2":
            employees = self.logic.roles(0, None, None) # print all employees with their ssn and role
            for emp in employees:
                print(emp)
                
        username = input(" | Enter ssn: ")
        while self.logic.input_checking(14, username) == False:
            print(" | user not found! ssn must be in the correct format: 123456-1234")
            username = input(" | Enter ssn: ")
            
        password = input(" | Enter password: ")
        while self.logic.input_checking(15, password) == False: # password in system check
            print(" | Incorrect password!")
            password = input(" | Enter password: ")
        
        the_user = self.logic.roles(0, username, "ssn")
        role_of_user = the_user[0].role.lower()
            
        while True:
            choice = input('''\n ------------------------------------------------------------------------------
 |                             Welcome to NaN Air                             | 
 ------------------------------------------------------------------------------
 | "Choose number to continue to next window"                                 |
 | "Choose "q" to quit"                                                       |
 |                                                                            |
 | 1. Employee accounts                                                       |
 | 2. Manage vehicles                                                         |
 | 3. Rental Locations                                                        |
 | 4. Contracts                                                               |
 | 5. Business reports                                                        |
 | q. Quit                                                                    |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------
 | Choice: ''').lower()
            if choice == "1":
                if role_of_user != "ceo":
                    print(" | Permission denied! ")
                    input(" | Press 'Enter' to continue ")
                    continue
                EmployeeUI().employee_loop()
            elif choice == "2":
                if role_of_user == "base":
                    print(" | Permission denied! ")
                    input(" | Press 'Enter' to continue ")
                    continue
                FleetUI().fleet_loop()
            elif choice == "3":
                if role_of_user != "ceo":
                    print(" | Permission denied! ")
                    input(" | Press 'Enter' to continue ")
                    continue
                LocationUI().location_loop()
            elif choice == "4":
                if role_of_user == "fleet":
                    print(" | Permission denied! ")
                    input(" | Press 'Enter' to continue ")
                    continue
                ContractUI().contract_loop()
            elif choice == "5":
                if role_of_user != "ceo":
                    print(" | Permission denied! ")
                    input(" | Press 'Enter' to continue ")
                    continue
                ReportsUI().reports_loop()
            elif choice == "q":
                break
            else:
                print(" | Invalid entry")