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
        income_period = input('''\n -----------------------------------------------------------------------------
 | -> Buisness reports -> Income                                             |
 -----------------------------------------------------------------------------
 | Please select the period you wish to see the income for(dd/mm/yyyy-dd/mm/yyyy):  ''')
        choice = input(''' | Please select either income by location or vehicle: 
 | 
 | 1. Income by location
 | 2. Income by vehicle      
        ''')
            if choice == "1":
                location_income = self.logic.reports(tala, income_period, None, None)
                for location in location_income:
                    print(" | Income by location is: ")
            elif choice == "2":
                location_income = self.logic.reports(tala, income_period, None, None)
                for vehicle in location_income:
                    print(" | Income by vehicle is: ")
            else:
                print(" | Invalid input, please choose again")


    def vehicle_usage(self):
        pass


    def contracts_period(self):
        pass




