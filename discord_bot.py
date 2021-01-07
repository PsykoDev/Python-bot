import os
import random

import discord
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Haykarnaque'))
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        print(f'{message.author} : {message.content}')
        return

    msg_meow_quotes = [
        f'https://tenor.com/view/kitten-falling-kitten-falls-kitten-fall-kitten-cute-cat-gif-17563015',
        f'https://tenor.com/view/scared-kitten-kitten-phone-kitten-flip-terrified-kitten-gif-16034921',
        f'https://tenor.com/view/ajaa-gif-19469374',
        (
            f'Nothing.'
            f'Nothing.'
        ),
    ]

    if message.content == 'meow':
        print(f'{message.content}')
        response = random.choice(msg_meow_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise



client.run(TOKEN)