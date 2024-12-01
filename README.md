# Recipe Finder LoCo

<p align="center">
    <img src="./assets/images/responsive_image.png" alt="Responsive image"/>
</p>

## Introduction

Welcome to my third project, part of the Code Institute Full Stack Development Course. The purpose of this project is to build a responsive website using python.

The code is a recipe finder. This is supposed to be a convenient and easy-to-use tool that helps you discover new meal ideas based on common ingredients that most people should have in their homes. The user will have the option to either find a recipe or add a recipe themselves to help other users find new recipes.

## Strategy

How many times have we come back from a long day at work we look in our fridge and we just stare without knowing what to cook. Recipe finder LoCo is meant for those seeking to look less and cook more. Choose from any of the ingredients dispplayed and make help those tough decisions go away.

## UX - User Experience Design

The 5 planes of UX are the following:

* The Strategy Plane
* The Scope Plane
* The Structure Plane
* The Skeleton Plane
* The Surface Plane

### The Strategy Plane

1. As the owner

* I want to show a greeting message and display a menu showing the options available.

* If the user chooses to find a recipe I want to help them make their choice easier by choosing between salty or sweet 

* I want the user to see the list of ingredients they can choose from easily and for recipes to appear when the ingredient is selected.

* I want errors indicating if the input is not correct and allow the user to try again.

* I want to give the user to find other recipes with other ingredients.

* I want to give the user to be able to exit and go back to the main menu.

* I want the user to feel engaged by allowing to contribute by adding their own recipes.

2. As a customer

* I want to have a tool that will allow me to explore and find new recipes in an easy and simple way.

* I want to see all recipes available using the ingredeint selected and to see all remaining ingredients to make that recipe.

* Given the choice to add my own recipe I want it to be simple and with instructions easy to follow.

### The scope

Below is a list of the leading features for the application.

#### In Scope Features

* A welcome message.

* Option to find a recipe.
- Option to choose recipe based on flavour preference.
- Option to choose between list of different ingredients.
- Option to repeat the process to find new recipes or return to the main menu.

* Option to add new recipe.
- Add the recipe to the spreadsheet alongside flavour profile and list of ingredients.

#### Out of Scope Features that could be implemented in the future

* Extend the list of recipes available.

* Include more flavour profiles or dietary restrictions.

* Include new categories such as nationalities, seasonal, etc.

* Add cooking instructions for each recipe for the user to understand how to make their chosen recipe.

### Structure

The website will be structured with the following design considerations.

* The user will be welcomed to the CLI (Command Line Interface) with a welcome message.
* The user will be asked for enter one of the following options displayed on the main menu.
* If they weish to find a recipe they will asked to decide on a flavour profile (Salty/sweet).
* As a result a list of ingredients will show, from which the user can pick. 
* This will be followed by a showing a list of recipes containing that ingredients.
* The user will then get the chance to decide if they wish to repeat the process with a new ingredient or exit.
* If the customer wishes to add a new recipe instead, they will asked to add the name of the recipe.
* Followed by its flavour profile.
* Finally they will be asked to add a list of ingredients within that recipe.
* The user will be thanked for adding a recipe and they will return to the main menu.
* If the user wishes to exit instead, they will recieve a prompt to make confirm that decision and if they do wish them goodbye. If they answer no they will go back to the main menu.

### Skeleton

The website will contain a simple interface that immediately welcomes the customers and takes them through the process with minimal inputs.

Aesthetically the page will be clean with no images, with some basic colours on some sections to guide the eye of the user across the code.

Should the user make an error whilst navigating through the system, a message will appear guiding them and allowing them to repeat their input.

#### Flowchart

A flowchart outlining the customer journey has been created using Lucidchart, The final application may contain higher level of detail.

<p align="center">
    <img src="./assets/images/Lucidchart.png" alt="Lucidchart"/>
</p>

### Surface

The surface theme has been kept simple and clean for a better user experience.

#### Colour and font

For colour and font colorama was imported into the pipeline for accents of colour throughout the code in order to make easier for the user to follow important information. Yellow, blue, and green are the only three colors chosen. 

Fore style was chosen due to its easy legibility. None of these have been overly used to ensure all critical text is readable.

### Features

### Current Features

