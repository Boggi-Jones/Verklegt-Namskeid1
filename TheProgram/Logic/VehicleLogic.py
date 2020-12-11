from Data.DataMain import DataMain

class VehicleLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Vehicle"

    def filter_vehicle_fleet(self, filter_or_id, attribute):
        ''' Gets a list of all vehicles from data. If there is no filter it just returns the full list.
        If there is a filter then it iterates through the list. It adds everything to a new list that has the filter in the chosen attribute.'''
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
        ''' Gets a list from data of all vehicles. Then iterates through the list and removes the vehicle with the given number plate.
        Then sends the rest of the list to data to rewrite everything without the removed vehicle.'''
        list_of_vehicles = self.filter_vehicle_fleet(None, None)
        for vehicle in list_of_vehicles:
            if vehicle.__getattribute__("number_plate") == filter_or_id:
                list_of_vehicles.remove(vehicle)
        self.datamain.overwrite(self.position, list_of_vehicles) 

    def register_new_vehicle(self, new_information):
        ''' Tells data to add this vehicle to the system'''
        self.datamain.add_to_list(self.position, new_information)

    def edit_vehicle_info(self, filter_or_id, attribute, new_information):
        ''' Gets a list of one vehicle by filtering with the number plate and then changes the chosen attribute.
        Then it removes that vehicle from data and adds the updated one.'''
        single_vehicle = self.filter_vehicle_fleet(filter_or_id, "number_plate")
        for vehicle in single_vehicle:
            vehicle.__setattr__(attribute, new_information)
            self.remove_vehicle(filter_or_id)
            self.register_new_vehicle(vehicle)

        return single_vehicle

    def edit_rate(self, vehicle_type, current_rate, new_rate):
        ''' Gets a list of all vehicles of the chosen type. Then goes through the entire list doing the same as in edit_vehicle_info.'''
        list_of_vehicles = self.filter_vehicle_fleet(vehicle_type, "type_of_vehicle")
        for vehicle in list_of_vehicles:
            vehicle.__setattr__("rate", new_rate)
            self.remove_vehicle(vehicle)
            self.register_new_vehicle(vehicle)
        return list_of_vehicles
