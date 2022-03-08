# apartment class 
# properties:  Id, Name, Address, City, Description, RoomCount, Size, WeekPrice
# behaviors: To string() (__str__) to return a fomattet string of all properties.
#  

class Apartment (object):
    def __init__(self,id,name,address,city,description,roomnumber,size,weekprice):
        self.Id = id
        self.Name = name
        self.Address = address
        self.City = city
        self.Description = description
        self.RoomNumber = roomnumber
        self.Size = size
        self.WeekPrice = weekprice
    
    # to sting metod
    def __str__(self):
        return str(self.Id)+" "+self.Name+" "+self.Address+" "+self.City+" "+self.Description+" "+str(self.RoomNumber)+" "+str(self.WeekPrice)              
    