* A welcome message greets the customer.

<p align="center">
    <img src="./assets/images/menu_display.png" alt="Welcome message"/>
</p>

* When option 1 is chosen flavour prefence shows up where the user must choose between salty or sweet.

<p align="center">
    <img src="./assets/images/flavour_preference.png" alt="Flavour preference"/>
</p>

* Once the flavour is chosen a list of ingredients specific to each flavour preference will show up.

<p align="center">
    <img src="./assets/images/ingredient_list.png" alt="List of ingredients"/>
</p>

* The user will pick an ingredient and a list of recipes containing that ingredients will show up. Recipes will also show the remaining ingredients to make the recipe.

<p align="center">
    <img src="./assets/images/recipe_list.png" alt="List of recipes"/>
</p>

* The user will then be asked if they wish to find more recipes by adding a new ingredient. If "yes" the list of ingredients will appear again.

<p align="center">
    <img src="./assets/images/ingredient_list_return.png" alt="List of ingredients shows again"/>
</p>

* If "no" the user will return to the main menu.

<p align="center">
    <img src="./assets/images/return_menu.png" alt="List of ingredients"/>
</p>

* When option 2 is chosen the user will be asked to enter the name of the recipe, alongside their flavour profile (salty/sweet), and list of ingredients.

<p align="center">
    <img src="./assets/images/recipe_instructions.png" alt="Instructions on how to add a recipe"/>
</p>

* The user will then receive a thank you message.

<p align="center">
    <img src="./assets/images/thank_you_message.png" alt="Thank you message"/>
</p>

* The receipe will be saved to the googlesheet.

<p align="center">
    <img src="./assets/images/googlesheet_added.png" alt="Recipe added to googlesheet"/>
</p>

* The program uses gspread API to interact with googlesheets where the ingredients and flavour profile for each recipe is stored.

<p align="center">
    <img src="./assets/images/googlesheet_project_3.png" alt="Googlesheet used in the project"/>
</p>

* When option 3 is chosen the user will be asked if the wish to return to the main menu or exit. This is to allow the user to rectify a possible mistake by having clicked option 3 by mistake. If they do decide to leave a goodbye message will be shown.

<p align="center">
    <img src="./assets/images/goodbye_message.png" alt="Goodbye message when exiting the program"/>
</p>


### Future Features

The application can be further developed. Some features include the following:

* Add cooking instructions for each recipe.
* Add an estimate cooking time for each recipe.
* Add quantities to each ingredient to show how much it is needed per person.
* Add calorie count to each ingredient to calculate the calories or nutritional content on each recipe.

### Testing

#### Validator testing

* Python

No major issues found when run through Code Institute's PEP8 linter.

<p align="center">
    <img src="./assets/images/pep8_validation.png" alt="PEP8 linter validator"/>
</p>

Validator Testing
Python
No major issues found when run through a PEP8 linter. Code Institute's PEP8 linter.

#### Manual testing

<p align="center">
    <img src="./assets/images/manual_testing.png" alt="Manual testing of the code"/>
</p>

### Fixed Bugs

Throughout this project there were no major bugs. However, I did encounter an issue. My computer broke down during this project and had to request a friends. I opened a new workspace and started adding new commits as I worked on my new workspace without realising they were not being saved. I tried troubleshooting this with tutors by pulling the git commits. However, further errors started appearing. The issue was eventually solved thanks to the help of my mentor where he suggested to save the current code directly in the run.py from github.

### Unfixed

No unfixed bugs that I am aware of.

### Deployment

#### Create googlesheet and integrate using an API

<details>
    <summary></summary>

Create a Spreadsheet (Data Model)
1. Login to your Google account, create an account if necessary.
1. Navigate to Sheets, Googles version of Microsoft Excel.
1. Start a new spreadsheet,


