# Recepie book CLI
 This will be a start to my recipe book app. It will incorporate 3 different tables using SQLite. 
 I will be starting with a CLI interaction so that I can just focus on the database rather than the GUI at the moment.

## DB schema and table design
 Table: __recipes__
    This will hold the majority of the recipe data.
    columns:
        id - integer - primary key, auto_incremented
        name - text - name of the recipe
        category - text - type of dish (i.e. breakfast, dinner, snack, etc.)
        prep_time - integer - preparation time in minutes
        cook_time - integer - cooking time in minutes
        total_time - integer - total time in minutes
        instructions - text - instructions for preparing the dish
        servings -integer - number of servings
        date_added - datetime - date the recipe was added

 Table: __ingredients__
    This will hold the ingredients. It will be queried using the recipe_id which will be tied to each ingredient.
    columns:
        id - integer - primary key, auto-incremented
        recipe_id - integer - foreign key referencing recipes(id)
        name - text - name of the ingredient
        quantity - real - amount needed for each ingredient
        unit - text - unit of measurement
        
 Table: __recipe_tags__
    This will hold the tags for each recipe. This will be used to have the capability for multiple tags for each recipe, and can cross reference using recipe_id.
    columns:
        id - integer - primary key, auto-incremented
        recipe_id - integer - foreign key referencing recipes(id)
        tag - text - tag for categorizing the recipe