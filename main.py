import discord
import os
import utils
import random

client = discord.Client()

@client.event
async def on_ready():
  print('\n\nlogged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  msg = message.content

  if msg.startswith('!o'):
    fields = msg.split(' ')
    try:
      dice_pool = int(fields[1])
      modifier = int(fields[2])
      dt = int(fields[3])
    except Exception as e:
      print('missing fields')

    reply = utils.dice_roll(dice_pool,modifier,dt)

    await message.channel.send(reply)

  elif msg.startswith('ordo!help'):
    reply = utils.help_command()
    await message.channel.send(reply)

  elif msg.startswith('ordo!ping'):
    reply = f'Pong! {round(client.latency * 1000)}ms'
    await message.channel.send(reply)

client.run(os.getenv('BOT_TOKEN'))