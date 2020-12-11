from Logic.EmployeeLogic import EmployeeLogic
from Logic.LocationLogic import LocationLogic
from Logic.VehicleLogic import VehicleLogic
from Logic.ContractLogic import ContractLogic
from Logic.CustomerLogic import CustomerLogic
from Logic.EmployeeLogic import RoleLogic
from Logic.ReportLogic import ReportLogic

class LogicMain:
    def __init__(self):
        self.employeelogic = EmployeeLogic()
        self.locationlogic = LocationLogic()
        self.vehiclelogic = VehicleLogic()
        self.contractlogic = ContractLogic()
        self.customerlogic = CustomerLogic()
        self.reportlogic = ReportLogic()
        self.rolelogic = RoleLogic()

    def employee(self, option, filter_or_id, attribute, new_information):
        if option == 0: # Option 0 gives back list of employees with a filter, if it gets None in filter it returns list of all employees.
            results = self.employeelogic.filter_employees(filter_or_id, attribute)

        elif option == 1: # Option 1 takes in employee ssn, removes that employee from the system and returns nothing.
            results = self.employeelogic.remove_employee(filter_or_id)

        elif option == 2: # Option 2 takes in employee class, tells data to save that employee and returns nothing.
            results = self.employeelogic.add_employee(new_information)

        else: # Else takes in the employees ssn, the attribute to edit and the new value for that attribute. Then it changes that employee and returns the updated employee class.
            results = self.employeelogic.edit_employee_info(filter_or_id, attribute, new_information)

        return results

    def location(self, option, filter_or_id, attribute, new_information):
        if option == 0: # Option 0 takes in filter and the attribute name for the filter. Then it gives back list of all locations with that filter.
            results = self.locationlogic.filter_country(filter_or_id, attribute)

        elif option == 1: # Option 1 takes in location class, tells data to save that location and returns nothing.
            results = self.locationlogic.add_location(new_information)

        elif option == 2: # Option 2 takes in airport name, removes that location from the system and returns nothing.
            results = self.locationlogic.remove_location(filter_or_id)

        else: # Else takes in the airport name, the attribute to edit and the new value for that attribute. Then it changes that location and returns the updated location class.
            results = self.locationlogic.edit_location_info(filter_or_id, attribute, new_information)

        return results

    def vehicle(self, option, filter_id_number_plate_or_vehicle_type, attribute_or_current_rate, new_vehicle_or_rate):
        if option == 0: # Option 0 takes in filter and the attribute name for the filter. Then it gives back list of all vehicles with that filter.
            results = self.vehiclelogic.filter_vehicle_fleet(filter_id_number_plate_or_vehicle_type, attribute_or_current_rate)

        elif option == 1: # Option 1 takes in the number plate, the attribute to edit and the new value for that attribute. Then it changes that location and returns the updated vehicle class.
            results = self.vehiclelogic.edit_vehicle_info(filter_id_number_plate_or_vehicle_type, attribute_or_current_rate, new_vehicle_or_rate)

        elif option == 2: # Option 2 takes in vehicle class, tells data to save that vehicle and returns nothing.
            results = self.vehiclelogic.register_new_vehicle(new_vehicle_or_rate)

        elif option == 3: # Option 3 takes in number plate, removes that vehicle from the system and returns nothing.
            results = self.vehiclelogic.remove_vehicle(filter_id_number_plate_or_vehicle_type)

        else: # Else takes in the vehicle type, current rate and the new rate. Then it gets a list of all these vehicle types and updates the rate for all of them.
            results = self.vehiclelogic.edit_rate(filter_id_number_plate_or_vehicle_type, attribute_or_current_rate, new_vehicle_or_rate)

        return results

    def contract(self, option, filter_or_id, attribute, new_information, vehicle_type):
        if option == 0: # Option 0 takes in filter and the attribute name for the filter. Then it gives back list of all contracts with that filter.
            results = self.contractlogic.filter_contract(filter_or_id, attribute)

        elif option == 1: # Option 1 takes in contract class, tells data to save that contract and returns nothing.
            results = self.contractlogic.make_new_contract(new_information)

        elif option == 2: # Option 2 takes in the customers ssn, the attribute to edit and the new value for that attribute. Then it changes that contract and returns the updated contract class.
            results = self.contractlogic.edit_contract_info(filter_or_id, attribute, new_information)

        elif option == 3: # Option 3 takes in customers ssn, removes that contract from the system and returns the removed contract.
            results = self.contractlogic.cancel_contract(filter_or_id)

        elif option == 4: # Option 4 takes in customer class and a number plate. Then it compares the license on both things and either returns the vehicle class or empty list.
            results = self.contractlogic.check_license(filter_or_id, attribute)

        elif option == 5: # Option 5 takes in the contract class, "number_plate" and the number plate of the new vehicle. 
            # Then it changes everything that has to change and returns the updated contract or false if the new vehicle is occupied.
            results = self.contractlogic.change_vehicle(filter_or_id, attribute, new_information)

        elif option == 6: # Option 6 takes in the customers ssn and the condition. Then it updates everything that needs to be updated and returns new calculated price.
            results = self.contractlogic.charge_contract(filter_or_id, attribute)

        elif option == 7: # Option 7 takes in the duration and vehicle class. Then it calculates the final price and returns it.
            results = self.contractlogic.calculate_final_price(filter_or_id, vehicle_type)

        else: # Else takes in value and attribute of either pickup date or return date and the new value. Then it changes the date, duration and final price and returns the updated contract.
            results = self.contractlogic.edit_contract_date(filter_or_id, attribute, new_information)

        return results

    def customer(self, option, ssn_or_customer_class, attribute, new_information):
        if option == 0: # Option 0 takes in filter and the attribute name for the filter. Then it gives back list of all customers with that filter.
            results = self.customerlogic.get_list_of_customers(ssn_or_customer_class, attribute)

        elif option == 1: # Option 1 takes in customer class, tells data to save that customer and returns nothing.
            results = self.customerlogic.add_customer_to_the_system(ssn_or_customer_class)

        elif option == 2: # Option 2 takes in customers ssn, removes that customer from the system and returns the removed customer.
            results = self.customerlogic.remove_customer(ssn_or_customer_class)

        else: # Else takes in the customers ssn, the attribute to edit and the new value for that attribute. Then it changes that customer and returns the updated customer class.
            results = self.customerlogic.edit_customer(ssn_or_customer_class, attribute, new_information)

        return results
    
    def roles(self, option, emp_ssn, emp_object):
        '''logic for association between employees and roles'''
        if option == 0: # if a function wants to use only attributes from roles
            results = self.rolelogic.role_list(emp_ssn, emp_object)
        elif option == 1:
            results = self.rolelogic.add_employee(emp_object) # when new emp is added with logic.employee()
        elif option == 2:
            results = self.rolelogic.remove_employee(emp_ssn, emp_object) # when emp is removed or updated with logic.employee()
        return results
            
            

    def reports(self, option, start_date, end_date):
        if option == 0: # Returns list of the most used type of vehicle for every location
            results = self.reportlogic.most_popular_type_by_location()

        elif option == 1: # Returns overview of income over a certain period
            total, location_dict, type_dict = self.reportlogic.overview_of_income(start_date, end_date)
            return total, location_dict, type_dict

        elif option == 2:  # Returns list of all types of vehicle and how many days they have been driven for all locations
            results = self.reportlogic.type_usage_by_location()

        else: # Returns a list of all contracts over a period and shows if they are paid or not
            results = self.reportlogic.overview_of_payment_status(start_date, end_date)

        return results

    def input_checking(self, option, user_input):
        if option == 0: #Email checking *****@**.***
            if ("@" in user_input) and ("." in user_input):
                return True       

        elif option == 1: #SSN checking ******-****
            if len(user_input) == 11 and user_input[6] == "-":
                for char in user_input:
                    if char.isalpha():
                        return False
                return True

        elif option == 2: #Phone checking 
            if len(user_input) == 7 and user_input.isdigit():
                return True

        elif option == 3: #Company role checking
            if user_input == "Ceo" or user_input == "Fleet" or user_input == "Base":
                return True

        elif option == 4: #Driving license checking
            if len(user_input) < 4 and ("a" in user_input) or ("b" in user_input) or ("c" in user_input):
                return True

        elif option == 5: #Yes or no checking
            if user_input == "yes" or user_input == "no":
                return True

        elif option == 6: #Date checking **/**/****
            if len(user_input) != 10:
                return False
                
            seperator_list = [2, 5]
            for pos in seperator_list:
                if user_input[pos] != "/":
                    return False
                
            for idx, char in enumerate(user_input):
                if not (char.isdigit() or idx in seperator_list):
                    return False

            return True

        elif option == 7: #Numbers checking
            if user_input.isnumeric():
                return True

        elif option == 8: # Model year checking
            if user_input.isnumeric() and len(user_input) == 4:
                return True

        elif option == 9: #Opening hours checking **:**-**:**
            if len(user_input) != 11:
                return False

            seperator_list = [2, 5, 8]
            for pos in seperator_list:
                if user_input[pos] != ":" and user_input[pos] != "-":
                    return False
                
            for idx, char in enumerate(user_input):
                if not (char.isdigit() or idx in seperator_list):
                    return False

            return True

        elif option == 10: #Letters checking
            if user_input.isalpha():
                return True

        elif option == 11: #Number plate checking ** ***
            if len(user_input) == 6:
                first_part = user_input[0:2]
                secondpart = user_input[5:]
                checker = 0
                if not [] == self.vehicle(0, user_input, "number_plate", None): #empty list if plate doesn´t exist
                    checker += 1
                if user_input[2] == " " and first_part.isalpha() and secondpart.isdigit():
                    checker += 1
                if checker == 2:
                    return True  
                
        elif option == 12: # For checking if the location exists in the system
            location = self.location(0, user_input, "name_of_airport", None)
            if location == []:
                return False
            if location != []:
                return True
              
        elif option == 13: #number plate in add vehicle
            if len(user_input) == 6:
                first_part = user_input[0:2]
                secondpart = user_input[5:]
                if user_input[2] == " " and first_part.isalpha() and secondpart.isdigit():
                    v_list = self.vehicle(0, user_input, "number_plate", None)
                    if v_list != []: # if list isn´t empty then a vehicle with n_plate was found
                        print(" | Number plate already exists!")
                        return False
                    return True    
                else:
                    print(" | Number plate has to be two letters and three numbers: 'AA 123'")
            else:
                print(" | Number plate has to be two letters and three numbers: 'AA 123'")            

        elif option == 14: #username
            if self.employee(0, user_input, "ssn", None) == []: 
                return False
            return True
        
        elif option == 16: #username
            if self.roles(0, user_input, "ssn") == []: 
                return False
            return True
        
        elif option == 15: #password
            if self.employee(0, user_input, "password", None) == []:
                return False
            return True

        return False