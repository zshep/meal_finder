import sqlite3

def get_db():
    #setting up sqlite database
    try:
        connection = sqlite3.connect('foods.db', check_same_thread= False)
        cursor = connection.cursor()
        print("DB init")

        cursor.execute("CREATE TABLE IF NOT EXISTS users (personid INTEGER PRIMARY KEY AUTOINCREMENT, user_name text NOT NUll, hash text)")

        connection.commit()

        

        # do I want to return the cursor or just the connection? 
        return connection 

    #handling errors
    except sqlite3.Error as error:
        print('Error Occured - ', error)