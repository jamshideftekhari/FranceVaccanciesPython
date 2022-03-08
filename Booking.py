# booking class
from typing_extensions import Self

class Booking (object):
    def __init__(self, id, start, end, totalprice, apar, customer):
        self.BookingId = id
        self.StartWeek = start
        self.EndWeek = end
        self.TotalPrice = totalprice
        self.Apartment = apar
        self.Customer = customer

    def CalculateWeek(self):
        return self.EndWeek - self.StartWeek    

    def CalculatePrice(self):
        return (self.EndWeek - self.StartWeek)*self.Apartment.WeekPrice    

    def BookingDetail(self):
        return "Booking Id: "+ self.BookingId+" Apartment Id: "+self.Apartment.AparId+" customer: "+ self.Customer.FName
