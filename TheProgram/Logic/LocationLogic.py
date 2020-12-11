from Data.DataMain import DataMain

class LocationLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Location"

    def filter_country(self, filter_or_id, attribute):
        ''' Gets a list of all locations from data. If there is no filter it just returns the full list.
        If there is a filter then it iterates through the list. It adds everything to a new list that has the filter in the chosen attribute.'''
        list_of_locations = self.datamain.get_list(self.position)
        retlist = []
        if filter_or_id != None:
            for location in list_of_locations:
                if location.__getattribute__(attribute) == filter_or_id:
                    retlist.append(location)
            return retlist
        else:
            return list_of_locations

    def remove_location(self, filter_or_id):
        ''' Gets a list from filter country with all locations. Then iterates through the list and removes the location with the given name of airport.
        Then sends the rest of the list to data to rewrite everything without the removed location.'''
        list_of_locations = self.filter_country(None, None)
        for location in list_of_locations:
            if location.__getattribute__("name_of_airport") == filter_or_id:
                list_of_locations.remove(location)
        self.datamain.overwrite(self.position, list_of_locations)
     
    def add_location(self, new_information):
        ''' Tells data to add this location to the system'''
        self.datamain.add_to_list(self.position, new_information)
    
    def edit_location_info(self, filter_or_id, attribute, new_information):
        ''' Gets a list of one location by filtering with the name of airport and then changes the chosen attribute.
        Then it removes that location from data and adds the updated one.'''
        single_location = self.filter_country(filter_or_id, "name_of_airport")
        for location in single_location:
            location.__setattr__(attribute, new_information)
            self.remove_location(filter_or_id)
            self.add_location(location)

        return single_location[0]
