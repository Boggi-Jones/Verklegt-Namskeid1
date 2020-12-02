from Data.DataMain import DataMain

class LocationLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Location"

    def filtercountry(self, filter_or_id, attribute):
        list_of_locations = self.datamain.get_list(self.position)
        retlist = []
        if filter_or_id != None:
            for location in list_of_locations:
                if location.__getattribute__(attribute) == filter_or_id:
                    retlist.append(location)
            return retlist
        else:
            return list_of_locations

    def removelocation(self, filter_or_id):
        list_of_locations = self.filtercountry(None, None)
        for location in list_of_locations:
            if location.__getattribute__("name_of_airport") == filter_or_id:
                list_of_locations.remove(location)
        self.datamain.overwrite(self.position, list_of_locations)
     
    def addlocation(self, new_information):
        self.datamain.add_to_list(self.position, new_information)
    
    def editlocationinfo(self, filter_or_id, attribute, new_information):
        single_location = self.filtercountry(filter_or_id, "name_of_airport")
        for location in single_location:
            location.__setattr__(attribute, new_information)
            self.removelocation(filter_or_id)
            self.addlocation(location)
