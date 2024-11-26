def manage_students():
    students = ["Alice", "Bob", "Charlie"]  # Create a list of student names
    first_student = students[1]            # Assign the second student's name
    last_student = students[-1]            # Assign the last student's name
    return f"First Student: {first_student}, Last Student: {last_student}"

# Call the function and print the result
print('Exercise 1:', manage_students())


def combine_foods():
    foods = ("Pizza", "Burger", "Sushi")  
    meal = ""                            
    for food in foods:                   
        meal += food + " "
    return meal.strip()                  


print('Exercise 2:', combine_foods())


def slice_foods():
    foods = ("Pizza", "Burger", "Sushi")  
    last_two_foods = foods[-2:]           
    return last_two_foods


print('Exercise 3:', slice_foods())


def hometown_info():
    home_town = {                        
        "city": "Dallas",
        "state": "Texas",
        "population": 1340000
    }
    home_town_message = (                 
        f"I was born in {home_town['city']}, "
        f"{home_town['state']} - population of {home_town['population']}"
    )
    return home_town_message


print('Exercise 4:', hometown_info())


def list_home_town_items():
    home_town = {                        
        "city": "Dallas",
        "state": "Texas",
        "population": 1340000
    }
    home_town_items = []                  # Initialize an empty list
    for key, value in home_town.items():  # Iterate over key-value pairs
        home_town_items.append(f"{key} = {value}")
    return home_town_items


print('Exercise 5:', list_home_town_items())
