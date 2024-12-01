# Recipe Finder LoCo

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

## Current Features

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









