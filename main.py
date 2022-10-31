import discord
import os
from dotenv import load_dotenv, find_dotenv
from bot_commands import Commands

client = discord.Client(intents=discord.Intents.default())

load_dotenv(find_dotenv('.env'))

client.run(os.getenv('MY_TOKEN'))


@client.event
async def on_ready():
    print('Logged in as {0.user}.format(client)')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.startswith('!'):
        cmd = Commands(message).isCommand()
        if cmd is True:
            await client.send(cmd)
        return
