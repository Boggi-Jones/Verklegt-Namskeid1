from Data.DataMain import DataMain

class ContractLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Contract"

    def filtercontract(self, filter_or_id, attribute):
        list_of_contracts = self.datamain.getlist(self.position)
        retlist = []
        if filter_or_id != None:
            for contract in list_of_contracts:
                if contract.__getattribute__(attribute) == filter_or_id:
                    retlist.append(contract)
            return retlist
        else:
            return list_of_contracts

    def makenewcontract(self, new_information):
        self.datamain.add_to_list(self.position, new_information)

    def editcontractinfo(self, filter_or_id, attribute, new_information):
        single_contract = self.datamain.getoneitem(self.position, filter_or_id)
        single_contract.__setattr__(attribute, new_information)
        self.datamain.remove_item(self.position, filter_or_id)
        self.datamain.add_to_list(self.position, single_contract)

    def cancelcontract(self, filter_or_id):
        self.datamain.remove_item(self.position, filter_or_id)

    def printcontract(self, filter_or_id):
        return self.datamain.getoneitem(self.position, filter_or_id)

    def calculatefinalprice(self, filter_or_id):
        single_contract = self.datamain.getoneitem(self.position, filter_or_id)
        return single_contract.total



    #DataMain.getlist("Contract")
    #def getlist(self, value):
        #with open(f"Data/data/{value}.csv")