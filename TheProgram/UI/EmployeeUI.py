class EmployeeUI():
    def __init__(self):
        pass

    def employee_loop(self):
        ''' Skv. wireframe. Valmynd fyrir UIemployee - klasann. Út frá eþssu er hægt
        að fara í "Manage employee, All employees o.s.frv." '''
        Employee_options = input('''----------- Employee accounts -----------
1. Manage employee
2. All employees
3. Search employee
b. <- Go back
--------------------------------------------
chocie: ''')
        while True:
            if employee_choice == "1":
                pass
            elif employee_choice == "2":
                pass
            elif employee_choice == "3":
                pass
            elif employee_choice == "b":
                UIMain()
            else:
                ("Invalid entry")

    def employee_manage(self):
        employee_options = input('''----------- Manage employee ------------------
1. Add employee
2. Remove employee
3. Update employee information
--------------------------------------------
choice: ''')
        while True:
            if employee_options == "1":
                pass
            elif employee_options == "2":
                pass
            elif employee_options == "3":
                pass
            else:
                print("Invalid entry")

    def add_employee(self):
        add_menu = print('''----------- Add employee ------------------
        """Insert information"""
Name:
SSN:
Home number:
Smart phone:
Email:
Homa address:
Company role:

" ARE YOU SURE YOU WANT TO SAVE INFO AND CONTINUE Y/N "

<- Back
--------------------------------------------''') # Þurfum að finna betri leið til að útfæra
        name_input = input("Name: ")
        ssn_input = input("SSN: ")
        home_phone_input = input("Home number: ")
        smart_phone_input = input("Smart phone: ")
        email_input = input("Email: ")
        home_address_input = input("Home address: ")
        company_role_input = input("Company role: ")

    def remove_employee(self):
        pass

    def update_employee(self):
        pass
