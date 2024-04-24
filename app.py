from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from db.db import get_db



# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#starting up sqlite db
cursor = get_db()


#creating login_requirement to view food pages
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function



#home route
@app.route("/")
@login_required
def index():
    #home route


    return render_template("index.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    # grab username and password from field
    username = request.form.get("name")
    password = request.form.get("password")

    if not username or not password:
        print("missing username or password")
        return render_template("error.html")
    
    #record the user name in session obejct 
    session["name"] = request.form.get("name")


    #redirect to main page
    return redirect("/")

@app.route("/logout")
def logout():
    #end session for username
    session.clear()

    return redirect("/")

@app.route("/register")
def register():

    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")

        #debugging
        print(username, password, confirm_password)

        #catching missing usernames or passwords
        if not username or not password or not confirm_password:
            #need to send error message to user
            print("missing field")
            return render_template("error.html")
        
        #catching miss matched passwords
        if password != confirm_password:
           #need to send error message to user
            print("passwords do not match")
            return render_template("error.html")     

        #grabbing all usernames to double check existance
        user_list = []
        user_names = cursor.execute("SELECT user_name FROM users")
        for user in user_names:
            user_list.append(user['user_name'])

        # checking if new username is unique in db
        if username in user_list:
            print("username already exists")
            return render_template("error.html")
        
        #hash password
        #TODO: use bcrypt or something to encript passwords


        #add in new user to db



        return render_template("/")


                


@app.route("/food", methods =["GET", "POST"] )
@login_required
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





# add food


#closing database connection: IS THIS PROPER?? to put it down here?
""" if connection:
        connection.close()
        print("SQL connection closed")
"""