from Logic.LogicMain import LogicMain

class ReportsUI():
    def __init__(self):
        self.logic = LogicMain()

    def reports_loop(self):
        """ Main menu loop for the reports UI which gives the option of seeing Income, Usage of vehicles and Contract for specified periods """
        while True:
            choice = input('''\n -----------------------------------------------------------------------------
 | Welcome to NaN Air  -> Buisness reports                                   |
 -----------------------------------------------------------------------------
 | "Choose number to continue to next window"                                |
 | "Choose "4" to go back"                                                   |
 |                                                                           |
 | 1. Income                                                                 |
 | 2. Usage of vehicles                                                      |
 | 3. Contracts by specified period                                          |
 | 4. <- Go Back                                                             |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 |                                                                           |
 -----------------------------------------------------------------------------
 | Choice: ''')
            if choice == "1":
                self.income()
            elif choice == "2":
                self.vehicle_usage()
            elif choice == "3":
                self.contracts_period()
            elif choice == "4":
                break
            else:
                print(" | Invalid choice!")
                input(" | Push enter to continue")

    def income(self):
        """ Prints out total income, income from different locations, income from different vehicles """
        print('''\n -----------------------------------------------------------------------------
 | -> Buisness reports -> Income                                             |
 -----------------------------------------------------------------------------''')
        
        start_date = input(" | Please select start date: ")
        while self.logic.input_checking(6, start_date) ==  False:
            print(" | Date must be in correct format: dd/mm/yyyy ")
            start_date = input(" | Please enter start date again: ")

        end_date = input(" | Please select end date: ")
        while self.logic.input_checking(6, end_date) ==  False:
            print(" | Date must be in correct format: dd/mm/yyyy ")
            end_date = input(" | Please enter end date again: ")

        print(" -----------------------------------------------------------------------------")
        total_income, location_income, vehicle_type_income = self.logic.reports(1, start_date, end_date)

        print(" | Total income over selected period is: ", total_income)
        print(" | ")
        print(" | Income from location: ")
        for key, value in location_income.items():
            print(" |\t{} : {}".format(key, value))
        print(" | ")
        print(" | Income from vehicle: ")
        for key, value in vehicle_type_income.items():
            print(" |\t{} : {}".format(key, value))
        print(" -----------------------------------------------------------------------------")
        input(" | Press 'Enter' to continue ")

    def vehicle_usage(self):
        """ Prints out total count for how many times each vehicle which has been rented out """
        print('''\n -----------------------------------------------------------------------------
 | -> Buisness reports -> Usage of vehicles                                  |
 -----------------------------------------------------------------------------''')
        results = self.logic.reports(2, None, None)

        for result in results:
            print(" | ",result[0].name_of_airport, ":")
            for key, value in result[1].items():
                print(" |     - {} : {}".format(key, value))
        print(" -----------------------------------------------------------------------------")
        input(" | Press 'Enter' to continue ")


    def contracts_period(self):
        """ Prints out person name and if they have paid or not for a specific period """
        print('''\n -----------------------------------------------------------------------------
 | -> Buisness reports -> Contracts by specified period                      |
 -----------------------------------------------------------------------------''')
        start_date = input(" | Please select start date: ")
        while self.logic.input_checking(6, start_date) ==  False:
            print(" | Date must be in correct format: dd/mm/yyyy ")
            start_date = input(" | Please enter start date again: ")

        end_date = input(" | Please select end date: ")
        while self.logic.input_checking(6, end_date) ==  False:
            print(" | Date must be in correct format: dd/mm/yyyy ")
            end_date = input(" | Please enter end date again: ")        
        
        print(" -----------------------------------------------------------------------------")

        results = self.logic.reports(3, start_date, end_date)
            
        print(" | Paid and unpaid contracts: ")
        for key, value in results.items():
            print(" | \t{} : {}".format(key, value))
        print(" -----------------------------------------------------------------------------")
        input(" | Press 'Enter' to continue ")