from Logic.EmployeeLogic import EmployeeLogic
from Logic.LocationLogic import LocationLogic
from Logic.VehicleLogic import VehicleLogic
from Logic.ContractLogic import ContractLogic
from Logic.CustomerLogic import CustomerLogic
from Logic.ReportLogic import ReportLogic

class LogicMain:
    def __init__(self):
        self.employeelogic = EmployeeLogic()
        self.locationlogic = LocationLogic()
        self.vehiclelogic = VehicleLogic()
        self.contractlogic = ContractLogic()
        self.customerlogic = CustomerLogic()
        self.reportlogic = ReportLogic()

    def employee(self, option, filter_or_id, attribute, new_information):
        if option == 0: # Option 0 is used to filter employees
            results = self.employeelogic.filter_employees(filter_or_id, attribute)

        elif option == 1: # Option 1 is used to remove employee
            results = self.employeelogic.remove_employee(filter_or_id)

        elif option == 2: # Option 2 is used to add employee
            results = self.employeelogic.add_employee(new_information)

        else: # Else is used for edit employee infi
            results = self.employeelogic.edit_employee_info(filter_or_id, attribute, new_information)

        return results

    def location(self, option, filter_or_id, attribute, new_information):
        if option == 0: # Option 0 is used to filter country
            results = self.locationlogic.filter_country(filter_or_id, attribute)

        elif option == 1: # Option 1 is used to add location
            results = self.locationlogic.add_location(new_information)

        elif option == 2: # Option 2 is used to remove location
            results = self.locationlogic.remove_location(filter_or_id)

        else: # Else is used to edit location info
            results = self.locationlogic.edit_location_info(filter_or_id, attribute, new_information)

        return results

    def vehicle(self, option, filter_id_number_plate_or_vehicle_type, attribute_or_current_rate, new_vehicle_or_rate):
        if option == 0: # Option 0 is used to filter vehicle fleet
            results = self.vehiclelogic.filter_vehicle_fleet(filter_id_number_plate_or_vehicle_type, attribute_or_current_rate)

        elif option == 1: # Option 1 is used to edit vehjicle info
            results = self.vehiclelogic.edit_vehicle_info(filter_id_number_plate_or_vehicle_type, attribute_or_current_rate, new_vehicle_or_rate)

        elif option == 2: # Option 2 is used to register new vehicle
            results = self.vehiclelogic.register_new_vehicle(new_vehicle_or_rate)

        elif option == 3: # Option 3 is used to remove vehicle
            results = self.vehiclelogic.remove_vehicle(filter_id_number_plate_or_vehicle_type)

        else: # Else is used to edit vehicle rate
            results = self.vehiclelogic.edit_rate(filter_id_number_plate_or_vehicle_type, new_vehicle_or_rate, attribute_or_current_rate)

        return results

    def contract(self, option, filter_or_id, attribute, new_information, vehicle_type):
        if option == 0: # Option 0 is used to filter contract
            results = self.contractlogic.filter_contract(filter_or_id, attribute)

        elif option == 1: # Option 1 is used to make new contract
            results = self.contractlogic.make_new_contract(new_information)

        elif option == 2: # Option 2 is used to edit contract information
            results = self.contractlogic.edit_contract_info(filter_or_id, attribute, new_information)

        elif option == 3: # Option 3 is used to cancel contract 
            results = self.contractlogic.cancel_contract(filter_or_id)

        elif option == 4: # Option 4 is used to check if customer has valid licence for type for vehicle
            results = self.contractlogic.check_license(filter_or_id, attribute)

        elif option == 5: # Option 5 used to switch vehicle on a contract
            results = self.contractlogic.change_vehicle(filter_or_id, attribute, new_information)

        elif option == 6: # Option 6 is used to charge the contract
            results = self.contractlogic.charge_contract(filter_or_id, attribute)

        elif option == 7:
            results = self.contractlogic.calculate_final_price(filter_or_id, vehicle_type)

        else:
            results = self.contractlogic.edit_contract_date(filter_or_id, attribute, new_information)

        return results

    def customer(self, option, ssn_or_customer_class, attribute, new_information):
        if option == 0: # Option 0 is used to get list of customers
            results = self.customerlogic.get_list_of_customers(ssn_or_customer_class, attribute)

        elif option == 1: # Option 1 is used to add customers to the system
            results = self.customerlogic.add_customer_to_the_system(ssn_or_customer_class)

        elif option == 2: # Option 2 is used to remove customers from system
            results = self.customerlogic.remove_customer(ssn_or_customer_class)

        else: # Else is used to edit customers information
            results = self.customerlogic.edit_customer(ssn_or_customer_class, attribute, new_information)

        return results

    def reports(self, option, start_date, end_date):
        if option == 0:
            results = self.reportlogic.most_popular_by_location()

        elif option == 1:
            total, location_dict, type_dict = self.reportlogic.overview_of_income(start_date, end_date)
            return total, location_dict, type_dict

        elif option == 2:
            results = self.reportlogic.type_usage_by_location()

        else:
            results = self.reportlogic.overview_of_payment_status(start_date, end_date)

        return results

    def input_checking(self, option, user_input):
        if option == 0: #Email checking
            if ("@" in user_input) and ("." in user_input):
                return True       

        elif option == 1: #SSN checking
            if len(user_input) == 11 and user_input[6] == "-":
                for char in user_input:
                    if char.isalpha():
                        return False
                return True

        elif option == 2: #Phone checking
            if len(user_input) == 7 and user_input.isdigit():
                return True

        elif option == 3: #Company role
            if user_input == "ceo" or user_input == "fleet" or user_input == "base":
                return True

        elif option == 4: #Driving license
            if len(user_input) < 4 and ("a" in user_input) or ("b" in user_input) or ("c" in user_input):
                return True

        elif option == 5: #Yes or no
            if user_input == "yes" or user_input == "no":
                return True

        elif option == 6: #Date **/**/****
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

        elif option == 7: #Numbers
            if user_input.isnumeric():
                return True

        elif option == 8: # Model year
            if user_input.isnumeric() and len(user_input) == 4:
                return True

        elif option == 9: #Opening hours
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

        elif option == 10: #Letters
            if user_input.isalpha():
                return True

        elif option == 11: #Number plate
            if len(user_input) == 6:
                first_part = user_input[0:2]
                secondpart = user_input[5:]
                checker = 0
                
                #if user_input in self.vehicle(0, None, None, None):
                    #checker += 1
                if user_input[2] == " " and first_part.isalpha() and secondpart.isdigit():
                    checker = 2
                
                if checker == 2:
                    return True  
            
        elif option == 12: #check for location in the system
            location = self.location(0, user_input, "name_of_airport", None)
            if location == []:
                return False
            if location != []:
                return True
                
        return False