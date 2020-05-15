#uses the cocktaildb api to import all ingredients and drinks
#into a recipe list

import cocktaildb
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

ingredient_sheet = client.open('RecipeList').worksheet("Ingredients")
recipe_sheet = client.open('RecipeList').worksheet("Recipes")

cocktaildb_api = cocktaildb.Api('1352')

ingredient_csv = "test.txt"

def import_ingredients():
    ingredients = cocktaildb_api.List().ingredient()
    for i in ingredients:
        row = [i]
        ingredient_sheet.insert_row(row)

def import_recipes():
    #Implement cocktaildb_api.List() and updating the google spreadsheet
    pass

import_ingredients()
import_recipes()