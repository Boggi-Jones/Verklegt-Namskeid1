from Data.DataMain import DataMain

class VehicleLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Vehicle"

    def filtervehiclefleet(self, filter_or_id, attribute):
        list_of_vehicles = self.datamain.get_list(self.position)
        retlist = []
        if filter_or_id != None:
            for vehicle in list_of_vehicles:
                if vehicle.__getattribute__(attribute) == filter_or_id:
                    retlist.append(vehicle)
            return retlist
        else:
            return list_of_vehicles

    def remove_vehicle(self, filter_or_id):
        list_of_vehicles = self.filtervehiclefleet(None, None)
        for vehicle in list_of_vehicles:
            if vehicle.__getattribute__("number_plate") == filter_or_id:
                list_of_vehicles.remove(vehicle)
        self.datamain.overwrite(self.position, list_of_vehicles)

    def registernewvehicle(self, new_information):
        self.datamain.add_to_list(self.position, new_information)

    def editvehicleinfo(self, filter_or_id, attribute, new_information):
        single_vehicle = self.filtervehiclefleet(filter_or_id, "number_plate")
        for vehicle in single_vehicle:
            vehicle.__setattr__(attribute, new_information)
            self.remove_vehicle(filter_or_id)
            self.registernewvehicle(vehicle)

    def remove_vehicle_by_type(self, vehicle_type):
        list_of_vehicles = self.filtervehiclefleet(None, None)
        for vehicle in list_of_vehicles:
            if vehicle.__getattribute__("vehicle_type") == vehicle_type:
                list_of_vehicles.remove(vehicle)
        self.datamain.overwrite(self.position, list_of_vehicles)

    def editrate(self, vehicle_type, current_rate, new_rate):
        list_of_vehicles = self.filtervehiclefleet(vehicle_type, "type_of_vehicle")
        for vehicle in list_of_vehicles:
            vehicle.__setattr__("rate", new_rate)
        self.remove_vehicle_by_type(vehicle_type)
        self.registernewvehicle(list_of_vehicles)
        return list_of_vehicles