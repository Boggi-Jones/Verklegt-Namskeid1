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
        ''' Gets a list of all contracts from data. If there is no filter it just returns the full list.
        If there is a filter then it iterates through the list. It adds everything to a new list that has the filter in the chosen attribute.'''
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
        ''' Gets a list from data of all contracts. Then iterates through the list and removes the contract with the given ssn.
        Then sends the rest of the list to data to rewrite everything without the removed contract.'''
        list_of_contracts = self.filter_contract(None, None)
        for contract in list_of_contracts:
            if contract.ssn == filter_or_id:
                the_removed_contract = contract
                list_of_contracts.remove(contract)
                self.datamain.overwrite(self.position, list_of_contracts)

                return the_removed_contract

    def make_new_contract(self, new_information):
        ''' Tells data to add this contract to the system'''
        self.datamain.add_to_list(self.position, new_information)

    def edit_contract_info(self, filter_or_id, attribute, new_information):
        ''' Gets a list of one contract by filtering with the ssn and then changes the chosen attribute.
        Then it removes that contract from data and adds the updated one.'''
        single_contract = self.filter_contract(filter_or_id, "ssn")
        single_contract[0].__setattr__(attribute, new_information)
        self.cancel_contract(filter_or_id)
        self.make_new_contract(single_contract[0])
        return self.filter_contract(filter_or_id, "ssn")
        
    def check_license(self, customer_class, number_plate):
        ''' Gets the vehicle class for the given number plate. Then compares the required license for the vehicle to the customers license.
        If the user doesn't have the required license it returns an empty list.'''
        vehicle_class = self.vehiclelogic.filter_vehicle_fleet(number_plate, "number_plate")
        if customer_class.driving_license in vehicle_class[0].driving_license:
            return vehicle_class

    def change_vehicle(self, contract_class, attribute, new_information):
        ''' Changes vehicle for contract. First it gets the new vehicle and if the status of that vehicle is unavailable it returns False.
        If it is available it changes the status for the current vehicle and the new one. Then it calculates new price.
        It then updates the contract with the new number plate and new price. Finally it returns the updated contract.'''
        new_vehicle = self.vehiclelogic.filter_vehicle_fleet(new_information, attribute)

        if new_vehicle[0].status == "available":
            self.vehiclelogic.edit_vehicle_info(contract_class[0].number_plate, "status", "available")
            the_vehicle = self.vehiclelogic.edit_vehicle_info(new_information, "status", "unavailable")
            self.edit_contract_info(contract_class[0].ssn, attribute, new_information)
            total_price = self.calculate_final_price(contract_class[0].duration, the_vehicle)
            self.edit_contract_info(contract_class[0].ssn, "final_price", total_price)
            return self.filter_contract(contract_class[0].ssn, "ssn")
        else:
            return False

    def charge_contract(self, ssn, condition):
        ''' Allows the user to pay for the contract. First it gets the current date and the chosen contract.
        Then it checks if it is already paid. After that it updates everything it needs to on the vehicle and the contract.
        Finally it returns the final sum to charge the customer.'''
        current_date = datetime.today()
        the_contract = self.filter_contract(ssn, "ssn")
        if the_contract[0].paid == "no":
            return_date = datetime.strptime(the_contract[0].return_date + " 23:59", '%d/%m/%Y %H:%M') # Collect the agreed return date with 23:59 to give customer a chance to return it.
            if condition == 1:
                self.vehiclelogic.edit_vehicle_info(the_contract[0].number_plate, "status", "available") # If condition is good the vehicle becomes available
            else:
                self.vehiclelogic.edit_vehicle_info(the_contract[0].number_plate, "condition", "in repairs") # If not condition has to be fixed
            
            duration = (current_date - datetime.strptime(the_contract[0].date,'%d/%m/%Y')).days # Figure out how long if it was returned early or late
            the_vehicle = self.vehiclelogic.filter_vehicle_fleet(the_contract[0].number_plate, "number_plate")
            new_total = int(self.calculate_final_price(duration, the_vehicle)) # Calculate with new duration
            self.edit_contract_info(ssn, "return_date", datetime.strftime(current_date,'%d/%m/%Y'))
            self.edit_contract_info(ssn, "duration", duration)
            self.vehiclelogic.edit_vehicle_info(the_contract[0].number_plate, "rent_counter", (int(the_vehicle[0].rent_counter) + int(duration)))
            
            if current_date > return_date:    # If customer returned late we charge 20% extra
                new_total = new_total * 1.2
                self.edit_contract_info(ssn, "final_price", new_total)
                self.customerlogic.edit_customer(ssn, "returned_late_before", "yes")
                return str(new_total)
            
            self.edit_contract_info(ssn, "final_price", new_total)
            return str(new_total)
        else:
            return None

    def calculate_final_price(self, duration, vehicle_class):
        ''' Multiplies the rate for the chosen vehicle with the duration to give back the total price.'''
        rate = vehicle_class[0].rate
        total = int(duration) * int(rate)
        return str(total)

    def edit_contract_date(self, filter_or_id, attribute, new_date):
        ''' Takes in either pickup date or return date. Changes the duration, date and the total for that contract'''
        the_contract = self.filter_contract(filter_or_id, "ssn")
        the_vehicle = self.vehiclelogic.filter_vehicle_fleet(the_contract[0].number_plate, "number_plate")
        return_date = datetime.strptime(the_contract[0].return_date, '%d/%m/%Y')
        pickup_date = datetime.strptime(the_contract[0].date, '%d/%m/%Y')
        the_new_date = datetime.strptime(new_date, '%d/%m/%Y')
        
        if attribute == "date": # For editing pickup date
            if the_new_date < return_date: # Pickup date can't be later than return date
                duration = (return_date - the_new_date).days                
            else:
                return False
        else: # For editing return date
            if the_new_date > pickup_date:
                duration = (the_new_date - pickup_date).days
            else:
                return False

        new_total = self.calculate_final_price(duration, the_vehicle)
        self.edit_contract_info(filter_or_id, attribute, new_date)
        self.edit_contract_info(filter_or_id, "duration", duration)
        results = self.edit_contract_info(filter_or_id, "final_price", new_total)
        return results