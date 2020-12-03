from Logic.LogicMain import LogicMain
from Models.Contract import Contracts

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

    def add_contract(self):
        print('''----------- Add contract ------------------
        """Insert information"""
Date:
Duration:
Country:
City:
Employee name:
Paid:
Final price:

--------------------------------------------''') # Þurfum að finna betri leið til að útfæra
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
 Enter contract name: {}


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
1. Date:
2. Duration:
3. Paid:

--------------------------------------------
chocie(Enter the number): ''')

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

    def charge_contact(self):