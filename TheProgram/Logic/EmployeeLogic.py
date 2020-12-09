from Data.DataMain import DataMain

class EmployeeLogic:
    def __init__(self):
        self.rolelogic = RoleLogic()
        self.datamain = DataMain()
        self.position = "Employee"

    def filter_employees(self, filter_or_id, attribute):
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

    def remove_employee(self, filter_or_id):
        # List of employees is gathered from filter employees function
        # If ssn attribute for emp matches filter or id
        # Employee is removed from list of employess
        # List of employees is then overwritten with updated list
        list_of_employees = self.filter_employees(None, None)
        for emp in list_of_employees:
            if emp.ssn == filter_or_id:
                list_of_employees.remove(emp)
        self.datamain.overwrite(self.position, list_of_employees)
        self.rolelogic.remove_employee(emp)

    def add_employee(self, new_information):
        # New employee is added to list
        self.datamain.add_to_list(self.position, new_information)

    def edit_employee_info(self, filter_or_id, attribute, new_information):
        # Single employee variable is created using filteremployee funtiong and ssn attribute to identifie uniqr emploee)
        # employee is then updated by using new_information attribute
        # remove employee and add employee functions are then called and updated
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
    
    def role_list(self, role, attribute):
        '''Get list of roles and associated employees with them'''
        list_of_roles = self.datamain.get_list(self.position)
        return list_of_roles
    
    def add_employee(self, attributes):
        '''when employee is added to employees file, they also get added with their role in role file'''
        self.datamain.add_to_list(self.position, attributes)
        
        
    def remove_employee(self, attribute):
        '''removed employee is either fired or given a new role''' 
        role_list_ssn = self.role_list(None, attribute)
        for ssn in role_list_ssn:
            if ssn.__getattribute__(attribute) == attribute:
                self.datamain.overwrite(self.position, ssn)

           