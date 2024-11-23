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

get_user_preference()

def get_available_ingredients():
    """
    Ask the user for their available ingredients
    """
    print("\nEnter the ingredient you have available")
    ingredients = input("Available ingredients: ").strip().lower().split(',')
    return [ingredient.strip() for ingredient in ingredients]

get_available_ingredients()

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

def main():
    """
    Main function to run the program
    """
    flavor = get_user_preference()
    ingredients = get_available_ingredients()
    recipes = find_recipes(flavor, ingredients)

    if recipes:
        print("\nHere are some recipes you can make:")
        for recipe in recipes:
            print(f"- {recipe}")
    else:
        print("\nNo recipes found with the given ingredients. Try adding more ingredients!")






