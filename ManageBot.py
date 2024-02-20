# https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py
import discord
from discord.ext import commands
from discord import app_commands
import mysql.connector
import yaml
import datetime 
import re


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
# @client.tree.command(name="warn", description="對成員發出警告")
# @app_commands.describe(member="要警告的成員", reason="警告的原因")
# @app_commands.guilds(MY_GUILD)
# async def warn(interaction: discord.Interaction, member: discord.Member, reason: str):
#     # 斜杠命令的邏輯
#     # 處理警告操作
#     if member.id not in warns:
#         warns[member.id] = 1 
#     else:
#         warns[member.id] += 1

#     await interaction.response.send_message(f"{member.mention}，原因：{reason} 已獲得 {warns[member.id]} 次警告!")

#     if warns[member.id] == 3:
#         await member.ban()
#         await interaction.response.send_message(f"{member.mention} 因達到3次警告而被ban!")
    # await interaction.response.send_message(f"{member.display_name} 被警告，原因：{reason}")

@client.tree.command(name="ban", description="將成員踢出伺服器並加入黑名單")
@app_commands.describe(member="要警告的成員", reason="踢出的原因")
@app_commands.guilds(MY_GUILD)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str):
    await member.ban()
    await interaction.response.send_message(f'{member.name} has been banned.')

@client.tree.command(name="timeoutmem", description="對成員禁言")
@app_commands.describe(member="要禁言的成員", minutes="禁言秒數", reason="禁言原因")
@app_commands.guilds(MY_GUILD)
@commands.has_permissions(manage_roles=True)  # 只有管理員才能使用這個指令
async def timeout(interaction: discord.Interaction, member: discord.Member, minutes: int, reason: str):
    await member.edit(timed_out_until=discord.utils.utcnow() + datetime.timedelta(minutes=minutes))
    await interaction.response.send_message(f'{member.mention}已被設定禁言，將在{minutes}分鐘後解除禁言，原因{reason}。')

@client.tree.command(name="retimeoutmem", description="對成員解除禁言")
@app_commands.describe(member="要解除禁言的成員", reason="解除禁言原因")
@app_commands.guilds(MY_GUILD)
@commands.has_permissions(manage_roles=True)
async def remove_timeout(interaction: discord.Interaction, member: discord.Member, reason: str):
    await member.edit(timed_out_until=discord.utils.utcnow())  # 使用已知的 UTC 時間
    await interaction.response.send_message(f'{member.mention}的禁言已被解除，原因{reason}。')

@client.tree.command(name="check_member", description="查看成員")
@app_commands.describe(member="標記成員")
@app_commands.guilds(MY_GUILD)
async def get_roles(interaction: discord.Interaction, member: discord.Member):
    # 獲取身份組，排除第一個（@everyone）
    roles = [role.name for role in member.roles[1:]]  

    # 傳送身份組，將所有角色名稱連接成一個字符串
    roles_description = ", ".join(roles)
    await interaction.response.send_message(f"User name: {member.name}\n"
        f"User ID: {member.id}\n"
        f"Joined at: {member.joined_at}\n" 
        f"{member.display_name} 的身份組: {roles_description}")

# 查看ping值
@client.tree.command(name="ping", description="查看ping")
@app_commands.describe()
@app_commands.guilds(MY_GUILD)
async def ping(interaction: discord.Interaction): # a slash command will be created with the name "ping"
    await interaction.response.send_message(f"Pong! Latency is {client.latency}")
# 運行機器人
client.run(bot_token)
