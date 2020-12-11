from Data.DataMain import DataMain
from Models.Role import Role

class RoleLogic:
    
    def __init__(self):
        self.datamain = DataMain()
    
    def role_list(self, filter_or_id, attribute):
        '''Get list of roles and associated employees with them'''
        list_of_roles = self.datamain.get_list(Role())
        retList = []
        if attribute != None:
            for emp in list_of_roles:
                if emp.__getattribute__(attribute) == filter_or_id:
                    retList.append(emp)
            return retList
        else:
            for i in list_of_roles:
                retList.append(i)
            return retList
    
    def add_employee(self, new_information):
        '''when employee is added to employees file, they also get added with their role in role file'''
        self.datamain.add_to_list(new_information)
        
    def remove_employee(self, filter_or_id):
        '''removed employee is either fired or given a new role''' 
        role_list_ssn = self.role_list(None, None)
        for s in role_list_ssn:
            if s.ssn == filter_or_id:
                role_list_ssn.remove(s)
        self.datamain.overwrite(role_list_ssn, Role())

    def edit_company_role(self, filter_or_id, attribute, new_information):
        single_employee = self.role_list(filter_or_id, "ssn")
        for emp in single_employee:
            emp.__setattr__(attribute, new_information)
            self.remove_employee(filter_or_id)
            self.add_employee(emp)