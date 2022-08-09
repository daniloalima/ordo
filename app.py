import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
import utils
from keep_alive import keep_alive

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
async def on_message(ctx):
    content = ctx.content
    if ctx.author == client.user:
        logger.info("message sent by bot itself, ignoring...")
        return

    if content.startswith('!o'):
        fields = content.split(' ')
        try:
            dice_pool = int(fields[1])
            modifier = int(fields[2])
            dt = int(fields[3])
        except IndexError as e:
            logger.warning(f"invalid fields for {ctx.author} message threw the exception bellow... \n {e}")
            await ctx.channel.send("Campos inválidos!")
            return

        dice_info = utils.dice_roll(dice_pool,modifier,dt)

        embed_image = discord.Embed(
            title = f'{ctx.author} rolou...',
            color=dice_info[3],
        )
        embed_image.add_field(name="**Dados**", value=dice_info[0], inline=True)
        embed_image.add_field(name="**Modificador**", value=modifier, inline=True)
        embed_image.add_field(name="**Dificuldade**", value=dt, inline=True)
        embed_image.add_field(name="**Rolagem final:**", value=dice_info[5]+modifier)
        embed_image.add_field(name="**Resultado:**", value=dice_info[4])
        embed_image.set_thumbnail(url=dice_info[2])

        logger.info(f"rolling dice for {ctx.author}...")
        await ctx.channel.send(embed=embed_image)
        return

    elif content.startswith('ordo!ping'):
        logger.info(f'running ping command by {ctx.author}...')
        response = f'Pong! {round(client.latency * 1000)}ms'
        await ctx.channel.send(response)
        return

keep_alive()
client.run(os.environ["BOT_TOKEN"])
