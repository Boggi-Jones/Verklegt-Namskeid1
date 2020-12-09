from Logic.EmployeeLogic import EmployeeLogic
from Logic.LocationLogic import LocationLogic
from Logic.VehicleLogic import VehicleLogic
from Logic.CustomerLogic import CustomerLogic
from Logic.ContractLogic import ContractLogic
from datetime import datetime

class ReportLogic:
    def __init__(self):
        self.locationlogic = LocationLogic()
        self.vehiclelogic = VehicleLogic()
        self.customerlogic = CustomerLogic()
        self.contractlogic = ContractLogic()

    def most_popular_type_by_location(self):
        list_of_all_vehicles = self.vehiclelogic.filtervehiclefleet(None, None)
        list_of_all_locations = self.locationlogic.filtercountry(None, None)
        return_list = []
        for location in list_of_all_locations:
            list_of_all_vehicle_by_location = []
            for vehicle in list_of_all_vehicles:
                if vehicle.name_of_airport == location.name_of_airport:
                    list_of_all_vehicle_by_location.append(vehicle)
            
            new_dict = {}
            for vehicle in list_of_all_vehicle_by_location:
                if vehicle.vehicle_type in new_dict:
                    new_dict[vehicle.vehicle_type] += int(vehicle.rent_counter)
                else:
                    new_dict[vehicle.vehicle_type] = int(vehicle.rent_counter)

            rent_count = 0
            most_used = ""
            for vehicle_type, rent_time in new_dict.items():
                if rent_time > rent_count:
                    rent_count = rent_time
                    most_used = vehicle_type

            most_popular = [location.name_of_airport, most_used, rent_count]
            return_list.append(most_popular)

        return return_list

    def overview_of_income(self, start_date, end_date):
        list_of_contracts = self.contractlogic.filter_contract("yes", "paid")
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
        total = 0
        location_dict = {}
        type_dict = {}
        for contract in list_of_contracts:
            pay_date = datetime.strptime(contract.return_date, "%d/%m/%Y")
            if pay_date >= start_date and pay_date <= end_date:
                total += int(contract.final_price)

                if contract.name_of_airport in location_dict:
                    location_dict[contract.name_of_airport] += int(contract.final_price)
                else:
                    location_dict[contract.name_of_airport] = int(contract.final_price)
                the_vehicle = self.vehiclelogic.filtervehiclefleet(contract.number_plate, "number_plate")
               
                if the_vehicle[0].vehicle_type in type_dict:
                    type_dict[the_vehicle[0].vehicle_type] += int(contract.final_price)
                else:
                    type_dict[the_vehicle[0].vehicle_type] = int(contract.final_price)

        return total, location_dict, type_dict

    def type_usage_by_location(self):
        list_all_vehicle = self.vehiclelogic.filtervehiclefleet(None, None)
        list_of_all_locations = self.locationlogic.filtercountry(None, None)
        return_list = []
        for location in list_of_all_locations:
            list_of_all_vehicle_by_location = []
            for vehicle in list_all_vehicle:
                if vehicle.name_of_airport == location.name_of_airport:
                    list_of_all_vehicle_by_location.append(vehicle)
            
            new_dict = {}
            for vehicle in list_of_all_vehicle_by_location:
                if vehicle.vehicle_type in new_dict:
                    new_dict[vehicle.vehicle_type] += int(vehicle.rent_counter)
                else:
                    new_dict[vehicle.vehicle_type] = int(vehicle.rent_counter)

            new_list = [location, new_dict]
            return_list.append(new_list)

        return return_list

    def overview_of_payment_status(self, start_date, end_date):
        list_of_contracts = self.contractlogic.filter_contract(None, None)
        start_date = datetime(start_date, "%d/%m/%Y")
        end_date = datetime(end_date, "%d/%m/%Y")
        new_dict = {}
        for contract in list_of_contracts:
            pay_date = datetime.strptime(contract.return_date, "%d/%m/%Y")
            if pay_date >= start_date and pay_date <= end_date:
                the_customer = self.customerlogic.get_list_of_customers(contract.ssn, "ssn")
                new_dict[the_customer.name] = contract.paid

        return new_dict