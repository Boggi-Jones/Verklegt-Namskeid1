import csv
<<<<<<< HEAD
from models.Employee import Employee
=======
from Models.Employee import Employee
>>>>>>> 2894248e215f43b1a456a456345c20e4a2abd3f3
class DataMain():
    def get_list(self, filename):
        retList = []
        with open(f"Data/data/{filename}.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if filename == "Employee":
<<<<<<< HEAD
                    emp = Employee(row["name"], row["ssn"], row["adress"], row["home_phone"], row["gsm_phone"], row["email"], row["location"], row["role"])
=======
                    emp = Employee(row["name"], row["ssn"], row["address"], row["home_phone"], row["gsm_phone"], row["email"], row["location"], row["role"])
>>>>>>> 2894248e215f43b1a456a456345c20e4a2abd3f3
                    retList.append(emp)
        return retList
    def add_to_list(self, filename, value):
        with open("gauti/employee.csv", "w",  newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = value.fieldnames())
            writer.writeheader()
            writer.writerow(value.add_to_dict())
        csvfile.close()


    

    