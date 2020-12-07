from Data.DataMain import DataMain

class VehicleLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Vehicle"

    def filtervehiclefleet(self, filter_or_id, attribute):
        # Creates a variable called list of vehicles
        # if the filter or id is not in the list, they get appended
        # The retlist is then returned
        # If filter or id is in the list, list of vehicle is returned
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
        # Removes vehicles from list using number_plate as identifier
        list_of_vehicles = self.filtervehiclefleet(None, None)
        for vehicle in list_of_vehicles:
            if vehicle.__getattribute__("number_plate") == filter_or_id:
                list_of_vehicles.remove(vehicle)
        self.datamain.overwrite(self.position, list_of_vehicles) 

    def registernewvehicle(self, new_information):
        #self explanitory?
        self.datamain.add_to_list(self.position, new_information)

    def editvehicleinfo(self, filter_or_id, attribute, new_information):
        # Creates a variable called single vehicle by getting information from filter vehicle fleet
        # Vehicle is identified using number plate
        # Attribute is set using a for loop
        # Old information is then removed and updated informations is added
        single_vehicle = self.filtervehiclefleet(filter_or_id, "number_plate")
        for vehicle in single_vehicle:
            vehicle.__setattr__(attribute, new_information)
            self.remove_vehicle(filter_or_id)
            self.registernewvehicle(vehicle)

        return single_vehicle[0]

    def editrate(self, vehicle_type, current_rate, new_rate):
        # Cretes a list of vehicle by using information from type of vehicle
        # New rate is set by using a for loop
        # old vehicle is removed from the list
        # new vehicle is registered through the registernewvehicle function with the new rate
        # Returns updated list of vehicle with new rates.
        list_of_vehicles = self.filtervehiclefleet(vehicle_type, "type_of_vehicle")
        for vehicle in list_of_vehicles:
            vehicle.__setattr__("rate", new_rate)
            self.remove_vehicle(vehicle)
            self.registernewvehicle(vehicle)
        return list_of_vehicles
