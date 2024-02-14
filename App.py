from flask import Flask, redirect, url_for,jsonify, request
from flask import render_template
from datetime import datetime
from Catalog import Catalog
from Apartment import Apartment
import requests

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

@app.route("/AparTable")
def AparTable():
    return render_template("Apartments.html", apars=fv.AparCatalog)


@app.route("/AddApartments/")
def AddApartment():
    fv.AddApartment("Danica", "Rue de apartment", "Nice", "Large and close to airport",2,55,4500)
    return Apartments()

@app.route("/AddApar/", methods=['POST'])
def AddApar():
    fv.AddApartment(request.form['name'], request.form['address'], request.form['city'], request.form['desc'],int(request.form['room']),int(request.form['size']),int(request.form['price']))
    return redirect(url_for('AparTable'))   

@app.route('/CustomerTable')
def CustomerTable():
    return render_template("Customers.html", customers = fv.CustomerCatalog)

@app.route('/AddCustomer', methods=['POST']) 
def AddCustomers():
    fv.AddCustomer(request.form['fname'], request.form['lname'], request.form['age'], request.form['phone'], request.form['email']) 
    return redirect(url_for('CustomerTable'))  

@app.route('/ShowMap')
def ShowMap():
    return render_template("Map.html")


app.run()
 