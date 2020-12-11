class Location(object):
    def __init__(self, name_of_airport = "", country = "", opening_hours = "", phone_number=""):
        self.name_of_airport = name_of_airport
        self.country = country
        self.opening_hours = opening_hours
        self.phone_number = phone_number
    
    def fieldnames(self):
        return ["name_of_airport", "country", "opening_hours", "phone_number"]
    def add_to_dict(self):
        return {"name_of_airport" : self.name_of_airport, "country" : self.country, "opening_hours" : self.opening_hours, "phone_number": self.phone_number}
    
    def __str__(self):
        return "{:^26s} | {:^26s} | {:^19s} | {:^17s}".format(self.name_of_airport, self.country, self.opening_hours, self.phone_number)