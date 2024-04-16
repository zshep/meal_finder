from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from sqlite3 import Error

# Configure application
app = Flask(__name__)

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect("mealFinder.db")
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"the error '{e}' occured")
    
    return connection


#home route
@app.route("/")
def index():
    #home route

    return render_template("index.html")

@app.route("/food", methods =["GET", "POST"] )
def food():
    if request.method == "GET":
        
        #grab the users meal items from DB

        #make variables to hold food info in order to be displayed on page
        return render_template("/food.html")
    else:
        new_food_item = request.form.get("foodname")
        is_vegan = request.form.get("vegan")
        is_vegetarian = request.form.get("vegetarian")
        dairy = request.form.get("dairy")
        glutonfree = request.form.get("gf")

        print("new food: ", new_food_item)
        print("is it vegan?", is_vegan)
        print("is it vegetarian?", is_vegetarian)
        print("does it have dairy?", dairy)
        print("is it gluton free? ", glutonfree)

        return render_template("/food.html")


@app.route("/jedi")
def jedi():
    return render_template("layout.html")


# log in



#register



# add food


#