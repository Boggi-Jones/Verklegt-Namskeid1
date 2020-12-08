from Logic.LogicMain import LogicMain
from Models.Contract import Contracts
from Models.Customer import Customer
from datetime import datetime

class ContractUI():
    def __init__(self):
        self.logic = LogicMain()

    def contract_loop(self):
        while True:
            choice = input('''\n -----------------------------------------------------------------------------
 | Welcome to NaN Air  -> Contracts                                          |
 -----------------------------------------------------------------------------
 | "Choose number to continue to next window"                                |
 | "Choose "4" to go back"                                                   |
 |                                                                           |
 | 1. Add contract                                                           |
 | 2. Remove contract                                                        |
 | 3. Update contract information                                            |
 | 4. See all contracts                                                      |
 | 5. Print contract                                                         |
 | 6. Charge contract                                                        |
 | 7 <- Go Back                                                              |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice: ''')

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
        ssn = input(" | Enter customer SSN: ")
        ssn_val = self.logic.customer(0, ssn, "ssn", None)
        if ssn_val == []:
            name = input(" | Name: ")
            ssn = input(" | SSN: ")
            email = input(" | Email: ")
            gsm_number = input(" | Phone: ")
            address = input(" | Address: ")
            driving_license = input(" | Drivers license: ")
            returned_late_before = input(" | Returned late before: ")
            new_customer = Customer(name, ssn, email, gsm_number, address, driving_license, returned_late_before)
            choice = input('''\n -----------------------------------------------------------------------------
 | -> -> Manage employee -> Add employee                                     |
 -----------------------------------------------------------------------------
 |                      "Customer information"                           |
 |Name:        {:59s}   |                                                  
 |SSN:         {:59s}   |
 |Email:       {:59s}   |
 |Cell phone:  {:59s}   |
 |Address:     {:59s}   |
 |License:     {:59s}   |
 |Late before: {:59s}   | 
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------'''.format(name, ssn, email, gsm_number, address, driving_license, returned_late_before)).lower()
            choice = input(" | Is the information correct (Y / N)? ")
            if choice == "y":
                self.logic.customer(1, new_customer, None, None)
                ssn_val = [new_customer]      
            else:
                return None, None
        else:
            choice = input("""\n -----------------------------------------------------------------------------
 | -> -> Manage employee -> Add employee                                     |
 -----------------------------------------------------------------------------
 |                      "New customer information"                           |
 |Name:        {:59s}   |                                                  
 |SSN:         {:59s}   |
 |Email:       {:59s}   |
 |Cell phone:  {:59s}   |
 |Address:     {:59s}   |
 |License:     {:59s}   |
 |Late before: {:59s}   | 
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------""".format(ssn_val[0].name, ssn_val[0].ssn, ssn_val[0].email, ssn_val[0].gsm_number, ssn_val[0].address, ssn_val[0].driving_license, ssn_val[0].returned_late_before)).lower()
            input("Is everything correct (Y / N)? ")
        vehicle_type = input("What type of vehicle does the customer want? ")
        list_of_vehicles = self.logic.vehicle(0, vehicle_type, "type_of_vehicle", None)
        for vehicle in list_of_vehicles:
            print(vehicle)
        number_plate = input("Enter the number plate of the chosen vehicle: ")
        while True:
            vehicle_class = self.logic.contract(4, ssn_val[0], number_plate, None, None)
            if vehicle_class == None:
                print("You don't have the required license for this vehicle.")
                number_plate = input("Enter the number plate of the chosen vehicle: ")
            else:
                choice = input("""------ You have chosen this car -----
        Type:             {}
        Model:            {}
        Rate:             {}
        Manufacturer:     {}
        Model year:       {}
        Color:            {}
        Is everything correct ? ( Y / N )
            """.format(vehicle_class[0].type_of_vehicle, vehicle_class[0].model, vehicle_class[0].rate, vehicle_class[0].manufacturer, vehicle_class[0].model_year, vehicle_class[0].color)).lower()
                if choice == "y":
                    break

        return ssn_val, vehicle_class

    def add_contract(self):
        customer_class, vehicle_class = self.the_customer()
        date = input("Pickup date: ")
        return_date = input("Return date: ")
        name_of_airport = input("Airport: ")
        employee_name = input("Employee name: ")
        duration = (datetime.strptime(return_date,'%d/%m/%Y') - datetime.strptime(date,'%d/%m/%Y')).days
        paid = "not"
        final_price = self.logic.contract(6, duration, None, None, vehicle_class)
        the_contract = Contracts(date, return_date, duration, name_of_airport, employee_name, paid, final_price, vehicle_class[0].number_plate, customer_class[0].ssn)
        print('''----------- Contract information ------------------
Date:                   {}
Return date:            {}
Duration:               {}
Name of airport:        {}
Employee name:          {}
Final price:            {}

------ Customer information -----
        Name:                   {}
        SSN:                    {}
        Email:                  {}
        Phone number:           {}
        Address:                {}
        Drivers license:        {}
        Returned late before:   {}

------ Vehicle information -----
        Type:             {}
        Model:            {}
        Rate:             {}
        Manufacturer:     {}
        Model year:       {}
        Color:            {}        
--------------------------------------------'''.format(date, return_date, duration, name_of_airport, employee_name, final_price, customer_class[0].name, customer_class[0].ssn, customer_class[0].email, customer_class[0].gsm_number, customer_class[0].address, customer_class[0].driving_license, customer_class[0].returned_late_before, vehicle_class[0].type_of_vehicle, vehicle_class[0].model, vehicle_class[0].rate, vehicle_class[0].manufacturer, vehicle_class[0].model_year, vehicle_class[0].color))
        choice = input("ARE YOU SURE YOU WANT TO SAVE INFO AND CONTINUE Y/N: ").lower()
        if choice == "y":
            self.logic.contract(1, None, None, the_contract, vehicle_class)
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
            the_removed_contract = self.logic.contract(3, contract_name, None, None, None)
            print("{} has been removed!".format(the_removed_contract))
        elif choice == "n":
            return
        else:
            return None

    def update_contract(self):
        while True:
            find_contract = input("Enter the contacts ssn: ")
            the_contract = self.logic.contract(0, find_contract, "ssn", None, None)
            try:
                print(the_contract[0])
            except IndexError:
                print("Contract not found, try again")
                continue
            choice = input("Is this the correct contract? Y/N").lower()
            if choice == "n":
                continue

            attribute = input('''--------------------------------------------
 What attribute would you like to change:
"""Contract information"""
 1. Pick up date:
 2. Drop off date:

"""Customer Information"""
 3. Phone:
 4. Email:
 5. Address:
 6. Driving license:

"""Vehicle Information"""
 7. Choose another vehicle:

--------------------------------------------
choice(Enter the number): ''')

            try:
                attribute = int(attribute)
            except ValueError:
                print("Wrong input")
                continue
            
            if attribute == 1 or attribute == 2:
                if attribute == 1:
                    attribute = "date"
                else:
                    attribute = "return_date"
                new_info = input("Enter new information: ")
                finished_product = self.logic.contract(2, find_contract, attribute, new_info, None)
            elif attribute < 7 and attribute > 2: 
                if attribute == 3:
                    attribute = "phone_number"
                elif attribute == 4:
                    attribute = "email"
                elif attribute == 5:
                    attribute = "address"
                else:
                    attribute = "driving_license"
                new_info = input("Enter new information: ")
                finished_product = self.logic.customer(3, find_contract, attribute, new_info)
            elif attribute == 7:
                attribute = "number_plate"
                vehicle_type = input("What type of vehicle does the customer want? ")
                list_of_vehicles = self.logic.vehicle(0, vehicle_type, "type_of_vehicle", None)
                for vehicle in list_of_vehicles:
                    print(vehicle)
                number_plate = input("Enter the number plate of the chosen vehicle: ")
                while True:
                    vehicle_class = self.logic.contract(4, the_contract[0], number_plate, None, None)
                    if vehicle_class == None:
                        print("You don't have the required license for this vehicle.")
                        number_plate = input("Enter the number plate of the chosen vehicle: ")
                    else:
                        choice = input("""------ You have chosen this car -----
        Type:             {}
        Model:            {}
        Rate:             {}
        Manufacturer:     {}
        Model year:       {}
        Color:            {}
        Is everything correct ? ( Y / N )
            """.format(vehicle_class[0].type_of_vehicle, vehicle_class[0].model, vehicle_class[0].rate, vehicle_class[0].manufacturer, vehicle_class[0].model_year, vehicle_class[0].color)).lower()
                        if choice == "y":
                            break
                
                finished_product = self.logic.contract(5, the_contract[0].number_plate, "number_plate", number_plate, None)

            else:
                print("Wrong input")
                continue
            
            print(finished_product)
            break

    def all_contracts(self):
        results = self.logic.contract(0, None, None, None, None)
        print('''\n ---------------------------------------------------------------------------------------------------------------------------------
 | -> Contracts -> All Contracts                                                                                        |
 ---------------------------------------------------------------------------------------------------------------------------------
 |  Date:         | Number:        | Location:      | Name:  | ?:     | Email:             | Location:  | Role:     |''')
        for contract in results:
            print(''' |  {}|'''.format(str(contract)))
        print(" ---------------------------------------------------------------------------------------------------------------------------------")
        input(" | Press 'Enter' to continue")

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