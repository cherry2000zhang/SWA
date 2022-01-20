class Company:
    count_id=0

    def __init__(self,company_id, company_name):
        Company.count_id+=1
        self.__company_id=company_id
        self.__companyname=company_name

    def get_company_id(self):
        return self.__company_id

    def get_companyname(self):
        return self.__companyname

    def set_companyname(self, company_name):
        self.__companyname = company_name

    def set_company_id(self, company_id):
        self.__company_id = company_id

