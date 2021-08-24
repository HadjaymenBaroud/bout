from discord.ext import commands, tasks
import discord
from random import choice
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import urllib.request
import re
from random import choice
import difflib
from modules.quiz import *
from modules.peta import *
import json
import asyncio
class Hide(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  

  @commands.command()
  
  

  async def rop(self,ctx):
  
      infos = anime_info(randomanime()) 
      nm = infos[12]
      nm.append(infos[7])
      cs = infos[7].replace(' ','+')
    
      html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={cs}+opening")
      video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
      url = "https://www.youtube.com/watch?v=" + video_ids[0]



      YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      voice = await ctx.message.author.voice.channel.connect()
 

      if not voice.is_playing():
         with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
      else:
         await ctx.send("Already playing song")
    




def setup(bot): 
  bot.add_cog(Hide(bot))
