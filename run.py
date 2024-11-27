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

def view_recipe_ingredients(recipes):
    """
    Allow the user to view the ingredients for a selected recipe.
    """
    while True:
        view_ingredients = input("\nWould you like to view the ingredients for any of these recipes? (yes/no): ").strip().lower()
        if view_ingredients == "yes":
            try:
                choice = int(input("Enter the number of the recipe to view its ingredients: "))
                if 1 <= choice <= len(recipes):
                    selected_recipe = recipes[choice - 1]
                    print(f"\nThe ingredients for '{selected_recipe['Recipe']}' are:")
                    print(f"{selected_recipe['Ingredients']}")
                    return
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif view_ingredients == "no":
            return
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

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


def main():
    """
    Main function to run the program.
    """
    while True:
        flavor = get_user_preference()
        ingredients = get_available_ingredients()
        recipes = find_recipes(flavor, ingredients)

        if recipes:
            list_recipes(recipes)
            view_recipe_ingredients(recipes)
        else:
            print("\nWe are sorry, we have no recipes found with the given ingredients.")
            if not ask_to_try_again():
                if not add_recipe_to_sheet():
                    break

        # Ask the user if they want to continue or exit
        if not ask_to_continue_or_exit():
            break


if __name__ == "__main__":
    main()






