#customer class
# properties : FName, LName, PhoneNr, Email
# Behavior: return properties
# 

class Customer (object):
    def __init__(self, id, fname, lname, age, phone, email):
        self.Id = id
        self.FName = fname
        self.LName = lname
        self.Age = age
        self.PhoneNr = phone
        self.Email = email

    def __str__(self):
        return str(self.Id) + " " +self.FName+" "+self.LName+" "+str(self.Age)+" "+self.PhoneNr+" "+self.Email      
