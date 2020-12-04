from Data.DataMain import DataMain

class EmployeeLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Employee"

    def filteremployees(self, filter_or_id, attribute):
        # List of employees is gathered from get list function in data main
        # If filter or id doesn´t match None if loop is used to iterate through lit of employees
        # If emp matches with filter or id they are added to retlist
        # Retlist is then returned
        # Else List of employees is returned
        list_of_employees = self.datamain.get_list(self.position)
        retlist = []
        if filter_or_id != None:
            for emp in list_of_employees:
                if emp.__getattribute__(attribute) == filter_or_id:
                    retlist.append(emp)
            return retlist
        else:
            return list_of_employees

    def removeemployee(self, filter_or_id):
        # List of employees is gathered from filter employees function
        # If ssn attribute for emp matches filter or id
        # Employee is removed from list of employess
        # List of employees is then overwritten with updated list
        list_of_employees = self.filteremployees(None, None)
        for emp in list_of_employees:
            if emp.ssn == filter_or_id:
                list_of_employees.remove(emp)
        self.datamain.overwrite(self.position, list_of_employees)

    def addemployee(self, new_information):
        # New employee is added to list
        self.datamain.add_to_list(self.position, new_information)

    def editemployeeinfo(self, filter_or_id, attribute, new_information):
        # Single employee variable is created using filteremployee funtiong and ssn attribute to identifie uniqr emploee)
        # employee is then updated by using new_information attribute
        # remove employee and add employee functions are then called and updated
        single_employee = self.filteremployees(filter_or_id, "ssn")
        for emp in single_employee:
            emp.__setattr__(attribute, new_information)
            self.removeemployee(filter_or_id)
            self.addemployee(emp)
