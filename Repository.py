# repository to make static test apartment list
# or read list from file
# or render data from database. 
# 
from Apartment import Apartment

class Repository (object):
    AparList=[]
    def __init__(self):
        pass

    def MakeTestContent(self,antal):
        for i in range(antal):
            ap = Apartment(i, "Name"+str(i), "Address"+str(i), "City"+str(i), "Description"+ str(i),  i, i+50, i+4*i+20)
            self.AparList.append(ap)
        return self.AparList    