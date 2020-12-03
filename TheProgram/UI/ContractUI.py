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
        ssn_val = self.logic.filtercustomer(ssn)
        if ssn_val == None:
            name = input("Name: ")
            ssn = input("SSN: ")
            email = input("Email: ")
            gsm_phone = input("Phone: ")
            address = input("Address: ")
            drivers_license = input("Drivers license: ")
            return_late_before = input("Returned late before: ")
            new_customer = Customer(name, ssn, phone, email, drivers_license)
        customer = input("""------ Customer information -----
        Name:                   {}
        SSN:                    {}
        Email:                  {}
        Phone number:           {}
        Address:                {}
        Drivers license:        {}
        Returned late before:   {}
        Is everything correct ? ( Y / N )
        """.format(name, ssn, email, gsm_phone, address, drivers_license, return_late_before)).lower
        if customer == "y":
            add_customer
        else:
            return
        vehicle_type = input("What type of vehicle does the customer want?")
        list_of_vehicles = self.logic.vehicle(0, vehicle_type, "vehicle type", None, None)
        for vehicle in list_of_vehicles:
            print(vehicle)
        number_plate = input("Enter the number plate of the chosen vehicle: ")
        vehicle_class = logic.contract.checklicense(tala, ssn_val, number_plate)
        if vehicle_class == None:
            print("Choose another vehicle, this one is occupied")
            number_plate = input("Enter the number plate of the chosen vehicle: ")
        else:
            break

        contract = Contracts(date, duration, country, city, employee_name, paid, final_price, vehicle_class, ssn_val)

    def add_contract(self):
        print('''----------- Add contract ------------------
        """Insert information"""
"""Contract Information"""
 Rental location:
 Creation of contract date:
 Employee who made contract:
 Pick up date:
 Drop of date:

"""Customer Information"""
 Customer id:
 Name:
 SSN:
 Phone:
 Email:
 Address:
 Drivers license:

 """Vehicle Information"""
 Plate number:


--------------------------------------------''')
        date = input("Date: ")
        duration = input("Duration: ")
        country = input("Country: ")
        city = input("City: ")
        employee_name = input("Employee name: ")
        the_contract = Contracts(date, duration, country, city, employee_name)

        print('''----------- Add employee ------------------
        """Insert information"""
Date:                   {}
Duration:               {}
Country:                {}
City:                   {}
Employee name:          {}

--------------------------------------------'''.format(date, duration, country, city, employee_name))
        choice = input("ARE YOU SURE YOU WANT TO SAVE INFO AND CONTINUE Y/N: ").lower()
        if choice == "y":
            self.logic.contract(1, None, None, the_contract)
        elif choice =="n":
            return
        else:
            return None

    def remove_contract(self):
        contract_name = input(""" ------- Remove contract ---------
 Enter contract name: <- Insert contract name






 --------------------------------------------""")
        choice = input("""# ------- Remove contract ---------
 Enter recipiants name of contract: {}


 |Are you sure you want to remove this contract?|
 | Y/N:__ |




 --------------------------------------------""".format(contract_name)).lower()
        if choice == "y":
            self.logic.contract(2, contract_name, None, None)
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
        customer_id = input("""------------- Print contract --------------

 Enter customer id:




 --------------------------------------------
 ID: """)
        print("""------------- Print contract --------------
#
# Enter customer id: 603-67-67
#
# """Contract information"""
# Rental location:
# Creation of contract date:
# Employee who made contract:
# Pick up date:
# Drop off date:
#
# """Customer information"""
# Name:
# SSN:
# Phone:
# Email:
# Address:
# Drivers license
#
# """Vehicle Information"""
# Manufacturer:
# Type:
# Color:
# Model
# Plate number:
# Vehicle rate:
#
#
#
# """Total cost"""
#
# ______________ $
#
#
#
# <- Back
# Choice:__
# -------------------------------------------""")

    def charge_contact(self):