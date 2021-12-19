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
BOT_NAME = os.getenv('BOT_NAME')
BOT_USER_ID = int(os.getenv('BOT_USER_ID'))
ADMIN_NAME = os.getenv('ADMIN_NAME')
ADMIN_USER_ID = int(os.getenv('ADMIN_USER_ID'))

# Intents
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

# Instantiate Client
client = discord.Client(intents=intents)

@client.event
async def on_ready(): # At Bot Startup
    print('\nWe have logged in as {0.user}\n'.format(client))

    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members_print = '\n -'.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members_print}')

    members_names_ids = [(member.name, member.id) for member in guild.members]

    for member_id in members_names_ids:
        print(member_id)

# TODO: How to identify which users are in a channel.

# Talk to Donut
@client.event
async def on_message(message): # A bot that responds to messages
    if message.author == client.user:
        return

    if message.content.startswith('Donut?'):
        await message.channel.send("I'm here!")

    if message.content.startswith('get matches'):
        await message.channel.send("On it..")

        guild = discord.utils.get(client.guilds, name=GUILD)

        members_names_ids = [(member.name, member.id) for member in guild.members]

        pairs = get_pairs(members_names_ids)

        # Prettify Pairs
        pairs_names = []
        for i in range(len(pairs)):
            print('i', pairs[i])
            pair_names = []
            for j in range(2):
                print('ij', pairs[i][j])
                pair_names.append(pairs[i][j][0])
            pairs_names.append(list(pair_names))

        await message.channel.send("-- PAIRS --")

        for pair in pairs_names:
            await message.channel.send(pair)

    if message.content.startswith('Make matches!'):
        await message.channel.send("OK!")

        guild = discord.utils.get(client.guilds, name=GUILD)

        members_names_ids = [(member.name, member.id) for member in guild.members]

        pairs = get_pairs(members_names_ids)

        # Send the pairs to admin.
        # Prettify Pairs
        pairs_names = []
        for i in range(len(pairs)):
            pair_names = []
            for j in range(2):
                pair_names.append(pairs[i][j][0])
            pairs_names.append(list(pair_names))

        # Temporarily Override Admin User to be me for testing
        ADMIN_USER_ID = 752348190027808911

        admin_member = guild.get_member(ADMIN_USER_ID)
        await admin_member.create_dm()
        await admin_member.dm_channel.send("-- PAIRS --")

        for pair in pairs_names:
            await admin_member.dm_channel.send(pair)

        # TODO: Add capability to message multiple people or create a new channel of 2 + donut user

        # Now notify those that are paired:
        # member_a = guild.get_member(752348190027808911)
        # member_b = guild.get_member(681586949836111935)
        # await member_a.create_dm()
        # await member_a.dm_channel.send(
        #     f"Hi {member_a.name}, you've been matched with **{member_b.name}** for a donut chat!"
        # )
        # await member_b.create_dm()
        # await member_b.dm_channel.send(
        #     f"Hi {member_b.name}, you've been matched with {member_a.name} for a donut chat!"
        # )


# Run Client
client.run(TOKEN)
