class Role():
    def __init__(self, role = "", name = "", ssn = ""):
        self.role = role
        self.name = name
        self.ssn = ssn
        
    
    def fieldnames(self):
        return ["role", "name", "ssn"]
    
    def add_to_dict(self):
        return {"role" : self.role, "name" : self.name, "ssn" : self.ssn}
    
    def __str__(self):
        return "{:^25s} | {:^25s} | {:^25s}".format(self.role, self.name, self.ssn)
