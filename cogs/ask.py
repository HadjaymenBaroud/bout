from discord.ext import commands, tasks
import discord
from random import choice
with open('db/ask','r') as f:
  b = f.read().splitlines()


class Hide(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  

  @commands.command()
  async def ask(self,ctx,*,qqs):
    await ctx.reply(f'**{choice(b)}**')
    

 




def setup(bot): 
  bot.add_cog(Hide(bot))
