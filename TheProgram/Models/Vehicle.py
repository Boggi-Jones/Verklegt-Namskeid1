class Vehicle():
    def __init__(self, status, type_of_vehicle, model, rate, manufacturer, condition, model_year, color, number_plate, driving_license, rent_counter , name_of_airport):
        self.status = status
        self.type_of_vehicle = type_of_vehicle
        self.model = model
        self.rate = rate
        self.manufacturer = manufacturer
        self.condition = condition
        self.model_year = model_year
        self.color = color
        self.number_plate = number_plate
        self.driving_license = driving_license
        self.rent_counter = rent_counter
        self.name_of_airport = name_of_airport

    def fieldnames(self):
        return ["status", "type_of_vehicle", "model", "rate", "manufacturer", "condition", "model_year", "color", "number_plate", "driving_license", "rent_counter", "name_of_airport"]
    
    def add_to_dict(self):
        return {"status" : self.status, "type_of_vehicle" : self.type_of_vehicle, "model" : self.model, "rate" : self.rate, "manufacturer": self.manufacturer, "condition": self.condition, "model_year" : self.model_year, "color":self.color, "number_plate": self.number_plate, "driving_license": self.driving_license, "rent_counter": self.rent_counter, "name_of_airport": self.name_of_airport}
    
    
    def __str__(self):
        return "{:^13s}| {:^16s}|{:^15s}|{:^6s}|{:^17s}|{:^11s}|{:^12s}|{:^12s}|{:^14s}|{:^9s}|{:^9s}|{:^16s}".format(self.status, self.type_of_vehicle, self.model, self.rate, self.manufacturer, self.condition, self.model_year, self.color, self.number_plate, self.driving_license, self.rent_counter, self.name_of_airport)