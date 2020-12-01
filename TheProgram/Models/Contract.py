from Vehicle import Vehicle
from Customer import Customer


class Contracts(Vehicle, Customer):
    def __init__(self, date, duration, country, city, employee_name, paid, final_price, Vehicle = Vehicle(), Customer = Customer() ):
        self.Vehicle = Vehicle
        self.Customer = Customer
        self.date = date
        self.duration = duration
        self.country = country
        self.city = city
        self.employee_name = employee_name
        self.paid = paid
        self.final_price = final_price

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.date, self.duration, self.country, self.city, self.employee_name, self.paid, self.final_price, self.Vehicle, self.Customer)