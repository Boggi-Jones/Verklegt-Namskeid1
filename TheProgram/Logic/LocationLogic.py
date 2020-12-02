from Data.DataMain import DataMain
class LocationLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Location"

    def filtercountry(self, filter_or_id, attribute):
        list_of_locations = self.datamain.getlist(self.position)
        retlist = []
        if filter_or_id != None:
            for location in list_of_locations:
                if location.__getattribute__(attribute) == filter_or_id:
                    retlist.append(location)
            return retlist
        else:
            return list_of_locations

    def addlocation(self, new_information):
        self.datamain.add_to_list(self.position, new_information)

    def removelocation(self, filter_or_id):
        self.datamain.removeitem(self.position, filter_or_id)
    
    def editlocationinfo(self, filter_or_id, attribute, new_information):
        single_location = self.datamain.get_one_item(self.position, filter_or_id)
        single_location.__setattr__(attribute, new_information)
        self.datamain.removeitem(self.position, filter_or_id)
        self.datamain.add_to_list(self.position, single_location)
