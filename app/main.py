# This example requires the 'message_content' intent.

import discord
from os import getenv

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "KoggersBot" in message.content:
        await message.channel.send("https://tenor.com/view/breaking-bad-bb-jesse-jesse-yeah-bitch-yeah-bitch-gif-15852209")

DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")
client.run(DISCORD_BOT_TOKEN)
