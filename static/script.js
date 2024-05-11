

// fetch function to send btn info to backend
async function add_recipe(btn) {
    //console.log("a btn was clicked");
   
    try {
        console.log(btn)
        let addrecipe = {
            recipe_name: btn,
        };
        console.log(addrecipe)
        const response = await fetch("/add_recipe", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(addrecipe)
        });

        console.log("fetch away!")
        const result = await response.json();
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