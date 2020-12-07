from Logic.EmployeeLogic import EmployeeLogic
from Logic.LocationLogic import LocationLogic
from Logic.VehicleLogic import VehicleLogic
from Logic.ContractLogic import ContractLogic
from Logic.CustomerLogic import CustomerLogic

class LogicMain:
    def __init__(self):
        self.employeelogic = EmployeeLogic()
        self.locationlogic = LocationLogic()
        self.vehiclelogic = VehicleLogic()
        self.contractlogic = ContractLogic()
        self.customerlogic = CustomerLogic()

    def employee(self, option, filter_or_id, attribute, new_information):
        if option == 0:
            results = self.employeelogic.filteremployees(filter_or_id, attribute)
        elif option == 1:
            results = self.employeelogic.removeemployee(filter_or_id)
        elif option == 2:
            results = self.employeelogic.addemployee(new_information)
        else:
            results = self.employeelogic.editemployeeinfo(filter_or_id, attribute, new_information)

        return results

    def location(self, option, filter_or_id, attribute, new_information):
        if option == 0:
            results = self.locationlogic.filtercountry(filter_or_id, attribute)
        elif option == 1:
            results = self.locationlogic.addlocation(new_information)
        elif option == 2:
            results = self.locationlogic.removelocation(filter_or_id)
        else:
            results = self.locationlogic.editlocationinfo(filter_or_id, attribute, new_information)

        return results

    def vehicle(self, option, filter_id_number_plate_or_vehicle_type, attribute_or_current_rate, new_vehicle_or_rate):
        if option == 0:
            results = self.vehiclelogic.filtervehiclefleet(filter_id_number_plate_or_vehicle_type, attribute_or_current_rate)
        elif option == 1:
            results = self.vehiclelogic.editvehicleinfo(filter_id_number_plate_or_vehicle_type, attribute_or_current_rate, new_vehicle_or_rate)
        elif option == 2:
            results = self.vehiclelogic.registernewvehicle(new_vehicle_or_rate)
        elif option == 3:
            results = self.vehiclelogic.remove_vehicle(filter_id_number_plate_or_vehicle_type)
        else:
            results = self.vehiclelogic.editrate(filter_id_number_plate_or_vehicle_type, new_vehicle_or_rate, attribute_or_current_rate)

        return results

    def contract(self, option, filter_or_id, attribute, new_information, vehicle_type):
        if option == 0:
            results = self.contractlogic.filtercontract(filter_or_id, attribute)
        elif option == 1:
            self.vehiclelogic.editvehicleinfo(vehicle_type[0].number_plate, "status", "rented")
            results = self.contractlogic.makenewcontract(new_information)
        elif option == 2:
            results = self.contractlogic.editcontractinfo(filter_or_id, attribute, new_information)
        elif option == 3:
            results = self.contractlogic.cancelcontract(filter_or_id)
        elif option == 4:
            vehicle_class = self.vehicle(0, attribute, "number_plate", None)
            results = self.contractlogic.checklicense(filter_or_id, vehicle_class)
        elif option == 5:
            new_vehicle = self.vehiclelogic.filtervehiclefleet(new_information, attribute)
            if new_vehicle[0].status == "available":
                self.vehiclelogic.editvehicleinfo(filter_or_id, "status", "available")
                the_vehicle = self.vehiclelogic.editvehicleinfo(new_information, "status", "rented")
                results = self.contractlogic.editcontractinfo(filter_or_id, attribute, new_information)
                total_price = self.contractlogic.calculatefinalprice(results.duration, the_vehicle)
                results = self.contractlogic.editcontractinfo(filter_or_id, "final_price", total_price)
            else:
                return False

        else:
            results = self.contractlogic.calculatefinalprice(filter_or_id, vehicle_type)

        return results

    def customer(self, option, ssn_or_customer_class, attribute, new_information):
        if option == 0:
            results = self.customerlogic.get_list_of_customers(ssn_or_customer_class, attribute)
        elif option == 1:
            results = self.customerlogic.add_customer_to_the_system(ssn_or_customer_class)
        elif option == 2:
            results = self.customerlogic.remove_customer(ssn_or_customer_class)
        else:
            results = self.customerlogic.edit_customer(ssn_or_customer_class, attribute, new_information)

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
            pass
        else: #Number plate
            pass

        return False
