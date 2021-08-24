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
  
  

  async def op(self,ctx):
    try:
  
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
         return
      cc = []
      psps=[]
      def check(msg): 
        if msg.author.id == 876398362960740382 or msg.channel.id != ctx.channel.id:
          return False
        if True:
          def check_true(nma):
            
           
            similarity = difflib.SequenceMatcher(None, msg.content.lower(), nma.lower().rstrip().lstrip()).ratio()
            ratio = 0
            if len(nma) <= 10:
              ratio = 0.80
            elif len(nma) > 10 and len(nma) < 20 :
             ratio = 0.60
         
            elif len(nma) >= 20 and len(nma) < 30 :
              ratio = 0.45
         
            elif len(nma)>=30  :
              ratio = 0.35
            if similarity >= ratio:
             cc.append(True)
             psps.append(similarity)
             return True
            return False
        lista = map(check_true,nm)
        if True in lista:
         return True
        return False

      try : 
       msg = await self.bot.wait_for('message', check=check ,timeout=25)
       await ctx.send(f'Congrats ,{msg.author.mention}  answered right  ')
       voice.stop()
       await voice.disconnect()
       with open("db/pointa.json") as f:
         players = json.load(f)
       id = str(msg.author.name)
       players.setdefault("players",{})
       ids = players["players"].keys()
       if id in ids:
         players["players"][id] += 1
       else:
     
         players["players"][id] = 1 
       
       with open('db/pointa.json','w') as f:
         json.dump(players, f, ensure_ascii=False, indent=4)
       
      
         
  
      except asyncio.TimeoutError:
        

       await ctx.send('No one answered,The answers are :  **{}** was the answer '.format(' / '.join(i for i in nm)))
       voice.stop()
       await voice.disconnect()

    except Exception as e:
      print(e)
  @commands.command()
  async def leaderboard(self,ctx):
    with open('db/pointa.json') as f:
      players = json.load(f)
    embod= discord.Embed(title='Leaderboard')
    sort_leader=sorted(players["players"].items(), key=lambda x: x[1], reverse=True)
    
    index=1
    for i in sort_leader:
        embod.add_field(name=f'{index}) {i[0]}', value=f'Points: {i[1]}',inline=False)
        
        index+=1
    embod.set_footer(text='Bot By Hadjaymen Baroud | DZO#9009',icon_url=self.bot.user.avatar_url)
    embod.set_image(url='https://media.discordapp.net/attachments/851792852753186818/851840177571233842/unknown.png?width=322&height=184')
    await ctx.send(embed=embod)


  

    

 




def setup(bot): 
  bot.add_cog(Hide(bot))
