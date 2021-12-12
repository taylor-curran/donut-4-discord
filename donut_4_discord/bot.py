import discord
import os
from dotenv import load_dotenv
import logging

# Get Logging Working
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Env Variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Intents
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

# Instantiate Client
client = discord.Client(intents=intents)

# TODO
# Me trying to figure out how to instantiate Guild so I can
# can use Guild.chunk() to get a list returned of all users
# client.get_guild()
# This is not working but I think I need to use await in order to use .chunk()...

@client.event
async def on_ready(): # At Bot Startup
    print('\nWe have logged in as {0.user}\n'.format(client))

    # Here we're assigning a local variable to our global variable
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n',
        f'{guild.name}(id: {guild.id})\n'
    )

    members_print = '\n -'.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members_print}')

    members = [member.name for member in guild.members]

    # Random Function Here

@client.event
async def on_message(message): # A bot that responds to messages
    if message.author == client.user:
        return

    if message.content.startswith('Donut?'):
        await message.channel.send("I'm here!")

# Run Client
client.run(TOKEN)

# At this point in the tutorial:
# Great! You can see the name of your bot,

# https://realpython.com/how-to-make-a-discord-bot-python/