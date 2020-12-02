import csv
from Models.Employee import Employee

class DataMain():

    def get_list(self, filename):
        retList = []
        with open(f"Data/data/{filename}.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if filename == "Employee":
                    emp = Employee(row["name"], row["ssn"], row["address"], row["home_phone"], row["gsm_phone"], row["email"], row["location"], row["role"])
                    retList.append(emp)
        return retList

    def add_to_list(self, filename, value):
        with open(f"Data/data/{filename}.csv", "a",  newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = value.fieldnames())
            writer.writerow(value.add_to_dict())
        csvfile.close()

    def overwrite(self, filename, list_of_items):
        with open(f"Data/data/{filename}.csv","w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "ssn", "address", "home_phone", "gsm_phone", "email", "location", "role"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for i in list_of_items:                
                writer.writerow(i.add_to_dict())
            
        csvfile.close()
