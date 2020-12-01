from Location import Location
class vehicle(Location):
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
    
    def __str__(self):
        pass