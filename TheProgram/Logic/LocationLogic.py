from Data.DataMain import DataMain

class LocationLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Location"

    def filtercountry(self, filter_or_id, attribute):
        #Gets list of location from data main
        # If filter or Id == None, iterate through list of locations and appends if location.attribute == filter or id
        # Then return retlist
        #If filter or id == None, return list oflocations
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
        # Creates a viariable calles list of location
        # iterates through list of locations
        # if name of airport attribute == filter or id, remove it from location
        #overwrite a list of new location with updated list
        list_of_locations = self.filtercountry(None, None)
        for location in list_of_locations:
            if location.__getattribute__("name_of_airport") == filter_or_id:
                list_of_locations.remove(location)
        self.datamain.overwrite(self.position, list_of_locations)
     
    def addlocation(self, new_information):
        # Add new location to list with new information
        self.datamain.add_to_list(self.position, new_information)
    
    def editlocationinfo(self, filter_or_id, attribute, new_information):
        # Creates new variable called single location with info from filtercountry
        # Iterates through single location looking for location attribute
        # Removes location from list
        # updates location information
        single_location = self.filtercountry(filter_or_id, "name_of_airport")
        for location in single_location:
            location.__setattr__(attribute, new_information)
            self.removelocation(filter_or_id)
            self.addlocation(location)

        return single_location[0]
