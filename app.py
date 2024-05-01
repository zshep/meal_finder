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
    #grab users info
    user_name = session['name']
    user_id = session['user_id']
    print(user_name, user_id)




    return render_template("index.html", user_name = user_name)

@app.route("/login", methods = ["GET","POST"])
def login():
    # GET Route
    if request.method == "GET":
        return render_template("login.html")
    
    #handling POST Route
    #Forget an user
    session.clear()

    # grab username and password from field
    username = request.form.get("name")
    password = request.form.get("password")
    print(username)
    print(password)

       
    if not username or not password:
        print("missing username or password")
        return render_template("error.html")
    
    #starting up sqlite db and creating cursor
    cursor = get_db().cursor()
        
    
    #checking username in to confirm password
    res = cursor.execute("SELECT personid, hash FROM users WHERE user_name == ?", [username])

    
    user_check = res.fetchall()

    #debugging
    #print(user_check)
    #print(user_check[0])
    #print(user_check[0][1])
    
    

    if not user_check:
        print("username not found")
        return render_template("error.html")
    
    #check if password matches
    if not check_password_hash(user_check[0][1], password):
        print("password is not correct")
        return render_template("error.html")


    #record the user id in session obejct 
    session["user_id"] = user_check[0][0]
    session["name"] = request.form.get("name")


    #redirect to main page
    return redirect("/")

@app.route("/logout")
def logout():
    #end session for username
    session.clear()

    return redirect("/")

@app.route("/register", methods= ["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")
    else:
             
        user_name = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")

        #debugging
        print(user_name, password, confirm_password)

        #catching missing usernames or passwords
        if not user_name or not password or not confirm_password:
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
               
        #starting up sqlite db and creating cursor
        db = get_db()
        cursor = db.cursor()

        res = cursor.execute("SELECT user_name FROM users")
        user_names = res.fetchall()
        print(user_names)

        for user in user_names:
            user_list.append(user[0])

        print(user_list)
        # checking if new username is unique in db
        if user_name in user_list:
            print("username already exists")
            return render_template("error.html")
        
        #hash password
        hash = generate_password_hash(password)
        print(hash)
        
        new_user = [user_name, hash]
        print(new_user)

                #add in new user to db
        cursor.execute("INSERT into users(user_name, hash) VALUES(?, ?)", new_user)

        db.commit()
        db.close()

        #TODO: let users know they are registered


        return render_template("/login.html")


                


@app.route("/food", methods =["GET", "POST"] )
@login_required
def food():
    if request.method == "GET":
                
        #grab the users meal items from DB
        db = get_db()
        foods = db.cursor()

        

        
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





# add food


#closing database connection: IS THIS PROPER?? to put it down here?
""" if connection:
        connection.close()
        print("SQL connection closed")
"""