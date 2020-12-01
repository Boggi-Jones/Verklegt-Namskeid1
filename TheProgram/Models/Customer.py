class Customer(object):
    def __init__(self, name, ssn, email, gsm_number, adress, driving_license, returned_late_before):
        self.name = name
        self.ssn = ssn
        self.email = email
        self.gsm_number = gsm_number
        self.adress = adress
        self.driving_license = driving_license
        self.returned_late_before = returned_late_before

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self.name, self.ssn, self.email, self.gsm_number, self.adress, self.driving_license, self.returned_late_before)