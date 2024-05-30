# Shep's Meal Planner

#### Video Demo: <URL here>

#### Description:
I try my best to eat healthy, I really do! The biggest challenge is to make sure that you plan out a weeks worth of meals so you are less tempted to default to quick and easy foods, that might be tastey... just not the healthiest. 

That is why I made Meal Planner (formely known as Meal Finder), an website to help plan out my meals for the week. Meal Planner allows users to log into a profile which allows them to add Recipe ideas to the global Meal Planner list along with their own personal "cookbook". Users then can populate a 7 day calendar with any choice of Recipes to any desired day of the week. The fact that users have their own favorite recipes saved they can easily access all of them so they are not just defaulting to the same 3-4 meals.

### Design
I wrote my back end using python for both it's familiarity and ease which meant I was also going to use Flask along with Jinja. From the cs50 course I became comfortable with Flask and Jinja that I didn't want to look into something else, But I have used Flask with React in the past before, it just would have taken me longer to get the hang of it. 

### db
I kept going back and forth between wanting to use sqlite and sqlalchemy. I have used sql alchemy before and even though it does require more set up I thought this could be more helpful in the future when trying to make the app more robust. I ultimately went with sqlite out of being scared of hooking up my db to flask. I didn't want things to get to crowded in my app.py file that I created a db directory and having my own seperate db.py file. This made it easy to organize my database and set up the code to create the tables I would be using. I then could easily export that db instance into my app.py file.

I used the movies.db as inspiration of creating and connecting my tables. At first I wanted to have a table for individual food items that you then connected to a meals table which had the name and id of whole recipies. I connected both of those tables through a table called ingredients, connecting the ids of both meals and food tables. Whle these tables do exist in my code, I actually never used them since I was more focused on connecting recipies to individual users, making sure the multiple users could have the same recipe. In the future I plan on linking each recipie with different food items to help also build a shopping list for future versions.



