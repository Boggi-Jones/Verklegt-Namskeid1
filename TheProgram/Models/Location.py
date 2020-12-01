class Location(object):
    def __init__(self, name_of_airport, country, opening_hours = "", phone_number=""):
        self.name_of_airport = name_of_airport
        self.country = country
        self.opening_hours = opening_hours
        self.phone_number = phone_number
    
    def __str__(self):
        pass