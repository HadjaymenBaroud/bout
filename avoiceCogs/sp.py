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
import urllib.parse

with open('db/spacetoon.txt','r') as f :
    lines = [x for x in f.readlines()]



class Hide(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()



    async def spc(self,ctx,rounds=5):
        for i in range(rounds):
           

            nmd = choice(lines).split('-/')
            url = nmd[0]
            nm = nmd[1].split('(')[0]
            nmk = []
            nmk.append(nm)

            print(nm+url)


           
           


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
                lista = map(check_true,nmk)
                if True in lista:
                    return True
                return False

            try :
                msg = await self.bot.wait_for('message', check=check ,timeout=25)
                await ctx.send(f'Congrats ,{msg.author.mention}  answered right  ')
                voice.stop()
                await voice.disconnect()
                await asyncio.sleep(2)
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


                await ctx.send('No one answered **{}** was the answer '.format(nm))
                voice.stop()
                await voice.disconnect()
                await asyncio.sleep(2)
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











def setup(bot):
    bot.add_cog(Hide(bot))