Setup API
1. Navigate to Google cloud platform.
1. If you do not already have a profile then follow the basic steps for creating an Account, via clicking on the 'Get Started for Free' button in the upper right corner.
1. Once the previous step is complete, create a new project with a unique title
1. You should now arrive at the project dashboard and be ready to setup the required credentials:
    * Access the navigation menu from clicking on the hamburger button
    * Select APIs and Services, followed by 'Library'
    * Search for and select Google Drive API -> Enable
    * Search for and select Google Sheets API -> Enable
    * Click Enable to navigate to 'API and Services Overview' 
    * Click Create Credentials in the upper left of the screen
    * For Credential Type, select 'Google Drive' from the dropdown
    * For 'What data will you be accessing' select Application Data
    * For 'Are you planning to use this API with Compute Engine...?' choose 'No, I'm not...'
    * Click Next
    * Within the Create Service Account page, enter a Service Account Name
    * Click Create and Continue
    * Next within 'Grant this service account access to project', choose Basic -> Editor from the 'Select a Role' dropdown
    * Click Continue
    * Next within 'Grant users access to this service account', choose 'Done'
    * On the following, click on the 'Service Account Name' you created to navigate to the config page
    * Navigate to the Keys section
    * Select 'Add Key' dropdown -> Create New Key.
    * Select 'JSON' -> Create - the file will download to your machine
    * From your local downloads folder, add file directly to your Gitpod workspace, and rename the file to creds.json
    * Within the file, copy the value for 'client email'. Paste this email address into the 'Share' area of your Google Sheet, assigning the role of Editor

Enable API within IDE
1. From within your GitPod IDE terminal, enter 'pip3 install gspread google-auth'
1. At the top of your Python file add the following lines:

    ```
    import gspread
    from google.oauth2.service_account import Credentials
    ```
    
1. Below this add the following code:

    ```
        SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]

        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open('vv_pizzas')
        console = Console()
        install(show_locals=True)
    ```
</details>

#### Deploy with Heroku
<details>
    <summary></summary>

* The requirements.txt file in the IDE must be updated to package all dependencies. To do this:
    1. Enter the following into the terminal: 'pip3 freeze > requirements.txt'
    1. Commit the changes and push to GitHub

* Next, follow the steps below:
    1. Login to Heroku, create an account if necessary
    1. Once at your Dashboard, click 'Create New App'
    1. Enter a name for your application, this must be unique, and select a region
    1. Click 'Create App'
    1. At the Application Configuration page, apply the following to the Settings and Deploy sections:
        * Within 'Settings', scroll down to the Config Vars section to apply the credentials being used by the application. In the Reveal Config Vars enter 'CREDS' for the Key field and paste the all the contents from the creds.json file into the Value field
        * Click 'Add'
        * Add another Config Var with the Key of 'PORT' and the Value of '8000'
        * Within Settings, scroll down to the Buildpacks sections, click to Add a Buildpack
        * Select Python from the pop-up window and Save
        * Add the Node.js Buildpack using the same method
        * Navigate to the Deploy section, select Github as the deployment method, and connect to GitHub when prompted
        * Use your GitHub repository name created for this project
        * Finally, scroll down to and select to deploy 'Automatically' as this will ensure each time you push code in GitHub, the pages through Heroku are updated
    1. Your application can be run from the Application Configuration section, click 'Open App'

</details>

***

### Credits

I want to my mentor Brian Macharia for all of his amazing support and guidance on how to improve my code and how to deliver a better user experience.

Support on developing ideas were derived from the following:

* The inspiration of building a recipe finder
https://www.makeuseof.com/recipe-finder-app-python/

* Inspiration from seeing flowcharts and googlesheet organisation 
https://github.com/RickofManc/vv-pizzas
https://github.com/alexkavanagh-dev/grocery_list_generator

* Deployment information taken from 
https://github.com/RickofManc/vv-pizzas

### Python libraries, software and web application

* To display recipes, flavour profile and ingredients.
[Google Sheet] (https://docs.google.com/spreadsheets/d/1QEgz7x3UKXEElsaPsE19S-WLulp7T6IgYADYWpCqXQU/edit?pli=1&gid=2115059317#gid=2115059317)

* To display colours for better visibility.
[Colorama] (https://pypi.org/project/colorama/)

* To display flow chart.
[LucidChart](https://www.lucidchart.com/pages/)

* To look for questions and solve doubts
[W3schools](https://www.w3schools.com/)
[ChatGPT] (https://chatgpt.com)

* For testing sections of code
[Python Tutor](https://pythontutor.com/)

* To validate python code
[PEP8 Validator](http://pep8online.com/)













