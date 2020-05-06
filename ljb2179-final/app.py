# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: lbarcelo
"""
#import statements
from flask import Flask, render_template, url_for, redirect

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/crypto")
def crypto():
	return render_template("crypto.html")

@app.route("/airPollution")
def airPollution():
	return render_template("pollution.html")

@app.route("/210")
def redirtest():
    return redirect("/")

#start the server
if __name__ == "__main__":
    app.run()

