from UI.UIMain import UIMain
from Logic.LogicMain import LogicMain


class FleetUI():
    def __init__(self):
        self.uimain = UIMain()
        self.logic = LogicMain()

    def fleet_loop(self):
        ''' Skv. wireframe. Valmynd fyrir UIFleet - klasann. Út frá þessu er hægt
        að fara í "Manage employee, All employees o.s.frv." '''

        while True:
            fleet_choice = input(''' ----------- Manage vehicle fleet ------------
1. Edit vehicle
2. All vehicles

3. <- Go back 
--------------------------------------------
chocie: ''')
        if fleet_choice == "1":
            edit_vehicle()
        elif fleet_choice == "2":
            all_vehicles()
        elif fleet_choice == "3":
            self.uimain
        else:
            ("Invalid entry")


    def edit_vehicle():
        edit_choice = input(''' ----------- Edit Vehicle ------------------
1. Add vehicle
2. Remove vehicle
3. Update vehicle information
4. Update Vehicle condition
5. <- Go back

--------------------------------------------
chocie: ''')
        while True:
            if edit_choice == "1":
                add_vehicle()
            elif edit_choice == "2":
                remove_vehicle()
            elif edit_choice == "3":
                update_vehicle_information()
            elif edit_choice == "4":
                update_vehicle_condition()
            elif edit_choice == "4":
                flee_loop()
            else:
                ("Invalid entry")
    

    def all_vehicles():
        pass

