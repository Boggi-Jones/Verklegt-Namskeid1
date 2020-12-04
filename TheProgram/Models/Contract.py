class Contracts:
    def __init__(self, date, duration, name_of_airport, employee_name, paid, final_price, number_plate, ssn):
        self.date = date
        self.duration = duration
        self.name_of_airport = name_of_airport
        self.employee_name = employee_name
        self.paid = paid
        self.final_price = final_price
        self.number_plate = number_plate
        self.ssn = ssn
    
    def fieldnames(self):
        return ["date", "duration", "name_of_airport", "employee_name", "paid", "final_price", "number_plate", "ssn"]

    def add_to_dict(self):
        return {"date" : self.date, "duration" : self.duration, "name_of_airport" : self.name_of_airport, "employee_name": self.employee_name, "paid" : self.paid, "final_price":self.final_price, "number_plate": self.number_plate, "ssn": self.ssn}
    
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(self.date, self.duration, self.name_of_airport, self.employee_name, self.paid, self.final_price, self.number_plate, self.ssn)