import User

class Customer(User.User):
    count_id=0
    def __init__(self,first_name, last_name, gender, membership, remarks, email, date_joined, address,contactby):
        super().__init__(first_name, last_name, gender, membership, remarks)
        Customer.count_id+=1
        self.__customer_id=Customer.count_id
        self.__email=email
        self.__date_joined=date_joined
        self.__address=address
        self.__contactby=contactby

    def get_customer_id(self):
        return self.__customer_id

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    def get_contactby(self):
        return self.__contactby

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_email(self, email):
        self.__email = email

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def set_address(self, address):
        self.__address = address

    def get_contactby_retrieve(self,contactby):
        contactlist=[]
        for contact in contactby:
            if contact=='P':
                contactlist.append("Phone")
            if contact=='E':
                contactlist.append("Email")
            if contact=='S':
                contactlist.append("SMS")
        str1= ", "
        return str1.join(contactlist)

    def set_contactby(self,contactby):
        self.__contactby=contactby
