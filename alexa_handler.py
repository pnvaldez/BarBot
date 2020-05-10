import boto3
import os
import time

from barbot_classes import *
from find_arduino_port import get_ports, find_arduino

flowrate = 1.31 #ml/sec

found_ports = get_ports()        
arduino_port = find_arduino(found_ports)

if arduino_port != 'None':
    ser = serial.Serial(arduino_port, baudrate = 9600, timeout=1)
    print('Connected to ' + arduino_port)

else:
    print('Connection Issue!')

time.sleep(2)
ser.write(bytes(str(flowrate), 'utf-8'))

utility = Utility(ser)
drink_list = utility.get_makeable_drinks()
  
access_key = "KEY"
access_secret = "SECRET"
region = "us-east-2"
queue_url = "URL"

waittime = 1
client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)
client.set_queue_attributes(QueueUrl = queue_url, Attributes = {'ReceiveMessageWaitTimeSeconds': str(waittime)})


class AlexaHandler():
	def __init__(self, client, url, ser):
		self.ser = ser
		self.utility = Utility(self.ser)
		self.client = client
		self.url = url

	def available_drinks(self):
		drink_list = self.utility.get_makeable_drinks()
		response = ""
		drink_str = ""
		for drink in drink_list:
			drink_str = drink_str + drink[0] + ", "
		if (drink_str == ""):
			response = "Bar Bot cannot make anything right now. Please update the loadout"
		else:
			response = "Here are the drinks that Bar Bot can make, " + drink_str

		#print(response)
		self.post_message(response)

	def drink_response(self, drink):
		makeable = False
		recipe = []
		response = "Bar Bot cannot make your " + drink
		drink_list = self.utility.get_makeable_drinks()
		for curr_recipe in drink_list:
			curr_drink = curr_recipe[0]
			if (drink.lower() == curr_drink.lower()):
				recipe = curr_recipe
				makeable = True
				response = "Bar Bot is making your " + drink

		#print(response)
		self.post_message(response)
		return [makeable, recipe]

	def post_message(self, message):
		self.client.send_message(QueueUrl = self.url, MessageBody = message)

	def receive_message(self):
		response = self.client.receive_message(QueueUrl = self.url, MaxNumberOfMessages = 10)
		message = response['Messages'][0]['Body']
		receipt = response['Messages'][0]['ReceiptHandle']
		client.delete_message(QueueUrl = self.url, ReceiptHandle = receipt)
		return message



def check_sqs():
	alexa = AlexaHandler(client, queue_url, ser)
	while True:
		print("Checking...")
		time.sleep(1)
		try:
			alexa = AlexaHandler(client, queue_url, ser)
			message = alexa.receive_message()
			print("SQS Recieved a message from Alexa")
			print(message)

			if (message == "AvailableDrinks"):
				alexa.available_drinks()
				time.sleep(3)
			else:
				recipe = alexa.drink_response(message)
				if (recipe[0] == True):
					loadout = alexa.utility.get_loadout()
					drink = Drink(recipe[1], loadout, alexa.ser)
					drink.make_drink()
				else:
					time.sleep(3)

		except:
			print("Nothing is there")
			pass

check_sqs()