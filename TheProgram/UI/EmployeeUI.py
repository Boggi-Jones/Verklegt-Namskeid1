#from UI.UIMain import UILoop
from Logic.LogicMain import LogicMain
from Models.Employee import Employee

class EmployeeUI():
    def __init__(self):
        #self.uiloop = UILoop()
        self.logic = LogicMain()

    def employee_loop(self):
        ''' Skv. wireframe. Valmynd fyrir UIemployee - klasann. Út frá þessu er hægt
        að fara í "Manage employee, All employees o.s.frv." '''

        while True:
            employee_choice = input(''' -----------------------------------------------------------------------------
 | Welcome to NaN Air  -> Employee accounts                                  | 
 -----------------------------------------------------------------------------
 | "Choose number to continue to next window"                                |
 | "Choose "4" to go back"                                                   |
 |                                                                           |
 | 1. Manage employee                                                        |
 | 2. All employees                                                          |
 | 3. Search employee                                                        |
 | 4. <- Go back                                                             |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice: ''')
            if employee_choice == "1":
                self.manage_employee()
            elif employee_choice == "2":
                self.get_all_employees()
            elif employee_choice == "3":
                self.search_employee()
            elif employee_choice == "4":
                break
            else:
                ("Invalid entry")

    def manage_employee(self):

        while True:
            employee_options = input(''' -----------------------------------------------------------------------------
 | -> Employee accounts -> Manage employee                                   | 
 -----------------------------------------------------------------------------
 | "Choose number to continue to next window"                                |
 | "Choose "4" to go back"                                                   |
 |                                                                           |
 | 1. Add employee                                                           |
 | 2. Remove employee                                                        |
 | 3. Update employee information                                            |
 | 4. <- Go back                                                             |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice: ''')
            if employee_options == "1":
                self.add_employee()
            elif employee_options == "2":
                self.remove_employee()
            elif employee_options == "3":
                self.update_employee()
            elif employee_options == "4":
                break
            else:
                print("Invalid entry")

    def add_employee(self):
        print(''' -----------------------------------------------------------------------------
 | -> -> Manage employee -> Add employee                                     | 
 -----------------------------------------------------------------------------
 |            Insert the following information                               |
 |                                                                           |
 | Name:                                                                     |
 | SSN:                                                                      |
 | Address:                                                                  |
 | Home phone:                                                               |
 | Smart phone:                                                              |
 | Email:                                                                    |
 | Location:                                                                 |
 | Company role:                                                             |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------''')
        name = input("Name: ")
        ssn = input("SSN: ")
        address = input("Address: ")
        home_phone = input("Home phone: ")
        smart_phone = input("Smart phone: ")
        email = input("Email: ")
        location = input("Location: ")
        role = input("Company role: ")
        the_employee = Employee(name, ssn, address, home_phone, smart_phone, email, location, role)

        print('''----------- Add employee ------------------
|        """Insert information"""          |
|Name:         {:25s}   |
|SSN:          {:25s}   |
|Address:      {:25s}   |
|Home phone:   {:25s}   |
|Smart phone:  {:25s}   |
|Email:        {:25s}   |
|Location:     {:25s}   |
|Company role: {:25s}   |
|                                          |
--------------------------------------------'''.format(name, ssn, address, home_phone, smart_phone, email, location, role))
        
        
        
        choice = input("ARE YOU SURE YOU WANT TO SAVE INFO AND CONTINUE Y/N: ").lower()
        if choice == "y":
            self.logic.employee(2, None, None, the_employee)
        elif choice =="n":
            return
        else:
            return None

    def remove_employee(self):
        '''Takes employee name input from user, and compares it
        to list of all employee. If name exists it will delete
        if the user wishes to do so'''
        find_employee = input("Enter employee name: ")
        self.logic.employee(1, find_employee, None, None)
        print("Employee has been removed!")

    def update_employee(self):
        while True:
            find_employee = input("Enter employee SSN: ")
            attribute = input(''' -----------------------------------------------------------------------------
 | -> -> Manage employee -> Updaate employee                                 | 
 -----------------------------------------------------------------------------
 | "Select attribute you would like to change"                               |
 |                                                                           |
 | 1. Address:                                                               |
 | 2. Home phone:                                                            |
 | 3. Smart phone:                                                           |
 | 4. Email:                                                                 |
 | 5. Location:                                                              |
 | 6. Company role:                                                          |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice(Enter the number): ''')

            if attribute == "1":
                attribute = "address"
            elif attribute == "2":
                attribute = "home_phone"
            elif attribute == "3":
                attribute = "gsm_phone"
            elif attribute == "4":
                attribute = "email"
            elif attribute == "5":
                attribute = "location"
            elif attribute == "6":
                attribute = "role"
            else:
                print("Wrong input")
                continue    
            new_employee_info = input("Enter new information: ")
            self.logic.employee(3, find_employee, attribute,  new_employee_info)
            break

    def get_all_employees(self):
        results = self.logic.employee(0, None, None, None)
        print("\n------------ All employees ------------------")
        for employee in results:
            print(employee)
        print("--------------------------------------------")

    def search_employee(self):
        employee = input("Enter employee SSN: ")
        result = self.logic.employee(0, employee, "ssn", None)
        for emp in result:
            print("\n--------------- Employee Result: -----------------","\n" "Employee information: ", emp)
        print("--------------------------------------------------")