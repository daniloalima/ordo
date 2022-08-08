from http import client
import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
import utils

load_dotenv()

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
    logger.info(f"logged in as {client.user}")

@client.event
async def on_message(message):
    content = message.content
    if message.author == client.user:
        logger.info("message sent by bot itself, ignoring...")
        return

    if content.startswith('!o'):
        fields = content.split(' ')
        try:
            dice_pool = int(fields[1])
            modifier = int(fields[2])
            dt = int(fields[3])
        except IndexError as e:
            logger.warning(f"invalid fields for {message.author} message threw the exception bellow... \n {e}")
            await message.channel.send("Campos inválidos!")
            return

        response = utils.dice_roll(dice_pool,modifier,dt)
        logger.info(f"rolling dice for {message.author}...")
        await message.channel.send(response)
        return

    elif content.startswith('ordo!ping'):
        logger.info(f'running ping command by {message.author}...')
        response = f'Pong! {round(client.latency * 1000)}ms'
        await message.channel.send(response)
        return


client.run(os.environ["BOT_TOKEN"])
