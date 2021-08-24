from discord.ext import commands, tasks
import discord
from random import choice
from modules.quiz import *
with open('db/zahrk','r') as f:
  b = f.read().splitlines()


class Hide(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  

  @commands.command()
  @commands.cooldown(1, 2, commands.cooldowns.BucketType.guild)
  async def ahrk(self,ctx):

      await ctx.reply(f'**{choice(b)}**')
    

 




def setup(bot): 
  bot.add_cog(Hide(bot))
