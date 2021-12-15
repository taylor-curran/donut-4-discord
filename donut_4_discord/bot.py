import discord
import os
from dotenv import load_dotenv
import logging
from members import get_pairs

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

    pairs = get_pairs(members)

    print('PAIRS: ', pairs)



@client.event
async def on_message(message): # A bot that responds to messages
    if message.author == client.user:
        return

    if message.content.startswith('Donut?'):
        await message.channel.send("I'm here!")

    if message.content.startswith('Make matches!'):
        await message.channel.send("OK!")



# Run Client
client.run(TOKEN)
