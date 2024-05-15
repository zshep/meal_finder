

// fetch function to send btn info to backend
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




/*
// Ajax attempt at sending data to backend
function add_recipe(btn) {

    console.log(btn)
    let addrecipe = {
        recipe_name: btn,
    };
    console.log(addrecipe);

    $.ajax({
        url: '/add_recipe',
        type: 'POST',
        data: addrecipe,
        success: function (response) {
            console.log(response);
            console.log(response.result);
        },

        error: function (error) {
            console.log(error);
        }

    });
    console.log("did it work?")

    return btn
}

*/