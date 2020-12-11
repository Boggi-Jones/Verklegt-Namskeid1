import csv
from Models.Employee import Employee
from Models.Location import Location
from Models.Vehicle import Vehicle
from Models.Contract import Contracts
from Models.Customer import Customer
from Models.Role import Role

import os

class DataMain():
    def __init__(self):
        self.model_dict = {"<class 'Models.Employee.Employee'>" : "Employee.csv", "<class 'Models.Location.Location'>" : "Location.csv", "<class 'Models.Vehicle.Vehicle'>" : "Vehicle.csv", "<class 'Models.Contract.Contracts'>" : "Contract.csv", "<class 'Models.Customer.Customer'>" : "Customer.csv", "<class 'Models.Role.Role'>" : "Role.csv"}

    def get_list(self, model_class):
        retList = []
        with open(f"Data/data/{self.model_dict[str(type(model_class))]}", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if self.model_dict[str(type(model_class))] == "Employee.csv":
                    emp = Employee(row["name"], row["ssn"], row["address"], row["home_phone"], row["gsm_phone"], row["email"], row["location"], row["role"], row["password"])
                    retList.append(emp)
                elif self.model_dict[str(type(model_class))] == "Role.csv":
                    roles = Role(row["role"], row["name"], row["ssn"])
                    retList.append(roles)
                elif self.model_dict[str(type(model_class))] == "Location.csv":
                    loc = Location(row["name_of_airport"], row["country"], row["opening_hours"], row["phone_number"])
                    retList.append(loc)
                elif self.model_dict[str(type(model_class))] == "Vehicle.csv":
                    vehicle = Vehicle(row["status"], row["type_of_vehicle"], row["model"], row["rate"], row["manufacturer"], row["condition"], row["model_year"], row["color"], row["number_plate"], row["driving_license"], row["rent_counter"], row["name_of_airport"])
                    retList.append(vehicle)
                elif self.model_dict[str(type(model_class))] == "Contract.csv":
                    contract = Contracts(row["date"], row["return_date"], row["duration"], row["name_of_airport"], row["employee_name"], row["paid"], row["final_price"], row["number_plate"], row["ssn"])
                    retList.append(contract)
                elif self.model_dict[str(type(model_class))] == "Customer.csv":
                    customer = Customer(row["name"], row["ssn"], row["email"], row["gsm_number"], row["address"], row["driving_license"], row["returned_late_before"])
                    retList.append(customer)
        return retList
        
    def add_to_list(self, value):
        with open(f"Data/data/{self.model_dict[str(type(value))]}", "a",  newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = value.fieldnames())
            writer.writerow(value.add_to_dict())
        csvfile.close()

    def overwrite(self, list_of_items, model_class):
        with open(f"Data/data/{self.model_dict[str(type(model_class))]}","w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = list(model_class.__dict__.keys()))
            writer.writeheader()
            for i in list_of_items:                
                writer.writerow(i.add_to_dict())
            
        csvfile.close()
