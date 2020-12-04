from Logic.LogicMain import LogicMain
from Models.Contract import Contracts
from Models.Customer import Customer

class ContractUI():
    def __init__(self):
        self.logic = LogicMain()

    def contract_loop(self):
        while True:
            choice = input("""# --------------- Contracts -------------------
 1. Add contract
 2. Remove contract
 3. Update contract information
 4. See all contracts
 5. Print contract
 6. Charge contract
 7. <-- Go Back

    choice: """)

            if choice == "1":
                self.add_contract()
            elif choice == "2":
                self.remove_contract()
            elif choice == "3":
                self.update_contract()
            elif choice == "4":
                self.all_contracts()
            elif choice == "5":
                self.print_contract()
            elif choice == "6":
                self.charge_contact()
            elif choice == "7":
                break
            else:
                print("Invalid choice!")

    def the_customer(self):
        ssn = input("Enter customer SSN: ")
        ssn_val = self.logic.customer(0, ssn)
        if ssn_val == None:
            name = input("Name: ")
            ssn = input("SSN: ")
            email = input("Email: ")
            gsm_number = input("Phone: ")
            address = input("Address: ")
            drivers_license = input("Drivers license: ")
            return_late_before = input("Returned late before: ")
            new_customer = Customer(name, ssn, email, gsm_number, address, drivers_license, return_late_before)
            choice = input("""------ Customer information -----
        Name:                   {}
        SSN:                    {}
        Email:                  {}
        Phone number:           {}
        Address:                {}
        Drivers license:        {}
        Returned late before:   {}
        Is everything correct ? ( Y / N )
            """.format(name, ssn, email, gsm_number, address, drivers_license, return_late_before)).lower()
            if choice == "y":
                self.logic.customer(1, new_customer)
                ssn_val = new_customer      
            else:
                return None, None
        else:
            choice = input("""------ Customer information -----
        Name:                   {}
        SSN:                    {}
        Email:                  {}
        Phone number:           {}
        Address:                {}
        Drivers license:        {}
        Returned late before:   {}
        Is everything correct ? ( Y / N )
            """.format(ssn_val.name, ssn_val.ssn, ssn_val.email, ssn_val.gsm_number, ssn_val.address, ssn_val.drivers_license, ssn_val.return_late_before)).lower()
        
        vehicle_type = input("What type of vehicle does the customer want? ")
        list_of_vehicles = self.logic.vehicle(0, vehicle_type, "type_of_vehicle", None)
        for vehicle in list_of_vehicles:
            print(vehicle)
        number_plate = input("Enter the number plate of the chosen vehicle: ")
        while True:
            vehicle_class = self.logic.contract(5, ssn_val, number_plate, None, None)
            if vehicle_class == None:
                print("You don't have the required license for this vehicle.")
                number_plate = input("Enter the number plate of the chosen vehicle: ")
            else:
                break
        return ssn_val, vehicle_class

    def add_contract(self):
        customer_class, vehicle_class = self.the_customer()
        print('''----------- Add contract ------------------
        """Insert information"""
"""Contract Information"""
 Date:
 Duration:
 Country:
 City:
 Employee name:
 Paid:
 Final price:

"""Customer Information"""
 Name:
 SSN:
 Phone:
 Email:
 Address:
 Drivers license:

 """Vehicle Information"""
 #vehicle class...:
 Plate number:


--------------------------------------------''')
        date = input("Date: ")
        duration = input("Duration: ")
        name_of_airport = input("Airport: ")
        employee_name = input("Employee name: ")
        paid = "not"
        final_price = self.logic.contract(6, duration, None, None, vehicle_class)
        the_contract = Contracts(date, duration, name_of_airport, employee_name, paid, final_price, vehicle_class[0].number_plate, customer_class.ssn)
        print('''----------- Contract information ------------------
Date:                   {}
Duration:               {}
Name of airport:        {}
Employee name:          {}
Final price:            {}

--------------------------------------------'''.format(date, duration, name_of_airport, employee_name, final_price))
        choice = input("ARE YOU SURE YOU WANT TO SAVE INFO AND CONTINUE Y/N: ").lower()
        if choice == "y":
            self.logic.contract(1, None, None, the_contract, None)
        elif choice =="n":
            return
        else:
            return None

    def remove_contract(self):
        contract_name = input(""" ------- Remove contract ---------
 Enter contractholder name: <- Insert contract name






 --------------------------------------------""")
        choice = input("""# ------- Remove contract ---------
 Contractholder: {}


 |Are you sure you want to remove this contract?|
 | Y/N:__ |




 --------------------------------------------""".format(contract_name)).lower()
        if choice == "y":
            self.logic.contract(3, contract_name, None, None, None)
            print("{} has been removed!".format(contract_name))
        elif choice == "n":
            return
        else:
            return None

    def update_contract(self):
        while True:
            find_contract = input("Enter contract recipient: ")
            attribute = input('''--------------------------------------------
 What attribute would you like to change:
"""Contract information"""
 1. Rental location:
 2. Pick up date:
 3. Drop off date:

"""Customer Information"""
 4. Phone:
 5. Email:
 6. Address:

"""Vehicle Information"""
 7. Plate number:

--------------------------------------------
choice(Enter the number): ''')

            if attribute == "1":
                attribute = "date"
            elif attribute == "2":
                attribute = "duration"
            elif attribute == "3":
                attribute = "paid"
            else:
                print("Wrong input")
                continue
            new_info = input("Enter new information: ")
            self.logic.contract(3, find_contract, attribute,  new_info)
            break

    def all_contracts(self):
        results = self.logic.contract(0, None, None, None)
        print("\n------- All locations ---------- ")
        for contract in results:
            print(contract)
        print("-----------------------------------")

    def print_contract(self):
        customer_id = print(''' ------------- Print contract --------------

 """Contract Information"""
 Date:
 Duration:
 Country:
 City:
 Employee name:
 Paid:
 Final price:

"""Customer Information"""
 Name:
 SSN:
 Phone:
 Email:
 Address:
 Drivers license:

 """Vehicle Information"""
 Manufacturer:
 Type:
 Color:
 Model
 Plate number:
 Vehicle rate:

 """Total cost"""
 Cost:
 
 Enter Customer ID: ''')

        printable_customer = self.logic.contract(4, customer_id, None, None)
        for item in printable_customer:
            print(item)

    def charge_contact(self):
        pass