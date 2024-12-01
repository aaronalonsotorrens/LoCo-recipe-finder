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

from colorama import Fore, Style
from art import text2art



def display_main_menu():
    """
    Display the main menu and prompt the user to choose an action.
    """

    print("\nWelcome to the Recipe Finder! Your guide to delicious meals.")
    print("\nMain Menu:\n")
    print("1. Find recipes")
    print("2. Add a recipe")
    print("3. Exit\n")

    while True:
        try:
            choice = int(input("What would you like to do? Enter the number of your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

def get_user_preference():
    """
    Get preference of either salty or sweet by the user.
    Raises error if user doesn't choose between sweet or
    salty
    """
    print("\nPlease enter your flavor preference.\n")
    print(f"Please choose between: {Fore.BLUE}Salty{Style.RESET_ALL} or {Fore.BLUE}Sweet{Style.RESET_ALL}.\n")

    while True:
        data_str = input(f"{Fore.YELLOW}Enter your preference here:{Style.RESET_ALL} ").strip().lower()
        if data_str in ["salty", "sweet"]:
            return data_str
        print(f"{Fore.RED}Invalid input. Please enter 'salty' or 'sweet'.{Style.RESET_ALL}")


def get_available_ingredients(flavor):
    """
    Display a predefined list of ingredients based on the flavor selected by the user.
    Allow users to select up to 10 ingredients by entering the corresponding numbers.
    """
    # Predefined ingredient lists
    salty_ingredients = [
        "salt", "peppers", "onions", "garlic", "chicken", "beef",
        "tomatoes", "rice", "pasta", "butter"
    ]
    sweet_ingredients = [
        "sugar", "flour", "eggs", "butter", "milk", "chocolate",
        "vanilla", "cream", "apples", "bananas"
    ]

    # Select the appropriate list based on the flavor
    available_ingredients = salty_ingredients if flavor == "salty" else sweet_ingredients

    while True:
        # Display the list of ingredients with numbers
        print("\nChoose your ingredients from the list below:\n")
        for i, ingredient in enumerate(available_ingredients, start=1):
            print(f"{i}. {ingredient}")

        print("\nEnter one of the available ingredients:")

        # Get the user's input
        selected_input = input("Your selection: ").strip()

        # Check if the input is a single valid number
        if selected_input.isdigit() and 1 <= int(selected_input) <= len(available_ingredients):
            selected_ingredient = available_ingredients[int(selected_input) - 1]
            print(f"\nYou selected: {selected_ingredient}")
            return [selected_ingredient]  # Return as a list to match expected structure
        else:
            print(f"\n{Fore.RED}Invalid input. Please enter a single valid number from the list.{Style.RESET_ALL}")

def find_recipes(flavor, ingredients):
    """
    Find recipes based on flavor and user-provided ingredients.
    Filter the recipes by the chosen flavor.
    """
    worksheet = SHEET.worksheet('Meals')  
    data = worksheet.get_all_records()
    
    # Filter recipes by the chosen flavor
    
    filtered_recipes = [row for row in data if row['Flavor'].lower() == flavor]

    # Match ingredients with recipes
    matching_recipes = []
    for recipe in filtered_recipes:
        recipe_ingredients = [ingredient.strip().lower() for ingredient in recipe['Ingredients'].split(',')]
        # Check if any of the user's ingredients match the recipe ingredients
        if any(ingredient in recipe_ingredients for ingredient in ingredients):
            matching_recipes.append(recipe)  # Add the recipe name to results
    return matching_recipes

        
def list_recipes_with_ingredients(recipes):
    """
    Display a list of recipes to the user.
    """
    print("\nHere are some recipes you can make:")
    for i, recipe in enumerate(recipes, start=1):
        print(f"\n{i}. {Fore.GREEN}{recipe['Recipe']}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Ingredients: {recipe['Ingredients']}{Style.RESET_ALL}")

def add_recipe_to_sheet():
    """
    Allow the user to add a new recipe to the Google Sheet.
    """
    
    # Get recipe details from the user
    recipe_name = input("\nEnter the name of the recipe: ").strip()
    flavor = input("\nEnter the flavor (Salty/Sweet): ").strip().lower()
    while flavor not in ["salty", "sweet"]:
        print("\nInvalid input. Please enter 'Salty' or 'Sweet'.")
        flavor = input("\nEnter the flavor (Salty/Sweet): ").strip().lower()
    ingredients = input("\nEnter the ingredients (comma-separated): ").strip()

    # Append the new recipe to the Google Sheet
    worksheet = SHEET.worksheet('Meals')
    worksheet.append_row([recipe_name, flavor, ingredients])

    print(f"\nThank you! Your recipe '{recipe_name}' has been added to the recipe collection.")
    return True


def main():
    """
    Main function to run the program with a main menu.
    """
    while True:
        # Display the main menu
        user_choice = display_main_menu()

        if user_choice == 1:
            # Option to find recipes
            flavor = get_user_preference()
            ingredients = get_available_ingredients(flavor)
            recipes = find_recipes(flavor, ingredients)

            if recipes:
                list_recipes_with_ingredients(recipes)
            else:
                print("\nWe are sorry, we have no recipes found with the given ingredients.")

            # Loop for searching again
            
            while True:
                another_search = input("\nWould you like to select a new ingredient and see new recipes? (yes/no): ").strip().lower()

                if another_search == "yes":
                    ingredients = get_available_ingredients(flavor)
                    recipes = find_recipes(flavor, ingredients)

                    if recipes:
                        list_recipes_with_ingredients(recipes)

                    else:
                        print("\nWe are sorry, we have no recipes found with the given ingredients.")

                elif another_search == "no":
                    print("\nReturning to the main menu...")
                    break

                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

        elif user_choice == 2:
            # Option to add a recipe
            add_recipe_to_sheet()

        elif user_choice == 3:
            # Confirmation before exiting
            back_to_main_menu = input(
                "Please enter 'y' to go back to the main menu or anything else to exit: "
            ).strip().lower()

            if back_to_main_menu == 'y':
                print("\nReturning to the main menu...")
                continue  # Go back to the start of the main loop
            else:
                print("\nThank you for using the Recipe Finder! Goodbye!")
                break  # Exit the program

    


if __name__ == "__main__":
    main()







