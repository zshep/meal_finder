# Shep's Meal Planner

#### Video Demo: [LInk to video](https://youtu.be/8WKtuLQJ6CU)

I try my best to eat healthy, I really do! The biggest challenge is to make sure that you plan out a weeks worth of meals so you are less tempted to default to quick and easy foods, that might be tasty... just not the healthiest. 

That is why I made Meal Planner (formerly known as Meal Finder), an website to help plan out my meals for the week. Meal Planner allows users to log into a profile which allows them to add Recipe ideas to the global Meal Planner list along with their own personal "cookbook". Users then can populate a 7 day calendar with any choice of Recipes to any desired day of the week. The fact that users have their own favorite recipes saved they can easily access all of them so they are not just defaulting to the same 3-4 meals.

## Design
I wrote my back end using python for both it's familiarity and ease which meant I was also going to use Flask along with Jinja. From the cs50 course I became comfortable with Flask and Jinja that I didn't want to look into something else, But I have used Flask with React in the past before, it just would have taken me longer to get the hang of it. 

## db/
I kept going back and forth between wanting to use sqlite and sqlalchemy. I have used sql alchemy before and even though it does require more set up I thought this could be more helpful in the future when trying to make the app more robust. I ultimately went with sqlite out of fearing hooking up my db to flask. I didn't want things to get to crowded in my app.py file that I created a db directory and having my own separate db.py file. This made it easy to organize my database and set up the code to create the tables I would be using. I then could easily export that db instance into my app.py file.

I used the database from the problem set movies as inspiration for creating and connecting my tables. At first, I wanted to have a table for individual food items that you then connected to a meals table which had the name and id of whole recipes. I connected both of those tables through a table called ingredients, connecting the ids of both meals and food tables. While these tables do exist in my code, I actually never used them since I was more focused on connecting recipes to individual users, making sure the multiple users could have the same recipe. In the future I plan on linking each recipe with different food items to help also build a shopping list for future versions.

I finally made a cookbook table that linked a users id, a meal id and a field for to indicate a day. This way I could connect a user with a recipe (meal) and also a day so it could be populated in a table.

## env/ 
In trying to do best practices, I created a env folder alone with a .gitignore and requirements.txt document to help manage and keep save my dependencies

## static/
Directory for Flask which held my image for an error page, and my styles.css along with a script.js. The script.js had a couple of functions which helped pass data from front end to back end. 

## templates/
The directory used by Flask for my various web templates. My layout was inspired by the finance app, by having a navigation bar at the top and a footer on the bottom allowing to use jinja's blocking to switch in whatever main page content I need for the given task. I also used Jinja’s variables and loops to make it easy to show proper data stored from the database. 

I made my index.html the home page that users would instantly see when they logged in and hit the home button in the navbar. I have a table showing the user's planned meals (if there are) as well as drop down options input for the user to select a meal to be paired with a certain day. I used a form tag to send the request to the backend which was relatively easy.

The difficult part was I originally wanted a delete button next to the meal items as they showed up on the daily planner. That way the user could just remove any meal from any given day. I kept running into an issue with using JS and fetch to send the data to my back end. My route was able to correctly get the message and use the data properly but there was always a 405 error on my front end which forced me to have to refresh the browser if I wanted to see the changes immediately. I have decided to put this feature on the next version of the app since users could reassign a meal to another day. 

I successfully used JavaScript and the fetch API to send data from my front end to the back to delete meals from the user’s cookbook. I was getting error messages on my front end, but it did not bother me since the page would reload almost instantly to show the new changes. I’m not sure why I was running into this problem with deleting from the user’s meal planner (the calendar). I have a feeling is that I was having trouble with a PUT request, since I was just changing the day to a NULL value instead of deleting the whole row. If I did delete the whole role then the user would also lose the meal to their own cookbook which I did not want to have happen.

My templates for adding meal items and registering users and logging in used similar techniques and strategies in my home templates using Jinja to properly load templates with desired data from my back end. 

## app.py
The powerhouse of my app. I used the idea of requiring a proper log in to view most pages just like the finance problem set. I was able to create a decorator to wrap all my routes in.

App.py contains all my routes which utilizes sqlite to pull data from the database along with making changes and updates as the user creates new recipes, adds them to their individual cookbooks and deleting meals from their cookbook.
I was comfortable enough with sqlite and SQL from past homework that my main challenge was just properly sending and receiving data from the front end.

All other files and folders are for best practices and boiler plate files for certain dependencies. 






