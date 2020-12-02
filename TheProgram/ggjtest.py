from Data.DataMain import DataMain
from Models.Employee import Employee
i = Employee("f","f","f","f","f","f","f","f")
print(DataMain().get_list("Employee", i.fieldnames()))