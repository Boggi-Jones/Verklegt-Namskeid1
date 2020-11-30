from Data.DataMain import DataMain
from Logic.EmployeeLogic import EmployeeLogic
from Logic.LocationLogic import LocationLogic
from Logic.VehicleLogic import VehicleLogic
from Logic.ContractLogic import ContractLogic

class LogicMain:
    def __init__(self):
        print("works")
        self.data = DataMain()
        self.employeelogic = EmployeeLogic()
        self.locationlogic = LocationLogic()
        self.vehiclelogic = VehicleLogic()
        self.contractlogic = ContractLogic()
        print("works more")
        


    def employee(self, option, filter, attribute):
        if option == 0:
            results = self.employeelogic.filteremployees(filter, attribute)
        elif option == 1:
            results = self.employeelogic.removeemployee(filter)
        elif option == 2:
            results = self.employeelogic.addemployee()
        else:
            results = self.employeelogic.editemployeeinfo()

        return results

    def location(self, option, filter = None):
        if option == 0:
            results = self.locationlogic.filtercountry(filter)
        elif option == 1:
            results = self.locationlogic.addlocation()
        elif option == 2:
            results = self.locationlogic.removelocation()
        else:
            results = self.locationlogic.editlocationinfo()

        return results

    def vehicle(self, option, filter = None):
        if option == 0:
            results = self.vehiclelogic.filtervehiclefleet()
        elif option == 1:
            results = self.vehiclelogic.editvehicleinfo()
        elif option == 2:
            results = self.vehiclelogic.registernewvehicle()
        else:
            results = self.vehiclelogic.editrate()

        return results

    def contract(self, option, filter = None):
        if option == 0:
            results = self.contractlogic.filtercontract()
        elif option == 1:
            results = self.contractlogic.makenewcontract()
        elif option == 2:
            results = self.contractlogic.editcontractinfo()
        elif option == 3:
            results = self.contractlogic.cancelcontract()
        elif option == 4:
            results = self.contractlogic.printcontract()
        else:
            results = self.contractlogic.calculatefinalprice()

        return results