import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials

bot = commands.Bot(command_prefix='Flash!', description='Giveaway Bot!')

scope = ['Insert']
creds = ServiceAccountCredentials.from_json_keyfile_name('Insert', scope)
client = gspread.authorize(creds)

sheet = client.open("Insert").sheet1


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def Help():
	await bot.say("Here are my available commands: Flash!Name,Flash!Token." \
	 			  "In order to use Flash!Token, enter your information in the following format: Flash!Token Blurb-0x2exklj23908znmlk1." \
	 			  "'Blurb' represents your name. The numbers starting with 0 and ending with 1 representing your Flash wallet.")

@bot.command
async def Token(message):

	row = message.split("-")
	records = sheet.get_all_records()
	index = len(records)+2
	sheet.insert_row(row, index)


@bot.command()
async def Name(name):
	records = sheet.get_all_records()
	for record in records:
		if str(record['Name']) == str(name):
			await bot.say("Confirmed. {name} is in the records.")

token = ''

bot.run(token)