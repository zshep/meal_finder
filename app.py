from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3


# Configure application
app = Flask(__name__)

#setting up sqlite database
try:
    connection = sqlite3.connect('foods.db', check_same_thread= False)
    cursor = connection.cursor()
    print("DB init")

#handling errors
except sqlite3.Error as error:
    print('Error Occured - ', error)

#home route
@app.route("/")
def index():
    #home route


    return render_template("index.html")

@app.route("/food", methods =["GET", "POST"] )
def food():
    if request.method == "GET":
        
        #grab the users meal items from DB
        foods = connection.cursor()

        foods.execute("SELECT * FROM recipes")

        for food in foods:
            print(food)

        #make variables to hold food info in order to be displayed on page
        return render_template("/food.html", foods)
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

        connection.execute("INSERT INTO recipes ?", new_food_item)

     

        return render_template("/food.html")


@app.route("/jedi")
def jedi():
    return render_template("layout.html")


# log in



#register



# add food


#closing database connection: IS THIS PROPER?? to put it down here?
""" if connection:
        connection.close()
        print("SQL connection closed")
"""