import os
import discord
from discord.ext import commands
from discord import Interaction
from discord import Embed
from discord import app_commands
from dotenv import load_dotenv
import utils

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

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

@bot.tree.command(name='st_roll', description='Rolls the dice')
async def roll(interaction: Interaction, qtd_dados: int, dificuldade: int = None):
    dice_rolled = utils.dice_roll(qtd_dados, dificuldade)

    embed = Embed(title='Rolagens')
    embed.add_field(name='Dados', value=', '.join(dice_rolled[0]), inline=False)
    embed.add_field(name='Sucessos', value=dice_rolled[1], inline=False)
    await interaction.response.send_message(embed=embed)

if __name__ == '__main__':
    bot.run(os.getenv('BOT_TOKEN'))