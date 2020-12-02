from Data.DataMain import DataMain
class VehicleLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Vehicle"

    def filtervehiclefleet(self, filter_or_id, attribute):
        list_of_vehicles = self.datamain.getlist(self.position)
        retlist = []
        if filter_or_id != None:
            for vehicle in list_of_vehicles:
                if vehicle.__getattribute__(attribute) == filter_or_id:
                    retlist.append(vehicle)
            return retlist
        else:
            return list_of_vehicles

    def editvehicleinfo(self, filter_or_id, attribute, new_information):
        single_vehicle = self.datamain.get_one_item(self.position, filter_or_id)
        single_vehicle.__setattr__(attribute, new_information)
        self.datamain.removeitem(self.position, filter_or_id)
        self.datamain.add_to_list(self.position, single_vehicle)

    def registernewvehicle(self, new_information):
        self.datamain.add_to_list(self.position, new_information)

    def editrate(self, vehicle_type, current_rate, new_rate):
        list_of_vehicles = self.datamain.get_list(self.position)
        returning_list = []
        for vehicle in list_of_vehicles:
            if vehicle.rate == current_rate:
                returning_list.append(vehicle)
        for vehicle in returning_list:
            vehicle.__setattr__(rate, new_rate)
