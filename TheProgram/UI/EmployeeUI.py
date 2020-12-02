class EmployeeUI():
    def __init__(self):
        self.uimain = UIMain()

    def employee_loop(self):
        ''' Skv. wireframe. Valmynd fyrir UIemployee - klasann. Út frá þessu er hægt
        að fara í "Manage employee, All employees o.s.frv." '''

        while True:
            employee_choice = input('''----------- Employee accounts -----------
1. Manage employee
2. All employees
3. Search employee
b. <- Go back
--------------------------------------------
chocie: ''')
            if employee_choice == "1":
                manage_employee()
            elif employee_choice == "2":
                all_employees()
            elif employee_choice == "3":
                search_employees()
            elif employee_choice == "b":
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
                add_employee()
            elif employee_options == "2":
                remove_employee()
            elif employee_options == "3":
                update_employee()
            else:
                print("Invalid entry")

    def add_employee(self):
        new_employee = []
        print('''----------- Add employee ------------------
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
        name = input("Name: ")
        ssn = input("SSN: ")
        home_phone = input("Home number: ")
        smart_phone = input("Smart phone: ")
        email = input("Email: ")
        home_address = input("Home address: ")
        company_role = input("Company role: ")
        new_employee.append(name)
        new_employee.append(ssn)
        new_employee.append(home_phone)
        new_employee.append(smart_phone)
        new_employee.append(home_address)
        new_employee.append(company_role)

        print('''----------- Add employee ------------------
        """Insert information"""
Name:         {}
SSN:          {}
Home number:  {}
Smart phone:  {}
Email:        {}
Homa address: {}
Company role: {}

" Press 'Enter' to continue "

<- Back
--------------------------------------------'''.format(name, ssn, home_phone, smart_phone, email, home_address, company_role))
        choice = input("ARE YOU SURE YOU WANT TO SAVE INFO AND CONTINUE Y/N").lower()
        if choice == "y":
            fall(2, None, None, new_employee)
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
        employee = Logic.EmployeeLogic.filteremployees(find_employee)
        if employee != None:
            Logic.EmployeeLogic.editemployeeinfo(employee)
        MENU = ('''Name:
SSN:
Home number:
Smart phone:
Email:
Homa address:
Company role:

" Press 'Enter' to continue "

<- Back
--------------------------------------------''')
        for line, i in enumerate(MENU):
            line += str(employee[i])
            print(line)