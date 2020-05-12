# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: lbarcelo
"""

#import statements
from flask import Flask, render_template, url_for, redirect
from matplotlib.figure import Figure
from io import BytesIO
import pandas as pd
import numpy as np
import base64

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/crypto")
def crypto():
	return render_template("crypto.html")

@app.route("/NYCh20Consumption")
def waterConsump():
    return render_template("waterConsump.html")

@app.route("/consump")
def consump():
	return redirect("/210")

@app.route('/200')
def dataTable():
    df = pd.read_csv("/Users/lucabarcelo/Desktop/Dev/1006/final/Water_Consumption_In_The_New_York_City.csv")
    return render_template("dataT.html", tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route("/210")
def NYCWaterAnalysis():
    xr = pd.read_csv("/Users/lucabarcelo/Desktop/Dev/1006/final/Water_Consumption_In_The_New_York_City.csv") 
    total, year = xr['NYC Consumption(Million gallons per day)'], xr['Year']
    
    def give_me_the_straight_boi(x, y):
        w, b = np.polyfit(x,y,deg=1)
        line = w * x + b
        return line

    def give_me_change(x, y):
        w, b = np.polyfit(x,y,deg=1)
        return w
    
    change = give_me_change(year, total)
    line = give_me_the_straight_boi(year, total)
    
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

        
    buf = BytesIO()
    fig.savefig(buf, format="png")
    
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return "<img src='data:image/png;base64,{}'/>".format(data)

@app.route("/220")
def NYCWaterAnalysises():
    xr = pd.read_csv("/Users/lucabarcelo/Desktop/Dev/1006/final/Water_Consumption_In_The_New_York_City.csv") 
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
    xr = pd.read_csv("/Users/lucabarcelo/Desktop/Dev/1006/final/Water_Consumption_In_The_New_York_City.csv") 
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
