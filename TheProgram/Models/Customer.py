class Customer(object):
    def __init__(self, name, ssn, email, gsm_number, address, driving_license, returned_late_before):
        self.name = name
        self.ssn = ssn
        self.email = email
        self.gsm_number = gsm_number
        self.address = address
        self.driving_license = driving_license
        self.returned_late_before = returned_late_before

    def fieldnames(self):
        return ["name", "ssn", "email", "gsm_number", "address" , "driving_license", "return_late_before"]
    def add_to_dict(self):
        return {"name" : self.name, "ssn" : self.ssn, "email" : self.email, "gsm_number": self.gsm_number, "address" : self.address,  "driving_license":self.driving_license, "returned_late_before": self.returned_late_before}
    

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self.name, self.ssn, self.email, self.gsm_number, self.address, self.driving_license, self.returned_late_before)