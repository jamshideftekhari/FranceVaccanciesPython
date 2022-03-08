from Repository import Repository
from Apartment import Apartment
from Customer import Customer
class Catalog(object):
    #AparCatalog = []
    def __init__(self):
        repo = Repository()
        self.AparCatalog = repo.MakeTestContent(3)
        self.CustomerCatalog=[] 

    def ShowAparCatalog(self):
        for apar in self.AparCatalog:
            print(apar)   

    def AddApartment(self, name,address,city,des,roomnr,size,weekprice):
        apr = Apartment(len(self.AparCatalog)+1,name,address,city, des, roomnr,size, weekprice)
        self.AparCatalog.append(apr)

    def ShowCustomer(self):
        for cus in self.CustomerCatalog:
            print(cus)

    def AddCustomer(self,fname,lname,age,phone,email):
        customer = Customer(len(self.CustomerCatalog)+1, fname, lname, age, phone, email)
        self.CustomerCatalog.append(customer)
        

