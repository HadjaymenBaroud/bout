from discord.ext import commands, tasks
from modules.premiere import pos

import discord
import os


color = os.getenv('color')


class PickCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bpl(self, ctx):
      b = pos()
      
      c = ''
      for i in range(0,20):
        c+=f'**{b[1][i]}-{b[0][i]} : {b[2][i]}** \n'
      embed= discord.Embed(title='Premier League Table',description=c)
      
      embed.set_image(url='https://dc6vmiz8c91pk.cloudfront.net/media/131/12584965286018/epremier_league_banner.png')
      await ctx.send(embed=embed)
      
      



def setup(bot):
    bot.add_cog(PickCommands(bot))
