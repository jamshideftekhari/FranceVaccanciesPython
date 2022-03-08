# booking class


class Booking (object):
    def __init__(self, id, start, end,  apar, customer):
        self.BookingId = id
        self.StartWeek = start
        self.EndWeek = end
        self.Apartment = apar
        self.TotalPrice = self.CalculatePrice()
        self.Customer = customer

    def CalculateWeek(self):
        return self.EndWeek - self.StartWeek    

    def CalculatePrice(self):
        return self.CalculateWeek()*self.Apartment.WeekPrice    

    def BookingDetail(self):
        return "Booking Id: "+ str(self.BookingId)+" Apartment Id: "+ str(self.Apartment.Id)+" customer: "+ self.Customer.FName
