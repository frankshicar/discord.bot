# https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py
import discord
from discord.ext import commands
from discord import app_commands
import mysql.connector
import yaml

# 讀取 config.yml 文件
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

bot_token = config['bot_token']
MY_GUILD = discord.Object(id=config['guild_id'])

# 資料庫連接設置
mydb = mysql.connector.connect(
  host="localhost",        # 例如 "localhost"
  user="root",    # 例如 "root"
  password="frank0403",
  database="discord_player"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM players")
myresult = mycursor.fetchall()
warns = {} # 警告计数


intents = discord.Intents.all()

class MyClient(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def setup_hook(self):
        # 在這裡設定您的斜杠命令
        await self.tree.sync(guild=MY_GUILD)

client = MyClient(command_prefix="", intents=intents)

# 斜杠命令 - 警告成員
@client.tree.command(name="warn", description="對成員發出警告")
@app_commands.describe(member="要警告的成員", reason="警告的原因")
@app_commands.guilds(MY_GUILD)
async def warn(interaction: discord.Interaction, member: discord.Member, reason: str):
    # 斜杠命令的邏輯
    # 處理警告操作
    if member.id not in warns:
        warns[member.id] = 1 
    else:
        warns[member.id] += 1

    await interaction.response.send_message(f"{member.name}，原因：{reason} 已獲得 {warns[member.id]} 次警告!")

    if warns[member.id] == 3:
        await member.ban()
        await interaction.response.send_message(f"{member.name} 因達到3次警告而被ban!")
    # await interaction.response.send_message(f"{member.display_name} 被警告，原因：{reason}")

# 運行機器人
client.run(bot_token)
