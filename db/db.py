import sqlite3

def get_db():
    #setting up sqlite database
    try:
        connection = sqlite3.connect('foods.db', check_same_thread= False)
        cursor = connection.cursor()
        print("DB init")

        #loading/creating users table
        cursor.execute("CREATE TABLE IF NOT EXISTS users (personid INTEGER PRIMARY KEY AUTOINCREMENT, user_name text NOT NUll, hash text)")
        #print("users table created")

        #loading/creating meal items table
        cursor.execute("CREATE TABLE IF NOT EXISTS meal_items (meal_id INTEGER PRIMARY KEY AUTOINCREMENT, meal_name TEXT NOT NULL, is_easy BOOL)")
        #print("meal_items table created")

        #loading/creating food items table
        cursor.execute("CREATE TABLE IF NOT EXISTS food_items (food_id INTEGER PRIMARY KEY AUTOINCREMENT, food_name TEXT NOT NULL)")
        #print("food_items table created")
        
        #loading/creating ingredients table
        cursor.execute("CREATE TABLE IF NOT EXISTS ingredients (food_id INTEGER FORIEGN KEY REFERENCES food_items (food_id), meal_id INTEGER FORIEGN KEY REFERENCES meal_items (meal_id))")
        #print("ingredients table created")

        #loading/creating cookbook table (individual's meal items)
        cursor.execute("CREATE TABLE IF NOT EXISTS cookbook(person_id INTEGER FORIEGN KEY REFERENCES users(person_id), meal_id INTEGER FORIEN KEY REFERENCES meal_items(meal_id), day INTEGER)")
        #print("cookbook table created")

        

        connection.commit()

        # return connection for routes to use
        return connection 

    #handling errors
    except sqlite3.Error as error:
        print('Error Occured - ', error)