from flask import Flask, flash, redirect, render_template, request, session, url_for
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

    meal_plan =[] #empty list to hold meals that are associated with a day
    #grab users info
    user_name = session['name']
    user_id = session['user_id']
    print(user_name, user_id)

    #grab users meals
    db = get_db()
    request = db.cursor().execute("SELECT meal_name, meal_items.meal_id, cookbook.day FROM meal_items JOIN cookbook ON meal_items.meal_id = cookbook.meal_id WHERE cookbook.person_id == (?)", [session['user_id']])
    user_meals = request.fetchall()
    print(user_meals)

    for meals in user_meals:
        if meals[2] is not None:
            meal_plan.append(meals)

            
    print(meal_plan)

    db.close()

    return render_template("index.html", user_name = user_name, meals = user_meals, meal_plan = meal_plan)

#login route
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

#logout route
@app.route("/logout")
def logout():
    #end session for username
    session.clear()

    return redirect("/")
# register route
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

#show meal route
@app.route("/show_meal", methods =["GET"])
@login_required
def show_meal():
    #grab the users meal items from DB
    db = get_db()
    res = db.cursor().execute("SELECT meal_name, meal_items.meal_id FROM meal_items JOIN cookbook ON meal_items.meal_id = cookbook.meal_id WHERE cookbook.person_id == (?)", [session['user_id']])
    user_meals = res.fetchall()
    print("the users' meals are...")
    print(user_meals)

    #grab all the recipe names and ids for db
    recipes = db.cursor().execute("SELECT meal_name, meal_id FROM meal_items")

    all_meals = recipes.fetchall()
    #print("all meals are...")
    #print(all_meals)
     
    #closing db
    db.close()

        
    return render_template("/food.html", user_meals = user_meals, all_meals = all_meals)

# add meal to global recipe list
@app.route("/add_meal", methods =["GET", "POST"] )
@login_required
def add_meal():
    #handling Get request
    if request.method == "GET":
                
        return render_template("/add_food.html")
    #handling Post request
    else:
        meal_name = request.form.get("mealname")
        is_easy = request.form.get("easy")
        print(meal_name, is_easy)
        meal_list = [] #empty list to hold list of meals

        #grabbing meal list from meal_item tables
        db = get_db()
        res = db.cursor().execute("SELECT meal_name FROM meal_items")
        old_meals = res.fetchall()
        #print(old_meals)

        #check to see if meal already exists in DB
        for old_meal in old_meals:
            print(old_meal[0])
            meal_list.append(old_meal[0])

        print(meal_list)
        if meal_name in meal_list:
            print("this meal already exists")
            return render_template("error.html")
        
        else:    
            print("meal not found in db")
            new_meal = [meal_name, is_easy]

            # add new meal item to db
            db = get_db()
            db.cursor().execute("INSERT INTO meal_items(meal_name, is_easy) VALUES(?,?)", new_meal)

            db.commit()
            db.close()        
            print("meal added to db")

            return redirect("/show_meal")

#adding a recipe from global to users cookbok
@app.route("/add_recipe", methods = ["POST"])
def add_recipe():
    print("the add recipe button was pushed")
    if request.method == "POST":
        data = request.get_json() # retrieve the data sent from JS
        print(data)
        new_recipe = data['recipe_name']
        meal_id = data['recipe_id']
       
           
        print(new_recipe +" has the id of", meal_id)

        insert_cookbook = [session['user_id'], meal_id]
        print(insert_cookbook)
     
        
        #adding new recipe to database
        db = get_db()
        db.cursor().execute("INSERT into cookbook(person_id, meal_id) VALUES(?, ?)", insert_cookbook)

        db.commit()
        db.close() 
        print("recipe should be added to users cookbook. DB Committed and closed")
        
        return redirect(url_for('show_meal'))

#delete meal route
@app.route("/delete_meal", methods = ["DELETE"])
@login_required
def delete_meal():
    print("delete meal button was pressed")
    
    data = request.get_json() #grab data from front end JS
    print(data)
    meal_name = data['meal_name']
    meal_id = data['meal_id']

    print(meal_name +" has the id of", meal_id)

    #sql query to delete row of meal id with person id
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM cookbook WHERE meal_id = ? AND person_id =?", [meal_id, session['user_id']])

    db.commit()
    db.close()
    print("the meal item should have been deleted from users cookbook")

    return render_template("food.html")

@app.route("/mealplan", methods = ["POST"])
@login_required
def meal_plan():

    print("attempting to add cookbook item to users meal plan")

    #grab data from front end
    meal = request.form.get("meal") # getting meal id
    day = request.form.get("day") #getting number 0-6
    print(meal, day)
    #print(type(day))

    #debugging on user errors
    if meal == "Choose a Meal":
        print("missing meal")
        return render_template("error.html")
    elif day == "Choose a day":
        print("missing day")
        return render_template("error.html")
    # checking if user picked random
    elif meal == "Random":
        #choose a meal at random
        db = get_db()
        random_meal = db.cursor().execute("SELECT meal_items.meal_id FROM meal_items JOIN cookbook ON meal_items.meal_id = cookbook.meal_id WHERE cookbook.person_id == ? ORDER BY RANDOM() LIMIT 1", [session["user_id"]])

        print(random_meal)
        db.close()

        meal_plan = [ session["user_id"], random_meal, day]
        new_db = get_db()

        new_db.cursor().execute("UPDATE cookbook SET day = ? WHERE person_id = ? AND meal_id = ? ", day, session['user_id'], random_meal)

        db.commit()
        db.close()
 
        return render_template("/index.html")
    
    #dealing with meal that user selected (not random)
           
    #Post/update data to meal_plan table 
    db = get_db()
    db.cursor().execute("UPDATE cookbook SET day = ? WHERE person_id = ? AND meal_id = ? ", [day, session['user_id'], meal])

    db.commit()
    db.close()
    

    return render_template("/index.html")



@app.route("/jedi")
def jedi():
    return render_template("layout.html")

