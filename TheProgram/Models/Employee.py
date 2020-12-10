class Employee(object):
    def __init__(self, name, ssn, address, home_phone, gsm_phone, email, location, role):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.home_phone = home_phone
        self.gsm_phone = gsm_phone
        self.email = email
        self.location = location
        self.role = role

    def fieldnames(self):
        return ["name", "ssn", "address", "home_phone", "gsm_phone", "email", "location", "role"]

    def add_to_dict(self):
        return {"name" : self.name, "ssn" : self.ssn, "address" : self.address, "home_phone": self.home_phone, "gsm_phone": self.gsm_phone, "email" : self.email, "location":self.location, "role": self.role}
    
    def __str__(self):
        return "{:^18s} | {:^11s} | {:^13s} | {:^12s} | {:^12s} | {:^18s} | {:^10s} | {:^8s}".format(self.name, self.ssn, self.address, self.home_phone, self.gsm_phone, self.email, self.location, self.role)

class Role(Employee):
    def __init__(self, role, name, ssn):
        self.role = role
        self.emp = name
        self.SSN = ssn
    
    def fieldnames(self):
        return ["role", "name", "ssn"]
    
    def add_to_dict(self):
        return {"role" : self.role, "name" : self.emp, "ssn" : self.SSN}
    
    def __str__(self):
        return "{:^25s} | {:^25s} | {:^25s}".format(self.role, self.emp, self.SSN)
