#from UI.UIMain import UIMain
from Logic.LogicMain import LogicMain
from Models.Employee import Employee

class EmployeeUI():
    def __init__(self):
        #self.uimain = UIMain()
        self.logic = LogicMain()

    def employee_loop(self):
        ''' Skv. wireframe. Valmynd fyrir UIemployee - klasann. Út frá þessu er hægt
        að fara í "Manage employee, All employees o.s.frv." '''

        while True:
            employee_choice = input('''----------- Employee accounts -----------
1. Manage employee
2. All employees
3. Search employee
4. <- Go back
--------------------------------------------
chocie: ''')
            if employee_choice == "1":
                self.manage_employee()
            elif employee_choice == "2":
                self.get_all_employees()
            elif employee_choice == "3":
                self.search_employee()
            elif employee_choice == "4":
                self.uimain
            else:
                ("Invalid entry")

    def manage_employee(self):
        employee_options = input('''----------- Manage employee ------------------
1. Add employee
2. Remove employee
3. Update employee information
--------------------------------------------
choice: ''')
        while True:
            if employee_options == "1":
                self.add_employee()
            elif employee_options == "2":
                self.remove_employee()
            elif employee_options == "3":
                self.update_employee()
            elif employee_options == "b":
                break
            else:
                print("Invalid entry")

    def add_employee(self):
        print('''----------- Add employee ------------------
        """Insert information"""
Name:
SSN:
Home number:
Smart phone:
Email:
Homa address:
Company role:

<- Back
--------------------------------------------''') # Þurfum að finna betri leið til að útfæra
        name = input("Name: ")
        ssn = input("SSN: ")
        home_phone = input("Home number: ")
        smart_phone = input("Smart phone: ")
        email = input("Email: ")
        home_address = input("Home address: ")
        postal_code = input("Postal code: ")
        company_role = input("Company role: ")
        the_employee = Employee(name, home_address, postal_code, ssn, home_phone, smart_phone, email, company_role)

        print('''----------- Add employee ------------------
        """Insert information"""
Name:         {}
SSN:          {}
Home number:  {}
Smart phone:  {}
Email:        {}
Home address: {}
Postal code:  {}
Company role: {}

<- Back
--------------------------------------------'''.format(name, ssn, home_phone, smart_phone, email, home_address, postal_code, company_role))
        choice = input("ARE YOU SURE YOU WANT TO SAVE INFO AND CONTINUE Y/N").lower()
        if choice == "y":
            self.logic.employee(2, None, None, the_employee)
        else:
            return None

    def remove_employee(self):
        '''Takes employee name input from user, and compares it
        to list of all employee. If name exists it will delete
        if the user wishes to do so'''
        find_employee = input("Enter employee name: ")
        employee = Logic.EmployeeLogic.filteremployees(find_employee)
        if employee != None:
            Logic.EmployeeLogic.removeemployee(employee)
        else:
            pass

    def update_employee(self):
        find_employee = input("Enter employee name: ")
        self.logic.employee(3, find_employee, None, None)
        MENU = '''Name:
SSN:
Home number:
Smart phone:
Email:
Homa address:
Company role:

" Press 'Enter' to continue "

<- Back
--------------------------------------------'''
    
    def get_all_employees(self):
        results = self.logic.all_employees()
        print("\nAll employees: ")
        for employee in results:
            print(employee)

    def search_employee(self):
        emp = input("Enter employee name: ")
        result = self.logic.employee(0, emp, None)
        print(result)