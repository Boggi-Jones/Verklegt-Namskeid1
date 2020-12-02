from Vehicle import Vehicle
from Customer import Customer


class Contracts(Vehicle, Customer):
    def __init__(self, date, duration, country, city, employee_name, paid, final_price, Vehicle, Customer):
        self.Vehicle = Vehicle
        self.Customer = Customer
        self.date = date
        self.duration = duration
        self.country = country
        self.city = city
        self.employee_name = employee_name
        self.paid = paid
        self.final_price = final_price
    
    def fieldnames(self):
        return ["date", "duration", "country", "city", "employee_name", "paid", "final_price", "vehicle", "customer"]

    def add_to_dict(self):
        return {"date" : self.date, "duration" : self.duration, "country" : self.country, "city": self.city, "employee_name": self.employee_name, "paid" : self.paid, "final_price":self.final_price, "vehicle": self.Vehicle, "customer": self.Customer}
    
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.date, self.duration, self.country, self.city, self.employee_name, self.paid, self.final_price, self.Vehicle, self.Customer)