from Data.DataMain import DataMain

class EmployeeLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Employee"

    def filteremployees(self, filter_or_id, attribute):
        '''Takes in a filter and attribute '''
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
        list_of_employees = self.filteremployees(None, None)
        for emp in list_of_employees:
            if emp.__getattribute__("ssn") == filter_or_id:
                list_of_employees.remove(emp)
        self.datamain.overwrite(self.position, list_of_employees)

    def addemployee(self, new_information):
        self.datamain.add_to_list(self.position, new_information)

    def editemployeeinfo(self, filter_or_id, attribute, new_information):
        single_employee = self.filteremployees(filter_or_id, "ssn")
        for emp in single_employee:
            emp.__setattr__(attribute, new_information)
            self.removeemployee(filter_or_id)
            self.addemployee(emp)