# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: lbarcelo
"""
#import statements
from flask import Flask, render_template, url_for, redirect, request
import banna

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/1006")
def testing1():
	return render_template("engi.html")

@app.route("/test")
def testing2():
	return banna.bannality()

@app.route("/210")
def redirtest():
    return redirect("/1006")

#start the server
if __name__ == "__main__":
    app.run()

