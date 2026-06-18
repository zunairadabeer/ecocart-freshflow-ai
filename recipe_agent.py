recipes = {
    "Chicken Pasta": [
        "chicken",
        "pasta"
    ],

    "Vegetable Stir Fry": [
        "broccoli",
        "carrot",
        "pepper"
    ],

    "Cheese Omelette": [
        "egg",
        "cheese"
    ],

    "Chicken Salad": [
        "chicken",
        "lettuce"
    ]
}


def suggest_recipes(inventory_items):

    available_items = []

    for item in inventory_items:
        available_items.append(
            item.name.lower()
        )

    suggestions = []

    for recipe, ingredients in recipes.items():

        match_count = 0

        for ingredient in ingredients:

            if ingredient in available_items:
                match_count += 1

        if match_count > 0:

            score = round(
                match_count / len(ingredients),
                2
            )

            suggestions.append(
                {
                    "recipe": recipe,
                    "score": score
                }
            )

    suggestions.sort(
        key=lambda recipe: recipe["score"],
        reverse=True
    )

    return suggestions
