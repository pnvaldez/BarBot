loadout_csv = 'barbot_loadout.txt'
drink_recipe_csv = "barbot_recipes.txt"
ingredient_csv = "barbot_ingredients.txt"
flowrate = 1.31 #ml/sec

import sys
import serial
import time
import csv

class Drink:
	def __init__(self, recipe_list, loadout, ser):
		self.name = recipe_list[0]
		self.recipe = recipe_list[1] #recipe is a dict, form of ingredient : servings
		self.loadout = loadout
		self.ser = ser

	def can_make(self, curr_drinks):
		for key in self.recipe:
			if key not in curr_drinks:
				return False
		return True

	def create_serial(self):
		serial_output = {}
		for i in range(len(self.loadout)):
			for key in self.recipe:
				if key == self.loadout[i]:
					pump = (i + 2) * 100 #pumps start at 2
					servings = int(self.recipe[key] * 10)
					serial_output[key] = str(pump + servings)

		return serial_output

	def make_drink(self):
		command = self.create_serial()
		print(command)
		for key in command:
			curr_output = command[key]
			curr_serving = (float(curr_output[1:])) / 10
			delay_time = (curr_serving * 29.57) / flowrate
			print("Pouring: " + key + " for " + str(curr_serving) + " ounces")
			self.ser.write(bytes(curr_output, 'utf-8'))
			time.sleep(delay_time + 3)

class Utility:
	def __init__(self, ser):
		self.loadout = self.get_loadout()
		self.ser = ser

	def get_loadout(self):
		with open(loadout_csv) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter = ',')
			for row in csv_reader:
				return row

	def make_recipe(self, input_recipe):
		output_recipe = ["", {}]
		recipe_dict = {}
		for i in range(len(input_recipe) - 1):
			if (i == 0):
				output_recipe[0] = input_recipe[0]
			if (i % 2 == 1):
				curr_key = input_recipe[i]
				ounces = input_recipe[i + 1]
				recipe_dict[curr_key] = float(ounces)
		output_recipe[1] = recipe_dict

		return output_recipe

	def get_makeable_drinks(self):
		loadout = self.get_loadout()
		drink_list = []

		with open(drink_recipe_csv) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter = ",")
			for row in csv_reader:
				curr_recipe = self.make_recipe(row)
				ingredients = curr_recipe[1]
				print(ingredients)
				makeable = True

				for key in ingredients:
					if key not in loadout:
						makeable = False

				if (makeable == True):
					drink_list.append(curr_recipe)

		return drink_list

	def get_ingredients(self):
		ingredient_list = []
		with open(ingredient_csv) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter = ",")
			for row in csv_reader:
				ingredient_list.append(row[0])
		return ingredient_list

	def change_loadout(self, new_loadout):
		with open(loadout_csv, 'w') as f:
			writer = csv.writer(f)
			writer.writerow(new_loadout)

	def send_to_arduino(self, outputs):
		for key in outputs:
			curr_output = outputs[key]
			curr_serving = (float(curr_output[1:])) / 10
			delay_time = (curr_serving * 29.57) / flowrate
			print("Pouring: " + key + " for " + str(curr_serving) + " ounces")
			self.ser.write(bytes(curr_output, 'utf-8'))
			time.sleep(delay_time + 3)

	def prime_pumps(self):
		prime_time = 5 #seconds
		serial_time = (prime_time * flowrate) / 29.57
		serial_time = int(serial_time * 10)

		serial_output = {}
		for i in range (4):
			curr_key = "PUMP_" + str(i + 1)
			serial_output[curr_key] = str(((i + 2)*100) + serial_time)

		print("Priming Pumps")
		self.send_to_arduino(serial_output)

	def flush_pumps():
		flush_time = 10 #seconds
		serial_time = (flush_time * flowrate) / 29.57
		serial_time = int(serial_time * 10)

		serial_output = {}
		for i in range (4):
			curr_key = "PUMP_" + str(i + 1)
			serial_output[curr_key] = str(((i + 2)*100) + serial_time)

		print("Flushing Pumps")
		send_to_arduino(serial_output)
