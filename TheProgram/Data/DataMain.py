import csv
from Models.Employee import Employee
from Models.Location import Location
from Models.Vehicle import Vehicle

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
                    vehicle = Vehicle(row["status"], row["type_of_vehicle"], row["rate"], row["manufacturer"], row["condition"], row["age"], row["color"], row["number_plate"], row["driving_license"], row["rent_counter"], row["name_ofAirport"], row["country"])
                    retList.append(vehicle)
                elif filename == "Contaract":
                    vehicle = Vehicle(row["data"], row["duration"], row["country"], row["city"], row["employee_name"], row["paid"], row["final_price"], row["Vehicle"], row["Customer"])
                    retList.append(vehicle)
        return retList

    def add_to_list(self, filename, value):
        with open(f"Data/data/{filename}.csv", "a",  newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = value.fieldnames())
            writer.writerow(value.add_to_dict())
        csvfile.close()

    def overwrite(self, filename, list_of_items, fieldname):
        with open(f"Data/data/{filename}.csv","w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fieldname)
            writer.writeheader()
            for i in list_of_items:                
                writer.writerow(i.add_to_dict())
            
        csvfile.close()
