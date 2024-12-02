import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('recipes_project3')


def display_main_menu():
    """
    Display the main menu and prompt the user to choose an action.

    Returns:
        int: The user's menu choice (1, 2, or 3).

    Raises:
        ValueError: If the user input is not a valid number or choice.
    """
    print("\nWelcome to the Recipe Finder! Your guide to delicious meals.")
    print("\nMain Menu:\n")
    print("1. Find recipes")
    print("2. Add a recipe")
    print("3. Exit\n")

    while True:
        try:
            choice = int(
                input("What would you like to do? Enter the number of your "
                      "choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a number (1, 2, or 3)."
                  f"{Style.RESET_ALL}")


def get_user_preference():
    """
    Get the user's preference for either salty or sweet recipes.

    Returns:
        str: The user's flavor preference ('salty' or 'sweet').

    Raises:
        ValueError: If the user enters a value other than 'salty' or 'sweet'.
    """
    print("\nPlease enter your flavor preference.\n")
    print(f"Please choose between: {Fore.BLUE}Salty{Style.RESET_ALL} "
          f"or {Fore.BLUE}Sweet{Style.RESET_ALL}.\n")

    while True:
        data_str = input(f"{Fore.YELLOW}Enter your preference here:"
                         f"{Style.RESET_ALL} ").strip().lower()
        if data_str in ["salty", "sweet"]:
            return data_str
        print(f"{Fore.RED}Invalid input. Please enter 'salty' or 'sweet'."
              f"{Style.RESET_ALL}")


def get_available_ingredients(flavor):
    """
    Display a list of available ingredients based on the selected flavor
    and allow the user to select ingredients.

    Args:
        flavor (str): The user's flavor preference ('salty' or 'sweet').

    Returns:
        list: A list of selected ingredients chosen by the user.

    Raises:
        ValueError: If the user enters invalid input for ingredient selection.
    """
    salty_ingredients = [
        "salt", "peppers", "onions", "garlic", "chicken", "beef",
        "tomatoes", "rice", "pasta", "butter"
    ]
    sweet_ingredients = [
        "sugar", "flour", "eggs", "butter", "milk", "chocolate",
        "vanilla", "cream", "apples", "bananas"
    ]
    available_ingredients = salty_ingredients if flavor == "salty" \
        else sweet_ingredients

    while True:
        print("\nChoose your ingredients from the list below:\n")
        for i, ingredient in enumerate(available_ingredients, start=1):
            print(f"{i}. {ingredient}")

        print("\nEnter one of the available ingredients:")

        selected_input = input("Your selection: ").strip()

        if selected_input.isdigit() and 1 <= int(selected_input) <= \
                len(available_ingredients):
            selected_ingredient = available_ingredients[
                int(selected_input) - 1]
            print(f"\nYou selected: {selected_ingredient}")
            return [selected_ingredient]
        else:
            print(f"\n{Fore.RED}Invalid input. Please enter a single valid "
                  f"number from the list.{Style.RESET_ALL}")


def find_recipes(flavor, ingredients):
    """
    Find recipes from a Google Sheet based on the selected flavor
    and user-provided ingredients.

    Args:
        flavor (str): The selected flavor ('salty' or 'sweet').
        ingredients (list): A list of ingredients selected by the user.

    Returns:
        list: A list of dictionaries, each containing recipe details
              (e.g., 'Recipe', 'Ingredients').
    """
    worksheet = SHEET.worksheet('Meals')
    data = worksheet.get_all_records()

    filtered_recipes = [row for row in data if row['Flavor'].lower() == flavor]

    matching_recipes = []
    for recipe in filtered_recipes:
        recipe_ingredients = [
            ingredient.strip().lower() for ingredient in recipe[
                'Ingredients'].split(',')
        ]
        if any(ingredient in recipe_ingredients for ingredient in ingredients):
            matching_recipes.append(recipe)
    return matching_recipes


def list_recipes_with_ingredients(recipes):
    """
    Display a list of recipes based on the user's selected ingredients.

    Args:
        recipes (list): A list of recipes that match the user's criteria.
    """
    print("\nHere are some recipes you can make:")
    for i, recipe in enumerate(recipes, start=1):
        print(f"\n{i}. {Fore.GREEN}{recipe['Recipe']}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Ingredients: {Style.RESET_ALL}"
              f"{recipe['Ingredients']}")


def add_recipe_to_sheet():
    """
    Add a new recipe to the Google Sheet.

    Returns:
        bool: True if the recipe is successfully added.
    """
    recipe_name = input("\nEnter the name of the recipe: ").strip()
    flavor = input("\nEnter the flavor (Salty/Sweet): ").strip().lower()
    while flavor not in ["salty", "sweet"]:
        print("\nInvalid input. Please enter 'Salty' or 'Sweet'.")
        flavor = input("\nEnter the flavor (Salty/Sweet): ").strip().lower()
    ingredients = input("\nEnter the ingredients (comma-separated): ").strip()

    worksheet = SHEET.worksheet('Meals')
    worksheet.append_row([recipe_name, flavor, ingredients])

    print(f"\nThank you! Your recipe '{recipe_name}' has been added to the "
          f"recipe collection.")
    return True


def main():
    """
    Main function to run the program, providing a menu for the user.
    """
    while True:
        user_choice = display_main_menu()

        if user_choice == 1:
            flavor = get_user_preference()
            ingredients = get_available_ingredients(flavor)
            recipes = find_recipes(flavor, ingredients)

            if recipes:
                list_recipes_with_ingredients(recipes)
            else:
                print("\nWe are sorry, we have no recipes found with the "
                      "given ingredients.")

            while True:
                another_search = input("\nWould you like to select a new "
                                       "ingredient and see new recipes? "
                                       "(yes/no): ").strip().lower()

                if another_search == "yes":
                    ingredients = get_available_ingredients(flavor)
                    recipes = find_recipes(flavor, ingredients)

                    if recipes:
                        list_recipes_with_ingredients(recipes)

                    else:
                        print("\nWe are sorry, we have no recipes found with "
                              "the given ingredients.")

                elif another_search == "no":
                    print("\nReturning to the main menu...")
                    break

                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

        elif user_choice == 2:
            add_recipe_to_sheet()

        elif user_choice == 3:
            back_to_main_menu = input(
                "Please enter 'y' to go back to the main menu or anything "
                "else to exit: ").strip().lower()

            if back_to_main_menu == 'y':
                print("\nReturning to the main menu...")
                continue
            else:
                print("\nThank you for using the Recipe Finder! Goodbye!")
                break


if __name__ == "__main__":
    main()