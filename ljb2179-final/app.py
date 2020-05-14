# -*- coding: utf-8 -*-
"""
by | Luca Barcelo ljb2179 |
Columbia University | Engi1006 | Spring 2020
Final - App V.1.0
"""

#import statements
from flask import Flask, render_template, url_for, redirect, request
from matplotlib.figure import Figure
from io import BytesIO
import pandas as pd
import numpy as np
import base64
import hashlib

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def index():
	return render_template("index.html")

#get method for displaying crypto.html page, post for displaying cracked.html
@app.route("/crypto", methods=["GET", "POST"])
def crypto():
    #run if form is submitted
    if request.method == "POST":
	#grab user input from html form
        InputWord = request.form["word"]
	#convert word to SHA1 hashed string
        HshInWrd = hashlib.sha1(bytes(InputWord, 'utf-8')).hexdigest()
	#return that hashed string in the Cracked.html page
        return render_template('Cracked.html', HshInWrd=HshInWrd)
    #if no form submitted, return crypto.html
    return render_template("crypto.html")

#get method for displaying crypto2.html page, post for displaying cracked2.html
@app.route("/UnhashCrypto", methods=['GET','POST'])
def UnhashIt():
    if request.method == 'POST':
	#grab input hash from form submission
        InputHash = request.form["hash"]
	#open list of strings
        OCompList = open('500k.txt', 'r')
	#read and split so I can pass into for loop on a per string basis
        CompList = OCompList.read().split('\n')

        for word in CompList:
	    #encode each string 
            encwrd = word.encode('utf-8')
	    #hash each string in my list of string combos into SHA1
            HashOutWord = hashlib.sha1(encwrd).hexdigest()
   	    #compare hashed string from list to user input hashed string
            if HashOutWord == InputHash:
		#render cracked2.html with the specific word in the list of strings that 
		#corresponds to HashOutWord when HashOutWord equals InputHash
                return render_template('Cracked2.html', word=word)
    #render crypto2.html if it's GET method is called
    return render_template('crypto2.html')

@app.route("/NYCh20Consumption")
def waterConsump():
    return render_template("waterConsump.html")

#read input NYC water consump data and return it as an html table
@app.route('/200')
def dataTable():
    df = pd.read_csv("Water_Consumption_In_The_New_York_City.csv")
    return render_template("dataT.html", tables=[df.to_html(classes='data')], titles=df.columns.values)

#read input NYC water consump data and return a matplotlib graph
@app.route("/210")
def NYCWaterAnalysis():
    xr = pd.read_csv("Water_Consumption_In_The_New_York_City.csv")
    #extract data I want from csv file
    total, year = xr['NYC Consumption(Million gallons per day)'], xr['Year']
    
    #helper functions defined inside for graph viewing 
    def give_me_the_straight_boi(x, y):
        w, b = np.polyfit(x,y,deg=1)
        line = w * x + b
        return line

    #gives rate of change for label viewing of rate of change
    def give_me_change(x, y):
        w, b = np.polyfit(x,y,deg=1)
        return w

    change = give_me_change(year, total)
    line = give_me_the_straight_boi(year, total)

    #plot my matplotlib figure 
    fig = Figure()
    ax = fig.subplots()
    ax.scatter(year, line, s=5, color='red', label="40-Year Average \n Total Consumption \n Rate Change:\n  {} Million Gallons".format(round(change, 2)))
    ax.plot(year, total)
    ax.legend()

    ax.set_xlim(1978,2020)
    ax.set_ylim(700, 2000)
    ax.set_xlabel('Year')
    ax.set_ylabel('Daily Consumption per Millions of Gallons')
    ax.set_title('40-Year NYC H2O Consumption')

    #converts plot from figure.IO to renderable fig
    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return "<img src='data:image/png;base64,{}'/>".format(data)

@app.route("/220")
def NYCWaterAnalysises():
    xr = pd.read_csv("Water_Consumption_In_The_New_York_City.csv")
    percap, year = xr['Per Capita(Gallons per person per day)'], xr['Year']

    def give_me_the_straight_boi(x, y):
        w, b = np.polyfit(x,y,deg=1)
        line = w * x + b
        return line

    def give_me_change(x, y):
        w, b = np.polyfit(x,y,deg=1)
        return w

    change = give_me_change(year, percap)
    line = give_me_the_straight_boi(year, percap)

    fig = Figure()
    ax = fig.subplots()
    ax.scatter(year, line, s=5, color='red', label="40-Year Average \n Individual Consumption \n Rate Change:\n  {} Million Gallons".format(round(change, 2)))
    ax.plot(year, percap)
    ax.legend()

    ax.set_xlim(1978,2020)
    ax.set_ylim(50, 250)
    ax.set_xlabel('Year')
    ax.set_ylabel('Daily Percap Consumption (Gallons)')
    ax.set_title('40-Year NYC H2O Consumption')


    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return "<img src='data:image/png;base64,{}'/>".format(data)

@app.route("/230")
def NYCWaterAnalysiseses():
    xr = pd.read_csv("Water_Consumption_In_The_New_York_City.csv")
    percap, populat = xr['Per Capita(Gallons per person per day)'], xr['New York City Population']

    def give_me_the_straight_boi(x, y):
        w, b = np.polyfit(x,y,deg=1)
        line = w * x + b
        return line

    def give_me_change(x, y):
        w, b = np.polyfit(x,y,deg=1)
        return w

    changePer = give_me_change(populat, percap)
    #changeTot = give_me_change(populat, total)
    linePer = give_me_the_straight_boi(populat, percap)
    #lineTot = give_me_the_straight_boi(populat, total)

    fig = Figure()
    ax = fig.subplots()
    ax.scatter(populat, linePer, s=5, color='red', label="For Each Person\nAdded to NYC:\n{} per-Capita Gallon change".format(round(changePer, 5)))
    ax.plot(populat, percap)
    ax.legend()

    ax.set_xlim(7000000, 8500000)
    ax.set_ylim(50, 250)
    ax.set_xlabel('Population')
    ax.set_ylabel('Daily Percap Consumption (Gallons)')
    ax.set_title('40-Year NYC H2O Consumption')


    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return "<img src='data:image/png;base64,{}'/>".format(data)

#start the server
if __name__ == "__main__":
    app.run()

