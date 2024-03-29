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

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

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
        except IndexError as error:
            logger.warning(f"invalid fields for {ctx.author} message threw the exception bellow...\n {error}")
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
        embed_image = discord.Embed(
            title = 'Ping...',
            color=0x492ea4,
        )
        logger.info(f'running ping command by {ctx.author}...')
        embed_image.add_field(name="**Pong!**", value=f'{round(client.latency * 1000)}ms')
        await ctx.channel.send(embed=embed_image)
        return

    elif content.startswith('!ro'):
        fields=content.split(' ')
        dice_info = utils.other_dice(fields[1])
        embed_image = discord.Embed(
            color=0x492ea4
        )
        embed_image.add_field(name="**Dados**", value=dice_info[0], inline=True)
        embed_image.add_field(name="**Total**", value=dice_info[3], inline=True)
        await ctx.channel.send(embed=embed_image)
        return

if __name__ == "__main__":
    client.run(os.environ["BOT_TOKEN"])
