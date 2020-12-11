from Data.DataMain import DataMain

class EmployeeLogic:
    def __init__(self):
        self.rolelogic = RoleLogic()
        self.datamain = DataMain()
        self.position = "Employee"

    def filter_employees(self, filter_or_id, attribute):
        ''' Gets a list of all employees from data. If there is no filter it just returns the full list.
        If there is a filter then it iterates through the list. It adds everything to a new list that has the filter in the chosen attribute.'''
        list_of_employees = self.datamain.get_list(self.position)
        retlist = []
        if filter_or_id != None:
            for emp in list_of_employees:
                if emp.__getattribute__(attribute) == filter_or_id:
                    retlist.append(emp)
            return retlist
        else:
            return list_of_employees

    def remove_employee(self, filter_or_id):
        ''' Gets a list from filter employee of all employees. Then iterates through the list and removes the employee with the given ssn.
        Then sends the rest of the list to data to rewrite everything without the removed employee.'''
        list_of_employees = self.filter_employees(None, None)
        for emp in list_of_employees:
            if emp.ssn == filter_or_id:
                list_of_employees.remove(emp)
        self.datamain.overwrite(self.position, list_of_employees)
        

    def add_employee(self, new_information):
        ''' Tells data to add this employee to the system'''
        self.datamain.add_to_list(self.position, new_information)
         

    def edit_employee_info(self, filter_or_id, attribute, new_information):
        ''' Gets a list of one employee by filtering with the ssn and then changes the chosen attribute.
        Then it removes that employee from data and adds the updated one.'''
        single_employee = self.filter_employees(filter_or_id, "ssn")
        for emp in single_employee:
            emp.__setattr__(attribute, new_information)
            self.remove_employee(filter_or_id)
            self.add_employee(emp)

        return single_employee[0]

    def change_employee_name(self, filter_or_id, emp_name):
        '''When names added in the system are too long the surname/lastname are cut to first alpha character'''
        the_emp = self.filter_employees(filter_or_id, "ssn")
        # get a list of employee attributes and take name attribute
        # then split every character by commas
        emp_name = str(the_emp[0])
        emp_name = tuple(emp_name)
        emp_name = list(emp_name) # name split into single char to list
        if ' ' in emp_name: # Where first name is separated
            index = emp_name.index(' ')
            del emp_name[index+2:]
            emp_name[-1] = emp_name[-1].capitalize()+"." 
            emp_name = ''.join(emp_name)
        self.edit_employee_info(filter_or_id, "name", emp_name) 
        #employee is first added to the system from input and then checked 
        

class RoleLogic:
    
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Role"
    
    def role_list(self, filter_or_id, attribute):
        '''Get list of roles and associated employees with them'''
        list_of_roles = self.datamain.get_list(self.position)
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
        self.datamain.add_to_list(self.position, new_information)
        
    def remove_employee(self, filter_or_id, attribute):
        '''removed employee is either fired or given a new role''' 
        role_list_ssn = self.role_list(None, None)
        for s in role_list_ssn:
            if s.ssn == filter_or_id:
                role_list_ssn.remove(s)
        self.datamain.overwrite(self.position, role_list_ssn)

           