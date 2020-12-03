from Logic.EmployeeLogic import EmployeeLogic
from Logic.LocationLogic import LocationLogic
from Logic.VehicleLogic import VehicleLogic
from Logic.ContractLogic import ContractLogic

class LogicMain:
    def __init__(self):
        self.employeelogic = EmployeeLogic()
        self.locationlogic = LocationLogic()
        self.vehiclelogic = VehicleLogic()
        self.contractlogic = ContractLogic()

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
            results = self.contractlogic.makenewcontract(new_information)
        elif option == 2:
            results = self.contractlogic.editcontractinfo(filter_or_id, attribute, new_information)
        elif option == 3:
            results = self.contractlogic.cancelcontract(filter_or_id)
        elif option == 4:
            results = self.contractlogic.printcontract(filter_or_id)
        else:
            list_of_vehicles_by_rate = self.vehiclelogicfilter(vehicle_type)
            results = self.contractlogic.calculatefinalprice(filter_or_id, list_of_vehicles_by_rate)

        return results