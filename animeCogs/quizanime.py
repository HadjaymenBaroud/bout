import discord
from random import choice
import difflib
from modules.quiz import *
from modules.peta import *
import asyncio
import json
import time
from discord.ext import commands, tasks
 
with open('db/animedb.txt','r') as f:
  b = f.read().splitlines()
import asyncio

class Hide(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  

  @commands.command()
  async def story(self,ctx,rounds=5):
    if int(rounds)>=8 :
      await ctx.send('rlx bzf rounds haka dir a9al mn 8 ')
      return 
      rounds=0
    for i in range(0,int(rounds)):
    
     infos =anime_info(randomanime()) 
     poster = infos[2]
     name = infos[7]
     nm = infos[12]

     nm.append(name)
     embed = discord.Embed(title = 'Guess The Anime Name !') 
     embed.add_field(name='The Story : ',value=f"**{poster}**")

     await ctx.send(embed=embed)
     cc = []
     psps = []
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
       msg = await self.bot.wait_for('message', check=check ,timeout=15)
       await ctx.send(f'Congrats ,{msg.author.mention}  answered right  **You got a Point**')
       with open("db/points.json") as f:
         players = json.load(f)
       id = str(msg.author.name)
       players.setdefault("players",{})
       ids = players["players"].keys()
       if id in ids:
         players["players"][id] += 1
       else:
     
         players["players"][id] = 1 
       
       with open('db/points.json','w') as f:
         json.dump(players, f, ensure_ascii=False, indent=4)
    except asyncio.TimeoutError:

       await ctx.send('No one answers,The answers are :  **{}** was the answer '.format(' / '.join(i for i in nm)))
    
       
   
     
    with open('db/points.json') as f:
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

    del players["players"]

    with open('db/points.json','w') as f:
       json.dump(players, f, ensure_ascii=False, indent=4)

     
    # asyncio.TimeoutError: a



def setup(bot): 
  bot.add_cog(Hide(bot))
