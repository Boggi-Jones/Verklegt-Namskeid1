from Data.DataMain import DataMain

class CustomerLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Customer"

    def get_customer_with_id(self, ssn):
        # List of customers variable is created using get list function from datamain
        # Using a for loop iterating through list of customers, The customer variable is updated with customr if ssn attribute is found
        # The customer is then returned
        list_of_customers = self.datamain.get_list(self.position)
        the_customer = None
        for customer in list_of_customers:
            if customer.__getattribute__("ssn") == ssn:
                the_customer = customer
        
        return the_customer

    def add_customer_to_the_system(self, customer_class):
        # Customer is then added to list
        self.datamain.add_to_list(self.position, customer_class)

    def edit_customer(self, ssn, attribute, new_information):
        pass
