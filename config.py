from dotenv import dotenv_values
from discord.ext import commands
from discord import Intents

# Imports secret keys and ID from the .env file
config = dotenv_values(".env")
token = config.get('TOKEN')
channel_id = int(config.get('CHANNEL_ID'))

# Creates and configures the Discord client
intents = Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)
