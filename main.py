import os
import discord
from discord.ext import commands
from discord import Interaction
from discord import Embed
from discord import app_commands
from dotenv import load_dotenv
import utils

load_dotenv()

bot = commands.Bot(command_prefix='ordo!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='sync', description='sync commands')
async def sync(ctx):
    synced = await bot.tree.sync()
    await ctx.send(f'Synced {len(synced)} commands')

@bot.tree.command(name='ping', description='Returns latency')
async def ping(interaction: Interaction):
    await interaction.response.send_message(f'Pong! {round(bot.latency * 1000)}ms')

@bot.tree.command(name='roll', description='Rolls the dice')
async def roll(interaction: Interaction, dice_pool: int, modifier: int, dt: int = None):
    dice_rolled = utils.dice_roll(dice_pool, modifier, dt)

    embed = Embed(title='Rolagens')
    embed.add_field(name='Dados', value=dice_rolled[0], inline=False)
    embed.add_field(name='Valor final', value=dice_rolled[1], inline=False)
    embed.add_field(name='Resultado', value=dice_rolled[3], inline=False) if dt is not None else None
    embed.colour = dice_rolled[2] if dt is not None else None
    await interaction.response.send_message(embed=embed)

if __name__ == '__main__':
    bot.run(os.getenv('BOT_TOKEN'))