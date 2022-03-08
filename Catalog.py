from Repository import Repository
from Apartment import Apartment
from Customer import Customer
from Booking import Booking
class Catalog(object):
    #AparCatalog = []
    def __init__(self):
        repo = Repository()
        self.AparCatalog = repo.MakeTestContent(3)
        self.CustomerCatalog=[] 
        self.BookingCatalog=[]

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
        
    def ShowBookings(self):
        for book in self.BookingCatalog:
            print(book.BookingDetail())

    def AddBooking(self,start,end,apar,cust):
        booking=Booking(len(self.BookingCatalog)+1, start,end,apar,cust)
        self.BookingCatalog.append(booking)

    def GetApartment(self, indexNr):
        return self.AparCatalog[indexNr]

    def GetCustomer(self, indexNr):
        return self.CustomerCatalog[indexNr]



