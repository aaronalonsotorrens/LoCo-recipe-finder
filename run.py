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
            matching_recipes.append(recipe['Recipe'])  # Add the recipe name to results
    return matching_recipes

def add_recipe_to_sheet():
    """
    Allow the user to add a new recipe to the Google Sheet.
    """
    print("No recipes found. Would you like to contribute a new recipe to help others?\n")

    # Confirm if the user wants to add a recipe
    add_recipe = input("Enter 'yes' to add a recipe, or 'no' to exit: ").strip().lower()
    if add_recipe != 'yes':
        print("I am sorry we could not be of more help right now please come back soon as we add more recipies to our list. Goodbye!")
        return

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






