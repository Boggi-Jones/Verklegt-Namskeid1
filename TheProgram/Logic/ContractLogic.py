from Data.DataMain import DataMain
from Logic.EmployeeLogic import EmployeeLogic
from Logic.LocationLogic import LocationLogic
from Logic.VehicleLogic import VehicleLogic
from Logic.CustomerLogic import CustomerLogic
from datetime import datetime

class ContractLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Contract"
        self.locationlogic = LocationLogic()
        self.vehiclelogic = VehicleLogic()
        self.customerlogic = CustomerLogic()

    def filter_contract(self, filter_or_id, attribute):
        # Gets lists of contracts from datamain
        # If filter or id doesn´t match none, it get added to newly made retlist
        # Retlist is then returned
        # Else list of contract is returned 
        list_of_contracts = self.datamain.get_list(self.position)
        retlist = []
        if filter_or_id != None:
            for contract in list_of_contracts:
                if contract.__getattribute__(attribute) == filter_or_id:
                    retlist.append(contract)
            return retlist
        else:
            return list_of_contracts

    def cancel_contract(self, filter_or_id):
        # Gets list of contractts from filtercontract function
        # Contract is then iterated through list of contract searching for matching attribute
        # If contracts attribut(ssn) matches with filter or id, it´s deleted
        # List of contract is then overwritten with updated list
        list_of_contracts = self.filter_contract(None, None)
        for contract in list_of_contracts:
            if contract.ssn == filter_or_id:
                the_removed_contract = contract
                list_of_contracts.remove(contract)
                self.datamain.overwrite(self.position, list_of_contracts)
                return the_removed_contract

    def make_new_contract(self, new_information):
        # New contract is added to list
        self.datamain.add_to_list(self.position, new_information)
        self.vehiclelogic.edit_vehicle_info(new_information.number_plate, "status", "unavailable")

    def edit_contract_info(self, filter_or_id, attribute, new_information):
        # Single contract is created from the filtercontract function using the ssn attribute
        # Single contract is then updated with new information with cancel contract and make new contract funtions
        single_contract = self.filter_contract(filter_or_id, "ssn")
        the_contract = single_contract[0].__setattr__(attribute, new_information)
        self.cancel_contract(filter_or_id)
        self.make_new_contract(single_contract[0])
        return the_contract
        
    def check_license(self, customer_class, number_plate):
        # After user chooses vehicle
        # Driver license attribute is compared to vehicle driving license attribute
        # Vehicle class is then returned
        vehicle_class = self.vehiclelogic.filter_vehicle_fleet(number_plate, "number_plate")
        if customer_class.driving_license in vehicle_class[0].driving_license:
            return vehicle_class

    def change_vehicle(self, number_plate, attribute, new_information):
        new_vehicle = self.vehiclelogic.filter_vehicle_fleet(new_information, attribute)

        if new_vehicle[0].status == "available":
            self.vehiclelogic.edit_vehicle_info(number_plate, "status", "available")
            the_vehicle = self.vehiclelogic.edit_vehicle_info(new_information, "status", "unavailable")
            results = self.edit_contract_info(number_plate, attribute, new_information)
            total_price = self.calculate_final_price(results.duration, the_vehicle)
            results = self.edit_contract_info(number_plate, "final_price", total_price)
        else:
            return False

    def charge_contract(self, ssn, condition):
        current_date = datetime.today()
        the_contract = self.filter_contract(ssn, "ssn")
        if the_contract[0].paid == "no":
            return_date = datetime.strptime(the_contract[0].return_date + " 23:59", '%d/%m/%Y %H:%M')
            #self.editcontractinfo(ssn, "paid", "yes") setja upp á UI
            if condition == "good":
                self.vehiclelogic.edit_vehicle_info(the_contract[0].number_plate, "status", "available")
            else:
                self.vehiclelogic.edit_vehicle_info(the_contract[0].number_plate, "condition", "in repairs")
            
            duration = (current_date - datetime.strptime(the_contract[0].date,'%d/%m/%Y')).days
            the_vehicle = self.vehiclelogic.filter_vehicle_fleet(the_contract[0].number_plate, "number_plate")
            new_total = int(self.calculate_final_price(duration, the_vehicle))
            self.edit_contract_info(ssn, "return_date", datetime.strftime(current_date,'%d/%m/%Y'))
            self.edit_contract_info(ssn, "duration", duration)
            
            if current_date > return_date:    
                new_total = new_total * 1.2
                self.edit_contract_info(ssn, "final_price", new_total)
                self.customerlogic.edit_customer(ssn, "returned_late_before", "yes")
                return str(new_total)
            
            self.edit_contract_info(ssn, "final_price", new_total)
            return str(new_total)
        else:
            return None

    def calculate_final_price(self, duration, vehicle_class):
        # After user has chosen vehicle
        # Variable called rate is created using the rate attribute from vehicle function
        # Total price is than calculated by multiplying duration ( total days rented ) with rate
        # Final price is returned
        rate = vehicle_class[0].rate
        total = int(duration) * int(rate)
        return str(total)

    def edit_contract_date(self, filter_or_id, attribute, new_date):
        # Takes in either pickup date or return date 
        # Changes the duration, date and the total for that contract
        the_contract = self.filter_contract(filter_or_id, "ssn")
        the_vehicle = self.vehiclelogic.filter_vehicle_fleet(the_contract[0].number_plate, "number_plate")
        return_date = datetime.strptime(the_contract[0].return_date, '%d/%m/%Y')
        pickup_date = datetime.strptime(the_contract[0].date, '%d/%m/%Y')
        the_new_date = datetime.strptime(new_date, '%d/%m/%Y')
        
        if attribute == "date":
            if the_new_date < return_date:
                duration = (return_date - the_new_date).days                
            else:
                return False
        else:
            if the_new_date > pickup_date:
                duration = (the_new_date - pickup_date).days
            else:
                return False

        new_total = self.calculate_final_price(duration, the_vehicle)
        self.edit_contract_info(filter_or_id, attribute, new_date)
        self.edit_contract_info(filter_or_id, "duration", duration)
        results = self.edit_contract_info(filter_or_id, "final_price", new_total)
        return results