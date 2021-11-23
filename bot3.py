import discord

intents = discord.Intents.default()
intents.members = True

# async for ... in fetch_members(*, limit=1000, after=None)
# await chunk(*, cache=True)¶

import discord

client = discord.Client()
guild = discord.Guild(data=data, state=state)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('HERE', guild.members)
    members = await
    guild.fetch_members(limit=150).flatten()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Donut?'):
        await message.channel.send("Yes! I'm here!")

client.run('your token here')