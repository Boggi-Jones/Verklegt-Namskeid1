from Location import Location
class Vehicle(Location):
    def __init__(self, status, type_of_vehicle, rate, manufacturer, condition, age, color, number_plate, driving_license, rent_counter, name_of_airport, country):
        super().__init__(name_of_airport, country)
        self.status = status
        self.type_of_vehicle = type_of_vehicle
        self.rate = rate
        self.manufacturer = manufacturer
        self.condition = condition
        self.age = age
        self.color = color
        self.number_plate = number_plate
        self.driving_license = driving_license
        self.rent_counter = rent_counter

    def fieldnames(self):
        return ["status", "type_of_vehicle", "rate", "manufacturer", "condition", "age", "color", "number_plate", "driving_licese", "rent_counter", "name_of_airport", "country"]
    def add_to_dict(self):
        return {"status" : self.status, "type_of_vehicle" : self.type_of_vehicle, "rate" : self.rate, "manufacturer": self.manufacturer, "condition": self.condition, "age" : self.age, "color":self.color, "number_plate": self.number_plate, "driving_license": self.driving_license, "rent_counter": self.rent_counter, "name_of_airport": self.name_of_airport, "country": self.country}
    
    
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.status, self.type_of_vehicle, self.rate, self.manufacturer, self.condition, self.age, self.color, self.number_plate, self.driving_license, self.rent_counter, self.name_of_airport, self.country)