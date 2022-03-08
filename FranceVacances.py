from Catalog import Catalog

#Show Apartment Catalog content
cat = Catalog() #instance of the catalog
cat.ShowAparCatalog()

# adding a new apartment to the catalog usin catalog add method with parametere
# name,address,city, des, roomnr,weekprice 
# parameters can be read from a form or terminal prompt. 
      
cat.AddApartment("Danica", "Rue de apartment", "Nice", "Large and close to airport",2,55,4500)
print("*********show catalog again**********")
cat.ShowAparCatalog()

#Show Customer Catalog Content
print("****************customers*****************") 
cat.ShowCustomer()

#add customer
# first name, last name, age , Address, phone, email 
print("************* adding a customer and printing again ***********")
cat.AddCustomer("Hans", "Hansen", 40, "22334455", "abc@bbc.com")
cat.ShowCustomer()

#add a booking 
#start week, end week,customer, hotel
print("**********booking list content before Add********")
cat.ShowBookings()

print("**********booking list content after Add********")
cat.AddBooking(5,7,cat.GetApartment(3),cat.GetCustomer(0))
cat.ShowBookings()