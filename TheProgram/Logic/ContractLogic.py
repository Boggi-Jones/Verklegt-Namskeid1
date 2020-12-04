from Data.DataMain import DataMain

class ContractLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Contract"

    def filtercontract(self, filter_or_id, attribute):
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
        list_of_contracts = self.filtercontract(None, None)
        for contract in list_of_contracts:
            if contract.ssn == filter_or_id:
                the_removed_contract = contract
                list_of_contracts.remove(contract)
                self.datamain.overwrite(self.position, list_of_contracts)
                return the_removed_contract

    def makenewcontract(self, new_information):
        self.datamain.add_to_list(self.position, new_information)

    def editcontractinfo(self, filter_or_id, attribute, new_information):
        single_contract = self.filtercontract(filter_or_id, "ssn")
        for contract in single_contract:
            single_contract.__setattr__(attribute, new_information)
            self.cancelcontract(filter_or_id)
            self.makenewcontract(contract)

    def checklicense(self, customer_class, vehicle_class):
        if customer_class.driving_license in vehicle_class[0].driving_license:
            return vehicle_class

    def calculatefinalprice(self, duration, vehicle_class):
        for vehicle in vehicle_class:
            rate = vehicle.__getattribute__("rate")
            total = int(duration) * int(rate)
        return total
