import discord
from discord.ext import commands, tasks
import os
import json
import time
import random
import asyncio
import requests
import glob
from discord.ext.commands import cooldown, BucketType

#--------------------------------

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="z", case_insensitive=True,intents=intents )

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
             activity=discord.Game("Drinking with Baroud!"))
    print("\nLogged in as", client.user, "\n")


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("Mataginich frr ")
    await client.process_commands(message)

@client.command()
async def cc(ctx):
  if ctx.author.id==526360392335753216:
      await ctx.reply('wi hhh')
@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
       pass

for cog in glob.glob("cogs/*.py"):
  cog = f'cogs.{cog.replace(".py","").replace("cogs/","")}'
  client.load_extension(cog)
for cog in glob.glob("animeCogs/*.py"):
  cog = f'animeCogs.{cog.replace(".py","").replace("animeCogs/","")}'
  client.load_extension(cog)
for cog in glob.glob("avoiceCogs/*.py"):
  cog = f'avoiceCogs.{cog.replace(".py","").replace("avoiceCogs/","")}'
  client.load_extension(cog)
client.run(os.getenv('TOKEN'))
 