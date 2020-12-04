from Data.DataMain import DataMain

class CustomerLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Customer"

    def get_list_of_customers(self, filter_or_id, attribute):
        # List of customers variable is created using get list function from datamain
        # Using a for loop iterating through list of customers, The customer variable is updated with customr if ssn attribute is found
        # The customer is then returned
        list_of_customers = self.datamain.get_list(self.position)
        the_customers = []
        if filter_or_id != None:
            for customer in list_of_customers:
                if customer.__getattribute__(attribute) == filter_or_id:
                    the_customers.append(customer)
            return the_customers
        else:    
            return list_of_customers

    def add_customer_to_the_system(self, customer_class):
        # Customer is then added to list
        self.datamain.add_to_list(self.position, customer_class)

    def remove_customer(self, filter_or_id):
        list_of_customers = self.get_list_of_customers(None, None)
        for customer in list_of_customers:
            if customer.ssn == filter_or_id:
                the_removed_contract = customer
                list_of_customers.remove(customer)
                self.datamain.overwrite(self.position, list_of_customers)
                return the_removed_contract

    def edit_customer(self, ssn, attribute, new_information):
        single_customer = self.get_list_of_customers(ssn, "ssn")
        new_customer = single_customer[0].__setattr__(attribute, new_information)
        self.remove_customer(ssn)
        self.add_customer_to_the_system(new_customer)
        return new_customer
