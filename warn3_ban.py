# import discord
# from discord.ext import commands

# intents = discord.Intents.default()
# intents.members = True

# bot = commands.Bot(command_prefix="!", intents=intents) 

# warns = {} # 警告计数

# @bot.command()
# @commands.has_permissions(ban_members=True)
# async def warn(ctx, member: commands.MemberConverter):
  
#   if member.name not in warns:
#     warns[member.id] = 1
#   else:
#     warns[member.id] += 1

#   await ctx.send(f"{member.name} ")

#   if warns[member.id] == 3:
#     await member.ban()
#     await ctx.send(f"{member.name} 因達到3次警告而被ban!")
    
# @bot.event
# async def on_ready():
#   print("Bot is ready.")




# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')



# from discord.ext import commands
# import discord

# intents = discord.Intents.all()



# bot = commands.Bot(command_prefix='!', intents=intents)

# warns = {} # 警告计数

# @bot.command()
# @commands.has_permissions(ban_members=True)
# async def warn(ctx, member: commands.MemberConverter):


#     if member.id not in warns:
#         warns[member.id] = 1 
#     else:
#         warns[member.id] += 1

#     await ctx.send(f"{member.name} 已獲得 {warns[member.id]} 次警告!")

#     if warns[member.id] == 3:
#         await member.ban()
#         await ctx.send(f"{member.name} 因達到3次警告而被ban!")



# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')