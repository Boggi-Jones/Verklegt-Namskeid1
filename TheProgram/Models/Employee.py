class Employee(object):
    def __init__(self, name = "", ssn = "", address = "", home_phone = "", gsm_phone = "", email = "", location = "", role = "", password = ""):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.home_phone = home_phone
        self.gsm_phone = gsm_phone
        self.email = email
        self.location = location
        self.role = role
        self.password = password

    def fieldnames(self):
        return ["name", "ssn", "address", "home_phone", "gsm_phone", "email", "location", "role", "password"]

    def add_to_dict(self):
        return {"name" : self.name, "ssn" : self.ssn, "address" : self.address, "home_phone": self.home_phone, "gsm_phone": self.gsm_phone, "email" : self.email, "location":self.location, "role": self.role, "password" : self.password}
    
    def __str__(self):
        return "{:^18s} | {:^11s} | {:^13s} | {:^12s} | {:^12s} | {:^18s} | {:^10s} | {:^8s} | {:^10s}".format(self.name, self.ssn, self.address, self.home_phone, self.gsm_phone, self.email, self.location, self.role, self.password)
