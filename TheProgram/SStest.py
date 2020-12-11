from Models.Employee import Employee
from Models.Location import Location
from Models.Vehicle import Vehicle
from Models.Contract import Contracts
from Models.Customer import Customer
from Models.Role import Role
employee = Employee()
model_dict = {"<class 'Models.Employee.Employee'>" : "Employee.csv", "<class 'Models.Location.Location'>" : "Location.csv", "<class 'Models.Vehicle.Vehicle'>" : "Vehicle.csv", "<class 'Models.Contract.Contracts'>" : "Contract.csv", "<class 'Models.Customer.Customer'>" : "Customer.csv", "<class 'Models.Role.Role'>" : "Role.csv"}
r = type(employee)
print(type(Location()))
print(type(Vehicle()))
print(type(Contracts()))
print(type(Customer()))
print(model_dict[str(type(Role()))])