from Logic.LogicMaain import LogicMain
from Models.Reports import Reports

class ReportsUI():
    self.logic = LogicMain()

    def reports_loop(self):
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
        print('''\n -----------------------------------------------------------------------------
 | -> Buisness reports -> Income                                             |
 -----------------------------------------------------------------------------''')
        start_date = input(" | Please select start date: ")
        end_date = input(" | Please select end date: ")

        choice = input(''' | Please select either income by location or vehicle: 
 | 
 | 1. Total income
 | 2. Income by location
 | 3. Income by vehicle ''')
        if choice == "1":
            location_income = self.logic.reports(1, start_date, end_date)
            print(" | Total income is: {}".format(str(location_income[0])))
        elif choice == "2":
            location_income = self.logic.reports(1, start_date, end_date)
            for location in location_income[1]:
                print(" | Income by location is: {}".format(str(location)))
        elif choice == "3":
            location_income = self.logic.reports(1, income_period, None, None)
            for vehicle in location_income[2]:
                print(" | Income by vehicle is: {}".format(str(vehicle)))
        else:
            print(" | Invalid input, please choose again")


    def vehicle_usage(self):
        print('''\n -----------------------------------------------------------------------------
 | -> Buisness reports -> Usage of vehicles                                  |
 -----------------------------------------------------------------------------''')
        vehicle_location = input(" | Please select location for vehicle overview: ")
        results = self.logic.reports(2, None, None)
        for key, value in results:
            print(key, value)


    def contracts_period(self):
        print('''\n -----------------------------------------------------------------------------
 | -> Buisness reports -> Contracts by specified period                      |
 -----------------------------------------------------------------------------''')
        start_date = input(" | Please select start date: ")
        end_date = input(" | Please select end date: ")
        results = self.logic.reports(3, start_date, end_date)
        for key, value in results:
            print(key, value)

