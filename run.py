# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('recipes_project3')

def get_user_preference():
    """
    Get preference of either salty or sweet by the user.
    Raises error if user doesn't choose between sweet or
    salty
    """
    print("Please enter your flavor preference.")
    print("Please choose between: Salty or Sweet.\n")

    while True:
        data_str = input("Enter your preference here: ").strip().lower()
        if data_str in ["salty", "sweet"]:
            return data_str
        print("Invalid input. Please enter 'salty' or 'sweet'.")


def get_available_ingredients():
    """
    Ask the user for their available ingredients
    """
    print("\nEnter the ingredient you have available")
    ingredients = input("Available ingredients: ").strip().lower().split(',')
    return [ingredient.strip() for ingredient in ingredients]


def find_recipes(flavor, ingredients):
    """
    Find recipes based on flavor and user-provided ingredients.
    Filter the recipes by the chosen flavor.
    """
    worksheet = SHEET.worksheet('Meals')  
    data = worksheet.get_all_records()
    """
    Filter recipes by the chosen flavor
    """
    filtered_recipes = [row for row in data if row['Flavor'].lower() == flavor]

    # Match ingredients with recipes
    matching_recipes = []
    for recipe in filtered_recipes:
        recipe_ingredients = [ingredient.strip().lower() for ingredient in recipe['Ingredients'].split(',')]
        # Check if any of the user's ingredients match the recipe ingredients
        if any(ingredient in recipe_ingredients for ingredient in ingredients):
            matching_recipes.append(recipe)  # Add the recipe name to results
    return matching_recipes

def list_recipes(recipes):
    """
    Display a list of recipes to the user.
    """
    print("\nHere are some recipes you can make:")
    for i, recipe in enumerate(recipes, start=1):
        print(f"{i}. {recipe['Recipe']}")

def add_recipe_to_sheet():
    """
    Allow the user to add a new recipe to the Google Sheet.
    """
    print("\nNo recipes found. Would you like to contribute a new recipe to help others?")
    add_recipe = input("Enter 'yes' to add a recipe, or 'no' to exit: ").strip().lower()
    if add_recipe != 'yes':
        return False
    
    # Get recipe details from the user
    recipe_name = input("Enter the name of the recipe: ").strip()
    flavor = input("Enter the flavor (Salty/Sweet): ").strip().lower()
    while flavor not in ["salty", "sweet"]:
        print("Invalid input. Please enter 'Salty' or 'Sweet'.")
        flavor = input("Enter the flavor (Salty/Sweet): ").strip().lower()
    ingredients = input("Enter the ingredients (comma-separated): ").strip()

    # Append the new recipe to the Google Sheet
    worksheet = SHEET.worksheet('Meals')
    worksheet.append_row([recipe_name, flavor, ingredients])

    print(f"\nThank you! Your recipe '{recipe_name}' has been added to the recipe collection.")
    return True

def list_recipe_ingredients(recipe_name, all_recipes):
    """
    Display the ingredients for the selected recipe.
    """
    for recipe in all_recipes:
        if recipe['Recipe'].lower() == recipe_name.lower():
            print(f"\nThe ingredients for '{recipe_name}' are:")
            print(f"{recipe['Ingredients']}")
            return
    print("Sorry, we couldn't find the ingredients for that recipe.")


def main():
    """
    Main function to run the program
    """
    flavor = get_user_preference()

    while True:
        # Ask for ingredients
        ingredients = get_available_ingredients()
        recipes = find_recipes(flavor, ingredients)

        if recipes:
            print("\nHere are some recipes you can make:")
            for recipe in recipes:
                print(f"- {recipe}")
            break  # Exit the loop if recipes are found
        else:
            print("No recipes found with the given ingredients.")
            try_again = input("Would you like to try adding more ingredients? (yes/no): ").strip().lower()
            if try_again != "yes":
                print("Goodbye! Feel free to try again later.")
                break 
    
if __name__ == "__main__":
    main()






