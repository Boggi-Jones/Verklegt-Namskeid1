class Employee(object):
    def __init__(self, name, ssn, adress, home_phone, gsm_phone, email, location, role):
        self.name = name
        self.ssn = ssn
        self.adress = adress
        self.home_phone = home_phone
        self.gsm_phone = gsm_phone
        self.email = email
        self.location = location
        self.role = role

    def __str__(self):
        pass