# import random
# import discord
# from discord.ext import commands

# intents = discord.Intents.default()
# intents.typing = False
# intents.presences = False

# bot = commands.Bot(command_prefix='', intents=intents)

# def roll_dice():
#     return [random.randint(1, 6) for _ in range(3)]

# @bot.command()
# async def 骰寶(ctx, bet_type: str, bet_value: str):
#     dice_roll = roll_dice()
#     total = sum(dice_roll)
#     await ctx.send(f"骰子點數為：{dice_roll}，總點數為：{total}")

#     if dice_roll[0] == dice_roll[1] == dice_roll[2]:
#         if bet_type == '豹子' and bet_value == str(dice_roll[0]):
#             await ctx.send("恭喜，你贏了！")
#         else:
#             await ctx.send("很遺憾，你輸了。")
#     else:
#         if bet_type == '總和' and bet_value == str(total):
#             await ctx.send("恭喜，你贏了！")
#         elif bet_type == '大小':
#             if total >= 4 and total <= 10 and bet_value == '小':
#                 await ctx.send("恭喜，你贏了！")
#             elif total >= 11 and total <= 17 and bet_value == '大':
#                 await ctx.send("恭喜，你贏了！")
#             else:
#                 await ctx.send("很遺憾，你輸了。")
#         elif bet_type == '單雙':
#             if total % 2 == 0 and bet_value == '雙':
#                 await ctx.send("恭喜，你贏了！")
#             elif total % 2 == 1 and bet_value == '單':
#                 await ctx.send("恭喜，你贏了！")
#             else:
#                 await ctx.send("很遺憾，你輸了。")
#         else:
#             await ctx.send("很遺憾，你輸了。")

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')





# import random
# import discord
# from discord.ext import commands


# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!',intents=intents)

# def roll_dice():
#     return random.randint(1, 6)

# @bot.command()
# async def dice(ctx, bet_type: str, bet_value: str):
#     if bet_type not in ['豹子','總和','單雙','大小'] :
#         await ctx.send('無效的猜測，請輸入 "豹子"、 "總和"、"單雙"或"大小"。')
#         return
#     elif bet_type == '總和' and int(bet_value) not in [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
#         await ctx.send('無效的猜測，請輸入"總和"及3~18其中一數字。')
#         return
#     elif bet_type == '豹子' and int(bet_value) not in [1,2,3,4,5,6]:
#         await ctx.send('無效的猜測，請輸入"豹子"及1~6其中一數字。')
#         return
#     elif bet_type in ['單雙'] and bet_value not in ['單','雙']:
#         await ctx.send('無效的猜測，請輸入"單雙"及"單"或"雙"。')
#         return
#     elif bet_type in ['大小'] and bet_value not in ['大','小']:
#         await ctx.send('無效的猜測，請輸入"大小"及"大"或"小"。')
#         return
    
    
    

#     dice_roll = [roll_dice(), roll_dice(), roll_dice()]
#     total = sum(dice_roll)
#     await ctx.send(f"骰子點數為：{dice_roll}，總點數為：{total}")

#     if dice_roll[0] == dice_roll[1] == dice_roll[2]:
#         if bet_type == '豹子' and bet_value == str(dice_roll[0]):
#             await ctx.send("恭喜，你贏了！")
#         else:
#             await ctx.send("很遺憾，你輸了。")
#     else:
#         if bet_type == '總和' and bet_value == str(total):
#             await ctx.send("恭喜，你贏了！")
#         elif bet_type == '大小':
#             if total >= 4 and total <= 10 and bet_value == '小':
#                 await ctx.send("恭喜，你贏了！")
#             elif total >= 11 and total <= 17 and bet_value == '大':
#                 await ctx.send("恭喜，你贏了！")
#             else:
#                 await ctx.send("很遺憾，你輸了。")
#         elif bet_type == '單雙':
#             if total % 2 == 0 and bet_value == '雙':
#                 await ctx.send("恭喜，你贏了！")
#             elif total % 2 == 1 and bet_value == '單':
#                 await ctx.send("恭喜，你贏了！")
#             else:
#                 await ctx.send("很遺憾，你輸了。")
#         else:
#             await ctx.send("很遺憾，你輸了。")

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')





# import random
# import discord
# from discord.ext import commands

# intents = discord.Intents.all()


# bot = commands.Bot(command_prefix='!', intents=intents)

# def roll_dice():
#     return random.randint(1, 6)

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# @bot.command()
# async def 猜大小(ctx, guess: str):
#     # guess = guess.lower()

#     if guess not in ['大', '小']:
#         await ctx.send('無效的猜測，請輸入 "大" 或 "小"。')
#         return

#     first_roll = roll_dice()
#     second_roll = roll_dice()
#     total = first_roll + second_roll

#     await ctx.send(f'第一次骰子點數：{first_roll}')
#     await ctx.send(f'第二次骰子點數：{second_roll}')
#     await ctx.send(f'點數總和：{total}')

#     if (guess == '大' and total >= 9) or (guess == '小' and total <= 8):
#         await ctx.send('恭喜，你猜對了！')
#     else:
#         await ctx.send('很遺憾，你猜錯了。')

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')




import random
import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='', intents=intents)

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

@bot.command()
async def 骰寶(ctx, bet_type: str, bet_value: str):
    dice_roll = roll_dice()
    total = sum(dice_roll)
    await ctx.send(f"骰子點數為:{dice_roll},總點數為:{total}")

    if dice_roll[0] == dice_roll[1] == dice_roll[2]:
        if bet_type == '圍骰' and bet_value == str(dice_roll[0]):
            await ctx.send(f"恭喜,你贏了!")
        else:
            await ctx.send(f"很遺憾,你輸了。")
    else:
        if bet_type == '大' and total >= 11 and total <= 17:
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '小' and total >= 4 and total <= 10:
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '全圍' and dice_roll[0] == dice_roll[1] == dice_roll[2]:
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和4' and (total == 4 ):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和17' and (total == 17):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和5' and (total == 5 ):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和16' and (total == 16):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和6' and (total == 6 ):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和15' and (total == 15):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和7' and (total == 7):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和14' and (total == 14):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和8' and (total == 8):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和13' and (total == 13):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和9' and (total == 9):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和10' and (total == 10):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和11' and (total == 11):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '點數總和12' and (total == 12):
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '雙' and total % 2 == 0:
            await ctx.send(f"恭喜,你贏了!")
        elif bet_type == '單' and total % 2 == 1:
            await ctx.send(f"恭喜,你贏了!")
        else:
            await ctx.send(f"很遺憾,你輸了。")

# 請將下面的 'YOUR_TOKEN_HERE' 替換為你的 Discord 機器人令牌  
bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')
