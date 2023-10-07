# # commad版本
# import discord


# from discord.ext import commands 

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='',intents=intents)

# @bot.command()
# async def hello(ctx):
#     await ctx.send('Hello, World!')
# @bot.command()
# async def bye(ctx):
#     await ctx.send('ByeBye~')
    
# @bot.event
# async def hello(ctx):
#     if ctx.author == bot.user:
#         return
#     if ctx.content.startswith('$hello'):
#         await ctx.channel.send('Hello!')

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')


# event版本
# from discord.ext import commands 
# import discord

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='',intents=intents)

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('hello'):
#         await message.channel.send('Hello, World!')

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')



# 查看username and id
# from discord.ext import commands
# import discord

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# async def userinfo(ctx, member: commands.MemberConverter):

#     roles = [role.name for role in member.roles[1:]]

#     await ctx.send(
#         f"User name: {member.name}\n"
#         f"User ID: {member.id}\n"
#         f"Joined at: {member.joined_at}\n" 
#         f"Roles: {', '.join(roles)}"
#     )



# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')




#將成員踢出伺服器並加入黑名單
# from discord.ext import commands
# import discord

# intents = discord.Intents.all()

# bot = commands.Bot(intents=intents)


# @bot.command()
# @commands.has_permissions(ban_members=True)
# async def ban(ctx, member: commands.MemberConverter):
#     await member.ban()
#     await ctx.send(f'{member.name} has been banned.')

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')





# 禁言分鐘 解禁言
# from discord.ext import commands
# import discord
# import datetime 

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!',intents=intents)

# @bot.command()
# @commands.has_permissions(manage_roles=True)  # 只有管理員才能使用這個指令
# async def timeout(ctx, member: commands.MemberConverter, minutes: int):
#     await member.edit(timed_out_until=discord.utils.utcnow() + datetime.timedelta(minutes=minutes))
#     await ctx.send(f'{member.name}已被設定超時時間，將在{minutes}分鐘後解除超時。')

# @bot.command()
# @commands.has_permissions(manage_roles=True)
# async def remove_timeout(ctx, member: commands.MemberConverter):
#     await member.edit(timed_out_until=discord.utils.utcnow())  # 使用已知的 UTC 時間
# #     await ctx.send(f'{member.name}的超時已被解除。')
# import discord
# from discord.ext import commands
# import datetime

# intents = discord.Intents.all() 

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()  
# @commands.has_permissions(manage_roles=True)
# async def timeout(ctx, member: discord.Member, seconds: int):

#   await member.edit(timed_out_until=discord.utils.utcnow() + datetime.timedelta(seconds=seconds))

#   await ctx.send(f"{member.mention} 已被設定超時 {seconds} 秒。")


# @bot.command()
# @commands.has_permissions(manage_roles=True)  
# async def remove_timeout(ctx, member: discord.Member):

#   await member.edit(timed_out_until=None)  

#   await ctx.send(f"已解除 {member.mention} 的超時。")

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')




#迴圈機器人
# from discord.ext import commands 
# import discord
# import asyncio


# class MyClient(discord.Client):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     async def setup_hook(self) -> None:
#         # create the background task and run it in the background
#         self.bg_task = self.loop.create_task(self.my_background_task())

#     async def on_ready(self):
#         print(f'Logged in as {self.user} (ID: {self.user.id})')
#         print('------')

#     async def my_background_task(self):
#         await self.wait_until_ready()
#         counter = 0
#         channel = self.get_channel(991905864162226177)  # channel ID goes here
#         while not self.is_closed():
#             counter += 1
#             await channel.send(counter)
#             await asyncio.sleep(10)  # task runs every 60 seconds


# client = MyClient(intents=discord.Intents.all())
# client.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')
  



#骰子
# 
# slap隨機一個人
# from discord.ext import commands 
# import discord
# import random

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!',intents=intents)


# class Slapper(commands.Converter):
#     async def convert(self, ctx, argument):
#         to_slap = random.choice(ctx.guild.members)
#         return f'{ctx.author} slapped {to_slap} because *{argument}*'

# @bot.command()
# async def slap(ctx, *, reason: Slapper):
#     await ctx.send(reason)
# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')




# 查看guild ID
# from discord.ext import commands 
# import discord

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!',intents=intents)


# @bot.command()
# async def getguild(ctx):
#     await ctx.send(f'guild id: {ctx.guild.id}')

# import re

# @bot.command()  
# async def userinfo(ctx, user_mention):

#     user_id = re.search(r'\d+', user_mention).group()
  
#     user = await bot.fetch_user(user_id)
#     guild = ctx.guild
#     member = await guild.fetch_member(user_id)
#     roles = member.roles
#     roles = roles[1:]  
#     joined_at = member.joined_at

#     await ctx.send(f"User name: {user.name}\n, ID: {user.id}\n, 身份組：{[r.name for r in roles]}\n, Join time{joined_at}")


#can't do
# import re
# @bot.command()
# async def userinfo(ctx, user_mention):
#   role_names = re.findall(r'\| (\w+)', user_mention)  
#   await ctx.send(f"Roles: {', '.join(role_names)}")
# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')



# from discord.ext import commands 
# import discord
# import re

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!',intents=intents)

# @bot.command()
# async def get_roles(ctx, user_mention):

#   # 1. 提取使用者ID
#     user_id = re.search(r'\d+', user_mention).group()

#   # 2. 獲取Member
#     member = ctx.guild.get_member(int(user_id))

#   # 3. 獲取身份組
#     roles = member.roles

#     roles = roles[1:]  

#   # 4. 傳送身份組
#     await ctx.send(f"該使用者的身份組:")
#     for role in roles:
#         await ctx.send(role.name)

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')





# from discord.ext import commands 
# import discord

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!',intents=intents)
# @bot.command()
# async def serverinfo(ctx, guild: commands.GuildConverter = None):
#     if guild is None:
#         guild = ctx.guild
#     await ctx.send(f'{guild.id} ')

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')




# from discord.ext import commands
# import discord

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!',intents=intents)

# @bot.event
# async def on_ready():
#     print('Logged in as')
#     print(bot.user.name)
#     print(bot.user.id)
#     print('------')

# @bot.command()
# @commands.has_permissions(ban_members=True)
# async def ban(ctx, member: commands.MemberConverter):
#     await member.ban()
#     await ctx.send(f'{member.name} has been banned.')

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')
