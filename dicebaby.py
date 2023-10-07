import random
import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='', intents=intents)

# 初始化基礎點數
base_points = 1000

# 定義各種玩法的賠率
multipliers = {
    '大': 1, 
    '小': 1,
    '圍骰': 180,
    '全圍': 30,
    '單骰': 1,
    '雙骰': 2,
    '全骰': 3,
    '對子': 11,
    '牌九式': 6,
    '點數總和4': 60,
    '點數總和17': 60,
    '點數總和5': 20,
    '點數總和16': 20,
    '點數總和6': 18,
    '點數總和15': 18,
    '點數總和7': 12,
    '點數總和14': 12,
    '點數總和8': 8,
    '點數總和13': 8,
    '點數總和9': 6,
    '點數總和10': 6,
    '點數總和11': 6,
    '點數總和12': 6,
    '單': 1,
    '雙': 1,
}

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

@bot.command()
async def 骰寶(ctx, bet_type: str, bet_value: str, amount: int):
    global base_points

    if amount <= 0:
        await ctx.send("下注金額必須大於零。")
        return

    if bet_type not in multipliers:
        await ctx.send("無效的下注類型。")
        return

    if base_points < amount:
        await ctx.send("你的基礎點數不足以進行這個下注。")
        return

    dice_roll = roll_dice()
    total = sum(dice_roll)
    await ctx.send(f"骰子點數為:{dice_roll},總點數為:{total}")

    if dice_roll[0] == dice_roll[1] == dice_roll[2]:
        if bet_type == '圍骰' and bet_value == str(dice_roll[0]):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        else:
            base_points -= amount  # 輸掉下注金額
            await ctx.send(f"很遺憾,你輸了。你現在有 {base_points} 基礎點數。")
    else:
        if bet_type == '大' and total >= 11 and total <= 17:
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '小' and total >= 4 and total <= 10:
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")

            
        elif bet_type == '全圍' and dice_roll[0] == dice_roll[1] == dice_roll[2]:
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和4' and (total == 4 ):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和17' and (total == 17):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和5' and (total == 5 ):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和16' and (total == 16):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和6' and (total == 6):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和15' and (total == 15):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和7' and (total == 7):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和14' and (total == 14):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和8' and (total == 8):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和13' and (total == 13):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和9' and (total == 9):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和10' and (total == 10):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和11' and (total == 11):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '點數總和12' and (total == 12):
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '雙' and total % 2 == 0:
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        elif bet_type == '單' and total % 2 == 1:
            base_points += int(amount * multipliers[bet_type])  # 贏得下注金額,加上賠率獎勵
            await ctx.send(f"恭喜,你贏了!你現在有 {base_points} 基礎點數。")
        else:
            base_points -= amount  # 輸掉下注金額
            await ctx.send(f"很遺憾,你輸了。你現在有 {base_points} 基礎點數。")

    # 如果基礎點數歸零,結束遊戲
    if base_points <= 0:
        await ctx.send("基礎點數已歸零,遊戲結束。")

@bot.command()
async def 設定賠率(ctx, bet_type: str, new_multiplier: int):
    global multipliers
    if bet_type in multipliers:
        multipliers[bet_type] = new_multiplier
        await ctx.send(f"{bet_type} 的賠率已設置為 {new_multiplier}。")
    else:
        await ctx.send("無效的下注類型。")

# 請將下面的 'YOUR_TOKEN_HERE' 替換為你的 Discord 機器人令牌  
bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')
