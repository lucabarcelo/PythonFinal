# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: lbarcelo
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

#start the server
if __name__ == "__main__":
    app.run()
