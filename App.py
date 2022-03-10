from flask import Flask
from flask import render_template
from datetime import datetime
from Catalog import Catalog
from Apartment import Apartment

app = Flask(__name__)
fv = Catalog()
@app.route("/")
def home():
    return " welcome to frans Vacancies: " + "time: " + str(datetime.now())

@app.route("/Apartments/")
def Apartments():
    allapar = " "
    for apar in fv.AparCatalog:
        allapar = allapar + apar.__str__() + "<br>"
    return allapar 

@app.route("/AddApartments/")
def AddApartment():
    fv.AddApartment("Danica", "Rue de apartment", "Nice", "Large and close to airport",2,55,4500)
    return Apartments()


app.run()
