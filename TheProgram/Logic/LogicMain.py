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
        if option == 0: # Option 0 is used to filter employees
            results = self.employeelogic.filteremployees(filter_or_id, attribute)
        elif option == 1: # Option 1 is used to remove employee
            results = self.employeelogic.removeemployee(filter_or_id)
        elif option == 2: # Option 2 is used to add employee
            results = self.employeelogic.addemployee(new_information)
        else: # Else is used for edit employee infi
            results = self.employeelogic.editemployeeinfo(filter_or_id, attribute, new_information)

        return results

    def location(self, option, filter_or_id, attribute, new_information):
        if option == 0: # Option 0 is used to filter country
            results = self.locationlogic.filtercountry(filter_or_id, attribute)
        elif option == 1: # Option 1 is used to add location
            results = self.locationlogic.addlocation(new_information)
        elif option == 2: # Option 2 is used to remove location
            results = self.locationlogic.removelocation(filter_or_id)
        else: # Else is used to edit location info
            results = self.locationlogic.editlocationinfo(filter_or_id, attribute, new_information)

        return results

    def vehicle(self, option, filter_id_number_plate_or_vehicle_type, attribute_or_current_rate, new_vehicle_or_rate):
        if option == 0: # Option 0 is used to filter vehicle fleet
            results = self.vehiclelogic.filtervehiclefleet(filter_id_number_plate_or_vehicle_type, attribute_or_current_rate)
        elif option == 1: # Option 1 is used to edit vehjicle info
            results = self.vehiclelogic.editvehicleinfo(filter_id_number_plate_or_vehicle_type, attribute_or_current_rate, new_vehicle_or_rate)
        elif option == 2: # Option 2 is used to register new vehicle
            results = self.vehiclelogic.registernewvehicle(new_vehicle_or_rate)
        elif option == 3: # Option 3 is used to remove vehicle
            results = self.vehiclelogic.remove_vehicle(filter_id_number_plate_or_vehicle_type)
        else: # Else is used to edit vehicle rate
            results = self.vehiclelogic.editrate(filter_id_number_plate_or_vehicle_type, new_vehicle_or_rate, attribute_or_current_rate)

        return results

    def contract(self, option, filter_or_id, attribute, new_information, vehicle_type):
        if option == 0: # Option 0 is used to filter contract
            results = self.contractlogic.filtercontract(filter_or_id, attribute)
        elif option == 1: # Option 1 is used to make new contract
            results = self.contractlogic.makenewcontract(new_information)
        elif option == 2: # Option 2 is used to edit contract information
            results = self.contractlogic.editcontractinfo(filter_or_id, attribute, new_information)
        elif option == 3: # Option 3 is used to cancel contract 
            results = self.contractlogic.cancelcontract(filter_or_id)
        elif option == 4: # Option 4 is used to check if customer has valid licence for type for vehicle
            vehicle_class = self.vehicle(0, attribute, "number_plate", None)
            results = self.contractlogic.checklicense(filter_or_id, vehicle_class)
        elif option == 5: # Option 5 used to check if the status on vehicle is rented or available
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
        if option == 0: # Option 0 is used to get list of customers
            results = self.customerlogic.get_list_of_customers(ssn_or_customer_class, attribute)
        elif option == 1: # Option 1 is used to add customers to the system
            results = self.customerlogic.add_customer_to_the_system(ssn_or_customer_class)
        elif option == 2: # Option 2 is used to remove customers from system
            results = self.customerlogic.remove_customer(ssn_or_customer_class)
        else: # Else is used to edit customers information
            results = self.customerlogic.edit_customer(ssn_or_customer_class, attribute, new_information)

        return results
