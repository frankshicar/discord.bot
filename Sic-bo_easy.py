# https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py
from typing import Optional
import random
import discord
from discord import app_commands


MY_GUILD = discord.Object(id=991905864162226177)  # replace with your guild id


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)


    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')




def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]
    

@client.tree.command()
async def 大小(interaction, 你指定的種類: str):
    dice_roll = roll_dice()
    total = sum(dice_roll)
    if 你指定的種類 == '大' and total >= 11 and total <= 17:

        await interaction.response.send_message(f"骰子點數為:{dice_roll},總點數為:{total}\n恭喜,你贏了!")
    elif 你指定的種類 == '小' and total >= 4 and total <= 10:
        await interaction.response.send_message(f"骰子點數為:{dice_roll},總點數為:{total}\n恭喜,你贏了!")
    else:
        await interaction.response.send_message(f"骰子點數為:{dice_roll},總點數為:{total}\n\n很遺憾,你輸了")


async def 全圍(interaction):
    dice_roll = roll_dice()
    if dice_roll[0] == dice_roll[1] == dice_roll[2]:
        await interaction.response.send_message(f"骰子點數為:{dice_roll}\n恭喜,你贏了!")
    else:
        await interaction.response.send_message(f"骰子點數為:{dice_roll}\n很遺憾,你輸了")

@client.tree.command()
async def 點數總和(interaction, 你指定的點數: int):
    dice_roll = roll_dice()
    total = sum(dice_roll)
    if 你指定的點數 == total:
        await interaction.response.send_message(f"骰子點數為:{dice_roll},總點數為:{total}\n恭喜,你贏了!")
    else:
        await interaction.response.send_message(f"骰子點數為:{dice_roll},總點數為:{total}\n\n很遺憾,你輸了")

@client.tree.command()
async def 單雙(interaction, 你指定的種類: str):
    dice_roll = roll_dice()
    total = sum(dice_roll)
    if 你指定的種類 == '雙' and total % 2 == 0:
        await interaction.response.send_message(f"骰子點數為:{dice_roll},總點數為:{total}\n恭喜,你贏了!")
    if 你指定的種類 == '單' and total % 2 == 0:
        await interaction.response.send_message(f"骰子點數為:{dice_roll},總點數為:{total}\n恭喜,你贏了!")
    else:
        await interaction.response.send_message(f"骰子點數為:{dice_roll},總點數為:{total}\n很遺憾,你輸了")

@client.tree.command()
async def 圍骰(interaction, 你指定的點數: int):
    dice_roll = roll_dice()
    if dice_roll[0] == dice_roll[1] == dice_roll[2] and 你指定的點數 == str(dice_roll[0]):
        await interaction.response.send_message(f"你猜的圍骰是:{你指定的點數}{你指定的點數}{你指定的點數}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    else:
        await interaction.response.send_message(f"你猜的圍骰是:{你指定的點數}{你指定的點數}{你指定的點數}\n骰子點數為:{dice_roll}\n很遺憾,你輸了")



@client.tree.command()
async def 單骰(interaction, 你指定的點數: int):
    dice_roll = roll_dice()
    if dice_roll[0] == 你指定的點數:
        await interaction.response.send_message(f"你猜的是:{你指定的點數}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")        
    elif dice_roll[1] == 你指定的點數:
        await interaction.response.send_message(f"你猜的是:{你指定的點數}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")    
    elif dice_roll[2] == 你指定的點數:
        await interaction.response.send_message(f"你猜的是:{你指定的點數}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")   
    else:
        await interaction.response.send_message(f"你猜的是:{你指定的點數}\n骰子點數為:{dice_roll}\n很遺憾,你輸了")
  

@client.tree.command()
async def 雙骰(interaction, 你指定的點數: int):
    dice_roll = roll_dice()
    if dice_roll[0] == dice_roll[1] == 你指定的點數 :
        await interaction.response.send_message(f"你猜的雙骰是:{你指定的點數}出現兩次\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    elif dice_roll[0] == dice_roll[2] == 你指定的點數:
        await interaction.response.send_message(f"你猜的雙骰是:{你指定的點數}出現兩次\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    elif dice_roll[1]  == dice_roll[2] == 你指定的點數:
        await interaction.response.send_message(f"你猜的雙骰是:{你指定的點數}出現兩次\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    else:
        await interaction.response.send_message(f"你猜的雙骰是:{你指定的點數}出現兩次\n骰子點數為:{dice_roll}\n很遺憾,你輸了")


@client.tree.command()
async def 全骰(interaction, 你指定的點數: int):
    dice_roll = roll_dice()
    if dice_roll[0] == dice_roll[1] ==  dice_roll[2] == 你指定的點數 :
        await interaction.response.send_message(f"你猜的雙骰是:{你指定的點數}出現三次\n骰子點數為:{dice_roll}\n恭喜,你贏了!")             
    else:
        await interaction.response.send_message(f"你猜的雙骰是:{你指定的點數}出現三次\n骰子點數為:{dice_roll}\n很遺憾,你輸了")




@client.tree.command()
async def 短牌(interaction, 你指定的點數一: int, 你指定的點數二: int):
    dice_roll = roll_dice()    
    if dice_roll[0] == 你指定的點數一 and dice_roll[1] == 你指定的點數二:
        await interaction.response.send_message(f"你猜的是:{你指定的點數一},{你指定的點數二}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    elif dice_roll[0] == 你指定的點數一 and dice_roll[2] == 你指定的點數二:
        await interaction.response.send_message(f"你猜的是:{你指定的點數一},{你指定的點數二}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    elif dice_roll[1] == 你指定的點數一 and dice_roll[2] == 你指定的點數二:
        await interaction.response.send_message(f"你猜的是:{你指定的點數一},{你指定的點數二}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    elif dice_roll[0] == 你指定的點數二 and dice_roll[1] == 你指定的點數一:
        await interaction.response.send_message(f"你猜的是:{你指定的點數一},{你指定的點數二}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    elif dice_roll[0] == 你指定的點數二 and dice_roll[2] == 你指定的點數一 :
        await interaction.response.send_message(f"你猜的是:{你指定的點數一},{你指定的點數二}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    elif dice_roll[1] == 你指定的點數二 and dice_roll[2] == 你指定的點數一 :
        await interaction.response.send_message(f"你猜的是:{你指定的點數一},{你指定的點數二}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")
    else:
        await interaction.response.send_message(f"你猜的是:{你指定的點數一},{你指定的點數二}\n骰子點數為:{dice_roll}\n很遺憾,你輸了")


@client.tree.command()
async def 長牌(interaction, 你指定的長牌點數: int):
    dice_roll = roll_dice()
    if dice_roll[0] == dice_roll[1] == 你指定的長牌點數:
        await interaction.response.send_message(f"你猜的是:{你指定的長牌點數}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")        
    elif dice_roll[0] == dice_roll[2] == 你指定的長牌點數:
        await interaction.response.send_message(f"你猜的是:{你指定的長牌點數}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")  
    elif dice_roll[1] == dice_roll[2] == 你指定的長牌點數:
        await interaction.response.send_message(f"你猜的是:{你指定的長牌點數}\n骰子點數為:{dice_roll}\n恭喜,你贏了!")  
    else:
        await interaction.response.send_message(f"你猜的是:{你指定的長牌點數}\n骰子點數為:{dice_roll}\n很遺憾,你輸了")








client.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')




