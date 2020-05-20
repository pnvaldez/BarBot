import sys
import serial
import time
import csv
import RPi.GPIO as GPIO

loadout_csv = './config/barbot_loadout.txt'
drink_recipe_csv = "./config/barbot_recipes.txt"
ingredient_csv = "./config/barbot_ingredients.txt"
flowrate = 1.31 #ml/sec

#GPIO Setup
GPIO.setmode(GPIO.BCM)

pump_1 = 26
pump_2 = 19
pump_3 = 13
pump_4 = 6

pumps = {"pump_1" : pump_1, "pump_2" : pump_2, "pump_3" : pump_3, "pump_4" : pump_4}

class Drink:
	def __init__(self, recipe_list):
		self.name = recipe_list[0]
		self.recipe = recipe_list[1] #recipe is a dict, form of ingredient : servings
		self.loadout = Utility().loadout

	def can_make(self):
		for key in self.recipe:
			if key not in self.loadout:
				return False
		return True

	def create_command(self):
		command = {}
		for i in range(len(self.loadout)):
			for key in self.recipe:
				if key == self.loadout[i]:
					num = (i + 1)
					pump = "pump_" + str(num)
					serving_time = (self.recipe[key] * 28.4131) / flowrate
					command[pump] = serving_time

		return command

	def make_drink(self):
		command = self.create_command()
		print(command)
		for pump in command:
                    print(pump)
                    print("Pump:" + str(command[pump]))
                    GPIO.output(pumps[pump], 0)
                    time.sleep(command[pump])
                    GPIO.output(pumps[pump], 1)

class Utility:
	def __init__(self):
		self.loadout = self.get_loadout()

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

	def send_to_gpio(self, outputs):
		for pump in outputs:
			print("Pump:" + str(outputs[pump]))
			GPIO.output(pumps[pump], 0)
			time.sleep(outputs[pump])
			GPIO.output(pumps[pump], 1)

	def prime_pumps(self):
		prime_time = 5 #seconds
		gpio_output = {}
		for i in range (1, 5):
                    key = "pump_" + str(i)
                    gpio_output[key] = prime_time

		print("Priming Pumps")
		self.send_to_gpio(gpio_output)

	def flush_pumps(self):
		flush_time = 10 #seconds
		gpio_output = {}
		for i in range (1, 5):
                    key = "pump_" + str(i)
                    gpio_output[key] = flush_time

		print("Flushing Pumps")
		self.send_to_gpio(gpio_output)
