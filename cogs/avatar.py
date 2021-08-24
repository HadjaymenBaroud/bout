from discord.ext import commands, tasks
import discord
from random import choice
import datetime

class Hide(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  

  @commands.command()
  async def ravatar(self,ctx):
    member = choice(ctx.message.channel.guild.members)
    embed = discord.Embed(title=f'{member.name}\'s avatar', description='', color=0x6F004A, timestamp = datetime.datetime.utcnow())
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}') 

    await ctx.send(embed=embed)
    

 




def setup(bot): 
  bot.add_cog(Hide(bot))
