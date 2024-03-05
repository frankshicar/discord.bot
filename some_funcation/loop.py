# from discord.ext import commands 
# import discord
# import asyncio

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')
    
# @bot.command()
# async def loop(ctx, time_interval: int, *, reason=""):
#     # 将时间间隔限制在最小值（例如，5秒）以及您认为合适的最大值之间
#     time_interval = max(5, time_interval)
    
#     while True:
#         await ctx.send(f"{ctx.author.mention} {reason}")
#         await asyncio.sleep(time_interval)

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')


#迴圈機器人
# from discord.ext import commands 
# import discord
# import asyncio
# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!',intents=intents)

# @bot.event
# async def on_ready():
#   channel = bot.get_channel(1119524353030234192)
  
#   asyncio.create_task(my_background_task(channel))
  
# async def my_background_task(channel):

#   while True:
#      print(channel) 
#      await channel.send("poker來打apex")
     
#      await asyncio.sleep(10)

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')


