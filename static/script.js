//fetch function for deleting a recipe from users cookbook
async function delete_recipe(name, id){
    try{
        //console.log(name);
        //console.log(id);
        let delete_recipe = {
            meal_name : name,
            meal_id : id,
        };
        console.log(delete_recipe);

        const response = await fetch("/delete_meal", {
            method : "DELETE",
            headers : {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(delete_recipe)
        });
        
        const result = await response.json();

        if (result)
            {
                console.log("fetch success")
                console.log(result)
            }
            
    }catch(error){

        console.log("there was an error")
        console.log(error)
    }
}

//fetch function for deleting meal from users meal plan (calendar)
async function delete_mp(day){
    try{
        console.log("the day is: ", + day)

        const url ="/delete_meal_plan"

        let fetchData =  {
            method : "PUT",
            headers : {
                "Content-Type": "application/json",
            },
            body : JSON.stringify(day),
        };

        fetch(url, fetchData)
            .then((function(){
                
                console.log("sent data, what did we get back?")
                console.log(fetchData)
            }))

        
        
        console.log("Delete meal from meal plan request sent")

    } catch(error){

        console.log("there was an error with deleting meal plan")
        console.log(error)
    }
}

// fetch function for adding recipe to users cookbook
async function add_recipe(name, id) {
    //console.log("a btn was clicked");
   
    try {
        //adding new recipe details in object
        let addrecipe = {
            recipe_name: name,
            recipe_id: id,
        };
        console.log(addrecipe)
        // sending new recipe to back end
        const response = await fetch("/add_recipe", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(addrecipe)
        });

        console.log("fetch away!")
        const result = await response.json();
        console.log(result);
        console.log("Success:", + result);
    } catch(error) {
        console.error("Error:", error);
    }
}



