from Data.DataMain import DataMain

class CustomerLogic:
    def __init__(self):
        self.datamain = DataMain()
        self.position = "Customer"

    def get_list_of_customers(self, filter_or_id, attribute):
        ''' Gets a list of all customers from data. If there is no filter it just returns the full list.
        If there is a filter then it iterates through the list. It adds everything to a new list that has the filter in the chosen attribute.'''
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
        ''' Tells data to add this customer to the system'''
        self.datamain.add_to_list(self.position, customer_class)

    def remove_customer(self, filter_or_id):
        ''' Gets a list from get list of customers with all customers. Then iterates through the list and removes the customer with the given ssn.
        Then sends the rest of the list to data to rewrite everything without the removed customer.'''
        list_of_customers = self.get_list_of_customers(None, None)
        for customer in list_of_customers:
            if customer.ssn == filter_or_id:
                the_removed_contract = customer
                list_of_customers.remove(customer)
                self.datamain.overwrite(self.position, list_of_customers)
                return the_removed_contract

    def edit_customer(self, ssn, attribute, new_information):
        ''' Gets a list of one customer by filtering with the ssn and then changes the chosen attribute.
        Then it removes that customer from data and adds the updated one.'''
        single_customer = self.get_list_of_customers(ssn, "ssn")
        for customer in single_customer:
            customer.__setattr__(attribute, new_information)
            self.remove_customer(ssn)
            self.add_customer_to_the_system(customer)
        return single_customer[0]
