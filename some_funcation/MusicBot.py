# import discord
# from discord.ext import commands
# from discord.voice_client import VoiceClient

# intents = discord.Intents.default()
# intents.message_content = True

# bot = commands.Bot(command_prefix='!', intents=intents)


# @bot.command()
# async def play(ctx, url):
#     channel = ctx.author.voice.channel
#     voice_client = await channel.connect()
    
#     player = await voice_client.create_ytdl_player(url)
#     player.start()
    
# @play.error
# async def play_error(ctx, error):
#     await ctx.send(f'Error: {error}')
    


# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')



# import discord
# from discord.ext import commands
# from discord.voice_client import VoiceClient
# import yt_dlp as youtube_dl




# intents = discord.Intents.default()
# intents.message_content = True

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# async def play(ctx, url):
#     channel = ctx.author.voice.channel
    
#     if not ctx.voice_client:
#         voice_client = await channel.connect()
#     else:
#         voice_client = ctx.voice_client
    
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }
    
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)
#         url2 = info['formats'][0]['url']
    
#     FFMPEG_OPTIONS = {
#         'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
#         'options': '-vn',
#     }
    
#     voice_client.play(discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS))
    
# @play.error
# async def play_error(ctx, error):
#     await ctx.send(f'错误：{error}')

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')






# import discord
# from discord.ext import commands
# import youtube_dl
# import opuslib

# intents = discord.Intents.default()
# intents.message_content = True

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# async def play(ctx, url):
#     channel = ctx.author.voice.channel

#     voice_client = await channel.connect()

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }

#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)
#         url2 = info['formats'][0]['url']

#     FFMPEG_OPTIONS = {
#         'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
#         'options': '-vn',
#     }

#     voice_client.play(discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS))

# @play.error
# async def play_error(ctx, error):
#     await ctx.send(f'错误：{error}')

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')





# import discord
# from discord.ext import commands


# intents = discord.Intents.default()
# intents.message_content = True

# client = commands.Bot(command_prefix="!", intents=intents)

# playing_list = []

# @client.event
# async def on_ready():
#     print('Bot is ready. Logged in as', client.user)

# @client.command()
# async def join(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if ctx.author.voice is None:
#         await ctx.send("You are not connected to any voice channel")
#     elif voice is None:
#         voiceChannel = ctx.author.voice.channel
#         await voiceChannel.connect()
#     else:
#         await ctx.send("Bot is already connected to a voice channel")

# @client.command()
# async def leave(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice is None:
#         await ctx.send("Bot is not connected to a voice channel")
#     else:
#         await voice.disconnect()

# @client.command()
# async def play(ctx, url: str = ""):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
#     if voice is None:
#         await ctx.send("Bot is not connected to a voice channel. Use the !join command first.")
#         return
    
#     if voice.is_playing():
#         playing_list.append(url)
#         print(playing_list)
#         await ctx.send("Inserted song into playing_list")
#     else:
#         voice.play(discord.FFmpegPCMAudio(url), after=lambda x: endSong(voice, "song.mp4"))

# def endSong(voice, path):
#     if len(playing_list) != 0:
#         url = playing_list[0]
#         del playing_list[0]
#         voice.play(discord.FFmpegPCMAudio(url), after=lambda x: endSong(voice, "song.mp4"))


# client.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')


# import discord
# from discord.ext import commands
# from discord.utils import get
# import youtube_dl

# intents = discord.Intents.default()
# intents.message_content = True

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# async def join(ctx):
#     channel = ctx.author.voice.channel
#     await channel.connect()

# @bot.command()
# async def leave(ctx):
#     voice_client = get(bot.voice_clients, guild=ctx.guild)
#     if voice_client.is_connected():
#         await voice_client.disconnect()

# @bot.command()
# async def play(ctx, url):
#     voice_client = get(bot.voice_clients, guild=ctx.guild)
    
#     if not voice_client.is_playing():
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',
#             }],
#         }
        
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#             url2 = info['formats'][0]['url']
        
#         FFMPEG_OPTIONS = {
#             'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
#             'options': '-vn',
#         }
        
#         voice_client.play(discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS))
#     else:
#         await ctx.send("Bot is already playing a song.")

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')




import discord
from discord.ext import commands
import youtube_dl


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def play(ctx, url):

  channel = ctx.author.voice.channel
  voice_client = await channel.connect()

  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',  
    }],
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False) 
    url2 = info['formats'][0]['url']

  print(url2)

  # 后续播放音频的代码

@play.error
async def error(ctx, error):
  print(error)


bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')
