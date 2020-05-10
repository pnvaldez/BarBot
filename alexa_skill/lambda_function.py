import boto3
import time

access_key = "KEY"
access_secret = "SECRET"
region = "us-east-2"
queue_url = "URL"

def post_message(client, message, url):
  client.send_message(QueueUrl = url, MessageBody = message)

def receive_message(client, url, previous):
  incoming = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 10)
  receipt = incoming['Messages'][0]['ReceiptHandle'] 
  response = incoming['Messages'][0]['Body']
  
  if(response == previous):
      response = "Bar Bot is busy or off, please wait or turn on Bar Bot"
      
  client.delete_message(QueueUrl = url, ReceiptHandle = receipt) 
  return response

def lambda_handler(event, context):
  end = False
  client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)
  event_type = event['request']['type']

  if(event_type == "LaunchRequest"):
    text = "Welcome to Bar Bot, ask me to make you a drink, or ask what's on tap"

  elif(event_type == "IntentRequest"):
    intent = event['request']['intent']['name']
    if(intent == "AMAZON.HelpIntent"):
      text = "I'm Bar Bot, just ask me to make you a drink, or ask what's on tap"
    elif(intent == "AMAZON.StopIntent" or intent == "AMAZON.CancelIntent"):
      text = "Goodbye"
      end = True
    elif (intent == "MakeDrink"):
      message = event['request']['intent']['slots']['Drink']['value']
      post_message(client, message, queue_url)
      time.sleep(1.5)
      text = receive_message(client, queue_url, message)
    elif (intent == "ListAvailableDrinks"):
      message = "AvailableDrinks"
      post_message(client, message, queue_url)
      time.sleep(1.5)
      text = receive_message(client, queue_url, message)

  else: 
    text = "I'm sorry, I didn't understand that. Say Help for options, or close to exit Bar Bot"

  output = {}
  output['version'] = 1.0
  output['response'] = {"outputSpeech": { "type" :"PlainText","text":text},"shouldEndSession" :end}
  return output