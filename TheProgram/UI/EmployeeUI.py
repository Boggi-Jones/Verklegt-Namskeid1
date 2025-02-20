#from UI.UIMain import UILoop
from Logic.LogicMain import LogicMain
from Models.Employee import Employee
from Models.Role import Role
from Models.Location import Location

class EmployeeUI():
    def __init__(self):
        #self.uiloop = UILoop()
        self.logic = LogicMain()

    def employee_loop(self):
        ''' Takes input from user and sends to one of the options within the employee window'''
        while True:
            employee_choice = input('''\n -----------------------------------------------------------------------------
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
                print(" | Invalid entry")
                input(" | Push enter to continue")

    def manage_employee(self):
        ''' Takes input from user and sends to one of the options within the Manage employee window '''
        while True:
            employee_options = input('''\n -----------------------------------------------------------------------------
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
                print(" | Invalid entry")
                input(" | Push enter to continue")

    def add_employee(self):
        ''' Takes multiple inputs from the user to create an "employee" within the system''' 
        print('''\n -----------------------------------------------------------------------------
 | -> -> Manage employee -> Add employee                                     |
 -----------------------------------------------------------------------------
 |"Insert information"                                                       |
 |                                                                           |
 | Name:                                                                     |
 | SSN:                                                                      |
 | Address:                                                                  |
 | Home phone:                                                               |
 | Smart phone:                                                              |
 | Email:                                                                    |
 | Location:                                                                 |
 | Company role:                                                             |
 | Password:                                                                |
 |                                                                           |
 -----------------------------------------------------------------------------''')
        name = input(" | Name: ").capitalize()

        ssn = input(" | SSN: ")
        while self.logic.input_checking(1, ssn) == False:
            print(" | SSN must be in the correct format: '123456-1234' ")
            ssn = input(" | SSN: ")

        address = input(" | Address: ").capitalize()

        home_phone = input(" | Home phone: ")
        while self.logic.input_checking(2, home_phone) == False:
            print(" | Home phone must be in the correct format: '1234567' ")
            home_phone = input(" | Home phone: ")
        smart_phone = input(" | Smart phone: ")

        while self.logic.input_checking(2, smart_phone) == False:
            print(" | Smart phone must be in the correct format: '1234567' ")
            smart_phone = input(" | Smart phone: ")
        
        email = input(" | Email: ")
        while self.logic.input_checking(0, email) == False:
            print(" | Email must be in the correct format: 'name@name.is' ")
            email = input(" | Email: ")

        location_list = self.logic.locationlogic.filter_country(None, "airport_name")
        print(''' | Choose the location: 
 -------------------------------------------------------------------------------------------------------''')
        for row in location_list:
            print(" | ",row," | ")
        print(" -------------------------------------------------------------------------------------------------------")
        location = input(" | Location: ").capitalize()
        while self.logic.input_checking(12,location) == False:
            print(" | '{}' is not registered!".format(location))
            location = input(" | Location: ").capitalize()
                       
        role = input(" | Company role: ").capitalize()
        while self.logic.input_checking(3, role) == False:
            print(" | company role is either 'ceo', 'fleet' or 'base'!")
            role = input(" | Company role: ").capitalize()
            
        password = input(" | Password: ")

        the_employee = Employee(name, ssn, address, home_phone, smart_phone, email, location, role, password)
        employee_roles = Role(role, name, ssn)
        print('''\n -----------------------------------------------------------------------------
 | -> -> Manage employee -> Add employee                                     |
 -----------------------------------------------------------------------------
 |                      "New employee information"                           |
 |Name:         {:58s}   |
 |SSN:          {:58s}   |
 |Address:      {:58s}   |
 |Home phone:   {:58s}   |
 |Smart phone:  {:58s}   |
 |Email:        {:58s}   |
 |Location:     {:58s}   |
 |Company role: {:58s}   |
 |Password:     {:58s}   |                                                                        
 -----------------------------------------------------------------------------'''.format(name, ssn, address, home_phone, smart_phone, email, location, role, password))

        add_choice = input(" | Do you want to save and continue? (Y / N): ").lower()
        if add_choice == "y":
            self.logic.employee(2, None, None, the_employee)
            self.logic.roles(1, None, employee_roles)
            print('''\n ------------------------------------------------------------------------------
 | -> -> Manage employee -> Add employee                                      |
 ------------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                The following employee has been added:                      |
 |                {:60s}|
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(name))
            input(" | Push 'Enter' to continue")
            if len(name) > 12:
                self.logic.employeelogic.change_employee_name(ssn, name)
                
        elif add_choice == "n":
            print('''\n -----------------------------------------------------------------------------
 | -> -> Manage employee -> Add employee                                      |
 ------------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                The following employee has not been added:                  |
 |                {:60s}|
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(name))
            input(" | Press 'Enter' to continue")
        else:
            return None

    def remove_employee(self):
        '''Takes employee name input from user, and compares it to list of all employee. If name 
        exists it will delete if the user wishes to do so'''
        while True:
            find_employee = input(" | Enter employee SSN: ")
            result = self.logic.employee(0, find_employee, "ssn", None)
            if result == []:           
                print(" | Employee with SSN: '{}' does not exist".format(find_employee))
                continue
               
            choice = input(" | Are you sure you want to remove '{}' ? (Y / N): ".format(find_employee)).lower()
            if choice == "y":
                self.logic.employee(1, find_employee, None, None)
                self.logic.roles(2, find_employee, "ssn")
                print('''\n ------------------------------------------------------------------------------
 | -> -> Manage employee -> Remove employee                                   |
 ------------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                The following employee has been removed:                    |
 |                {:60s}|
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(find_employee))
                input(" | Press 'Enter' to continue")
                break
            elif choice == "n":
                print('''\n ------------------------------------------------------------------------------
 | -> -> Manage employee -> Remove employee                                   |
 ------------------------------------------------------------------------------
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                The following employee has not been removed:                |
 |                {:60s}|
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 |                                                                            |
 ------------------------------------------------------------------------------'''.format(find_employee))
                input(" | Press 'Enter' to continue")
                return
            else:
                return None

    def update_employee(self):
        ''' User can choose a field within the employee class and change the information '''
        while True:
            find_employee = input(" | Enter employee SSN: ")
            while self.logic.input_checking(1, find_employee) == False:
                print(" | SSN must be in the correct format: '123456-1234' ")
                find_employee = input(" | SSN: ")
            the_employee = self.logic.employee(0, find_employee, "ssn", None)
            attribute = input('''\n -----------------------------------------------------------------------------
 | -> -> Manage employee -> Update employee                                  |
 -----------------------------------------------------------------------------
 | "Select attribute you would like to change"                               |
 |                                                                           |
 | 1. Address:           {:52s}|
 | 2. Home phone:        {:52s}|
 | 3. Smart phone:       {:52s}|
 | 4. Email:             {:52s}|
 | 5. Location:          {:52s}|
 | 6. Company role:      {:52s}|
 | 7. Password:          {:52s}|                                                                         
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice: '''.format(the_employee[0].address, the_employee[0].home_phone, the_employee[0].gsm_phone, the_employee[0].email, the_employee[0].location, the_employee[0].role, the_employee[0].password))
            new_employee_info = "0"
            if attribute == "1":
                attribute = "address"
                new_employee_info = input(" | Enter new information: ")

            elif attribute == "2":
                attribute = "home_phone"
                new_employee_info = input(" | Enter new information: ")
                while self.logic.input_checking(2, new_employee_info) == False:
                    print(" | Home phone must be in the correct format: '1234567' ")

            elif attribute == "3":
                attribute = "gsm_phone"
                new_employee_info = input(" | Enter new information: ")
                while self.logic.input_checking(2, new_employee_info) == False:
                    print(" | Home phone must be in the correct format: '1234567' ")

            elif attribute == "4":
                attribute = "email"
                new_employee_info = input(" | Enter new information: ")
                while self.logic.input_checking(0, new_employee_info) == False:
                    print(" | Email must be in the correct format: 'name@name.is' ")

            elif attribute == "5":
                attribute = "location"
                new_employee_info = input(" | Enter new information: ").capitalize()
                while self.logic.input_checking(12, new_employee_info) == False:
                    print(" | Location {} does not exist!".format(new_employee_info))
                    new_employee_info = input(" | Enter new information: ").capitalize()
            elif attribute == "6":
                attribute = "role"            
                new_employee_info = input(" | Enter new information: ").capitalize()
                while self.logic.input_checking(3, new_employee_info) == False:
                    print(" | company role is either 'Ceo', 'Fleet' or 'Base'!")
                    new_employee_info = input(" | Company role: ").capitalize()
                    
            elif attribute == "7":
                attribute = "password"  
                new_employee_info = input(" | Enter new information: ")

            else:
                print(" | Wrong input")
                continue

            
            updated_employee = self.logic.employee(3, find_employee, attribute,  new_employee_info)
            print('''\n -----------------------------------------------------------------------------
 | -> -> Manage employee -> Update employee                                  |
 -----------------------------------------------------------------------------
 | "Updated employee information"                                            |
 |                                                                           |
 | 1. Address:             {:50s}|
 | 2. Home phone:          {:50s}|
 | 3. Smart phone:         {:50s}|
 | 4. Email:               {:50s}|
 | 5. Location:            {:50s}|
 | 6. Company role:        {:50s}|
 | 7. Password:            {:50s}|                                                          
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------'''.format(updated_employee.address, updated_employee.home_phone, updated_employee.gsm_phone, updated_employee.email, updated_employee.location, updated_employee.role, updated_employee.password))
            input(" | Press 'Enter' to continue")
            break

    def get_all_employees(self):
        '''List all employess in appropriate columns based on their attributes below'''
        results = self.logic.employee(0, None, None, None)
<<<<<<< HEAD
        print("""\n ------------------------------------------------------------------------------------------------------------------------------------------------
 | -> -> Manage employee -> All Employees                                                                                                       |
 ------------------------------------------------------------------------------------------------------------------------------------------------
 |  Name:              | SSN:        | Address:      | Home number: | Cell number: | Email:             | Location:  | Role:     | Password:    |""")
        print(" ------------------------------------------------------------------------------------------------------------------------------------------------")
        
        for employee in results:
            print(''' |  {}  |'''.format(str(employee)))
        print(" ------------------------------------------------------------------------------------------------------------------------------------------------")
=======
<<<<<<< HEAD
        print("""\n ------------------------------------------------------------------------------------------------------------------------------------------
 | -> -> Manage employee -> All Employees                                                                                                     |
 ---------------------------------------------------------------------------------------------------------------------------------------------
 |  Name:              | SSN:        | Address:      | Home number: | Cell number: | Email:             | Location:  | Role:     | Password:  |""")
        print(" ----------------------------------------------------------------------------------------------------------------------------------------------")
        
        for employee in results:
            print(''' |  {}  |'''.format(str(employee)))
        print(" ----------------------------------------------------------------------------------------------------------------------------------------------")
=======
        print("""\n ----------------------------------------------------------------------------------------------------------------------------------------------
 | -> -> Manage employee -> All Employees                                                                                                     |
 ----------------------------------------------------------------------------------------------------------------------------------------------
 |  Name:              | SSN:        | Address:      | Home number: | Cell number: | Email:             | Location:  | Role:     | Password:  |""")
        print(" ---------------------------------------------------------------------------------------------------------------------------------------------")
        
        for employee in results:
            print(''' |  {}  |'''.format(str(employee)))
        print(" ---------------------------------------------------------------------------------------------------------------------------------------------")
>>>>>>> a289c1aa38d6bc1e42219b972e6201b2dd2a0c4a
>>>>>>> b7fa3317f4fb83a6cc5a5d63523c18e2aea22adc
        input(" | Press 'Enter' to continue")

    def search_employee(self):
        ''' Takes input from user and find the employee associated with that input and prints out the employees information '''
        employee = input(" | Enter employee SSN: ")

        while self.logic.input_checking(1, employee) == False:
            print(" | SSN must be in the correct format: '123456-1234' ")
            employee = input(" | Enter employee SSN: ")
        result = self.logic.employee(0, employee, "ssn", None)
        if result == []:
            print(" | Employee with SSN: '{}' does not exist".format(employee))
            employee = input(" | Enter employee SSN: ")

        result = self.logic.employee(0, employee, "ssn", None)
        print("""\n -----------------------------------------------------------------------------
 | -> -> Manage employee -> Search Employee                                  |
 -----------------------------------------------------------------------------""")
        for emp in result:
            print(''' | 'Employee information'                                                    |
 |                                                                           |
 | Name:          {:54s}     |
 | SNN:           {:54s}     |
 | Address:       {:54s}     |
 | Home number:   {:54s}     |
 | Cell number:   {:54s}     |
 | Email:         {:54s}     |
 | Location:      {:54s}     |
 | Company role:  {:54s}     |
 | Password:      {:54s}     |                     
 |                                                                           |
 ----------------------------------------------------------------------------- '''.format(emp.name, emp.ssn, emp.address, emp.home_phone, emp.gsm_phone, emp.email, emp.location, emp.role, emp.password))
        input(" | Press 'Enter' to continue")