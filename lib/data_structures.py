spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

def get_spiciest_foods(spicy_foods):
   return [{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}, {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}
def print_spiciest_foods(spicy_foods):
    # Filter foods with heat level greater than 5
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    
    # Print each spiciest food in the correct format
    for food in spiciest_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average_heat = total_heat // len(spicy_foods) 
    return average_heat

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, new_spicy_food):
    # Add the new spicy food to the list
    spicy_foods.append(new_spicy_food)
    # Return the updated list
    return spicy_foods

# Example usage
spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

new_food = {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}

updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(updated_spicy_foods)

