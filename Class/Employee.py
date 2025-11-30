class Employee:

    def __init__(self,companyName,CompanyAddress,CompanyType):
        self.compName=companyName
        self.compAddr=CompanyAddress
        self.compType=CompanyType

    def getEmployeeDetails(self):
        print("Company Name- ",self.compName,
              "Company Address- ",self.compAddr,
              "Company Type- ",self.compType)



