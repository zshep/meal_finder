


function add_recipe(recipe_name) {
    var added_recipe = document.getElementById('${recipe_name}');
    print(recipe_name)
    console.log("attempting to add recipe to users cookbook");
    console.log(added_recipe);
    console.log(added_recipe.value)

    $.ajax({
        url: '/add_recipe',
        type: 'POST',
        data: { 'recipe' : added_recipe},
        success: function(response) {
            console.log(response);
            console.log(response.result);
        },

        error: function(error){
            console.log(error);
        }

    });

}