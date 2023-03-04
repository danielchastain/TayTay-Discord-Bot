import discord
import requests
import urllib.request, json
import random
from discord.ext.commands import Bot
import time

bot = Bot("!")
client = discord.Client()


@client.event
async def on_ready():
	print('Initalizing')
	time.sleep(2)
	print('Loading packets')
	time.sleep(3)
	print('Loading websockets')
	time.sleep(1)
	print('Increasing Positivity')
	time.sleep(5)
	print('Taytay Succesfully Updated')
	time.sleep(1)
	print('Taytay Bot is Online. Now logging...\n')


@client.event
async def on_message(message):
	url = 'https://api.taylor.rest/'
	r = requests.get(url)
	r = r.text
	text_json = json.loads(r) 
	messageContent = message.content

	if message.author == client.user:
		return
	if message.content.startswith(''):
		random_number = random.randint(1, 100)
		print(message.author, " ", time.ctime(), ": ", messageContent)

		if random_number % 9 == 0:
			await message.channel.send(text_json['quote'])
			print("Taytay quote registered, the number was: ", random_number)
			
	if "toxic" in messageContent:
		random_number = random.randint(0, 6)
		messages = [
		    "Don't be toxic",
		    "Imagine being toxic.",
		    "Let's stop the hate and spread positivity",
		    "Let's stop the hate and spread positivity",
		]
		await message.channel.send(messages[random_number])
	if "Toxic" in messageContent:
		random_number = random.randint(0, 6)
		messages = [
		    "Don't be toxic", "Stop doing Austin Cosplay",
		    "Imagine being toxic.",
		    "Let's stop the hate and spread positivity",
		    "Let's stop the hate and spread positivity", "Stop Asian Hate"
		]
		await message.channel.send(messages[random_number])


    
client.run('KEYHERE')
