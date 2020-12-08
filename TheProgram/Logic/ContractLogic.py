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

    def filtercontract(self, filter_or_id, attribute):
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

    def cancelcontract(self, filter_or_id):
        # Gets list of contractts from filtercontract function
        # Contract is then iterated through list of contract searching for matching attribute
        # If contracts attribut(ssn) matches with filter or id, it´s deleted
        # List of contract is then overwritten with updated list
        list_of_contracts = self.filtercontract(None, None)
        for contract in list_of_contracts:
            if contract.ssn == filter_or_id:
                the_removed_contract = contract
                list_of_contracts.remove(contract)
                self.datamain.overwrite(self.position, list_of_contracts)
                return the_removed_contract

    def makenewcontract(self, new_information):
        # New contract is added to list
        self.datamain.add_to_list(self.position, new_information)

    def editcontractinfo(self, filter_or_id, attribute, new_information):
        # Single contract is created from the filtercontract function using the ssn attribute
        # Single contract is then updated with new information with cancel contract and make new contract funtions
        single_contract = self.filtercontract(filter_or_id, "ssn")
        single_contract[0].__setattr__(attribute, new_information)
        self.cancelcontract(filter_or_id)
        self.makenewcontract(single_contract[0])
        return single_contract[0]

    def checklicense(self, customer_class, number_plate):
        # After user chooses vehicle
        # Driver license attribute is compared to vehicle driving license attribute
        # Vehicle class is then returned
        vehicle_class = self.vehiclelogic.filtervehiclefleet(number_plate, "number_plate")
        if customer_class.driving_license in vehicle_class[0].driving_license:
            return vehicle_class

    def changevehicle(self, number_plate, attribute, new_information):
        new_vehicle = self.vehiclelogic.filtervehiclefleet(new_information, attribute)

        if new_vehicle[0].status == "available":
            self.vehiclelogic.editvehicleinfo(number_plate, "status", "available")
            the_vehicle = self.vehiclelogic.editvehicleinfo(new_information, "status", "rented")
            results = self.editcontractinfo(number_plate, attribute, new_information)
            total_price = self.calculatefinalprice(results.duration, the_vehicle)
            results = self.editcontractinfo(number_plate, "final_price", total_price)
        else:
            return False

    def chargecontract(self, ssn, condition):
        # contract paid í yes
        # spyrja um ástand ef good þá gera hann available
        # fá current date og bera saman við skiladag
        # ef skilað seint bæta við 20% á verðið og breyta customer returned_late_before í yes
        # skila til baka lokaverði
        current_date = datetime.today()
        the_contract = self.filtercontract(ssn, "ssn")
        return_date = datetime.strptime(the_contract[0].return_date, '%d/%m/%Y')
        self.editcontractinfo(ssn, "paid", "yes")
        if current_date > return_date:
            return True
        else:
            return False

    def calculatefinalprice(self, duration, vehicle_class):
        # After user has chosen vehicle
        # Variable called rate is created using the rate attribute from vehicle function
        # Total price is than calculated by multiplying duration ( total days rented ) with rate
        # Final price is returned
        rate = vehicle_class[0].rate
        total = int(duration) * int(rate)
        return total
