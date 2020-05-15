import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

ingredient_sheet = client.open('RecipeList').worksheet("Ingredients")
recipe_sheet = client.open('RecipeList').worksheet("Recipes")


ingredient_csv = "barbot_ingredients.txt"
recipe_csv = "barbot_recipes.txt"

def ingredients():
    with open(ingredient_csv, 'w') as f:
        all_ingredients = ingredient_sheet.get_all_values()
        writer = csv.writer(f)
        writer.writerow(["None"])
        for ingredient in all_ingredients:
            writer.writerow(ingredient)

def recipes():
    with open(recipe_csv, 'w') as f:
        writer = csv.writer(f)
        for i in range(2, recipe_sheet.row_count):
            recipe = recipe_sheet.row_values(i)
            if (recipe == []):
                break
            else:
                writer.writerow(recipe)

def loadout():
    pass      