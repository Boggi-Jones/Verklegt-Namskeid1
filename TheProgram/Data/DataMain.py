import csv
from Models.Employee import Employee
from Models.Location import Location
from Models.Vehicle import Vehicle
from Models.Contract import Contracts
from Models.Customer import Customer

import os


class DataMain():

    def get_list(self, filename):
        retList = []
        with open(f"Data/data/{filename}.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if filename == "Employee":
                    emp = Employee(row["name"], row["ssn"], row["address"], row["home_phone"], row["gsm_phone"], row["email"], row["location"], row["role"])
                    retList.append(emp)
                elif filename == "Location":
                    loc = Location(row["name_of_airport"], row["country"], row["opening_hours"], row["phone_number"])
                    retList.append(loc)
                elif filename == "Vehicle":
                    vehicle = Vehicle(row["status"], row["type_of_vehicle"], row["model"], row["rate"], row["manufacturer"], row["condition"], row["model_year"], row["color"], row["number_plate"], row["driving_license"], row["rent_counter"], row["name_of_airport"])
                    retList.append(vehicle)
                elif filename == "Contract":
                    contract = Contracts(row["date"], row["return_date"], row["duration"], row["name_of_airport"], row["employee_name"], row["paid"], row["final_price"], row["number_plate"], row["ssn"])
                    retList.append(contract)
                elif filename == "Customer":
                    customer = Customer(row["name"], row["ssn"], row["email"], row["gsm_number"], row["address"], row["driving_license"], row["returned_late_before"])
                    retList.append(customer)
        return retList
        
    def add_to_list(self, filename, value):
        with open(f"Data/data/{filename}.csv", "a",  newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = value.fieldnames())
            writer.writerow(value.add_to_dict())
        csvfile.close()

    def overwrite(self, filename, list_of_items):
        with open(f"Data/data/{filename}.csv","w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = list(list_of_items[0].__dict__.keys()))
            writer.writeheader()
            for i in list_of_items:                
                writer.writerow(i.add_to_dict())
            
        csvfile.close()
