import discord

from discord.ext import commands 

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='',intents=intents)

class ButtonView(discord.ui.View):
    @discord.ui.select(placeholder = "選擇", min_values=1, max_values=1, options=[
            discord.SelectOption(label="A", description="讓他告訴你未來一年間發生的事"),
            discord.SelectOption(label="B", description="讓他告訴你明天發生的事"),
            discord.SelectOption(label="C", description="讓他什麼都不要說")
        ])
    async def select_callback(self, interaction:discord.Interaction,select:discord.ui.Select ):
            self.disabled = True
            msg = None
            if select.values[0] is "A": msg = "你的外表看起來隨和、好相處，但內裡其實有點固執，意志非常的堅強，面對自己在乎的事情會非常執著。"
            elif select.values[0] is "B": msg = "你的個性有點急躁，想到什麼就做什麼，但也非常的單純，從來不記仇，社交能力很強，是大家的開心果。"
            else : msg = "你總是非常的小心謹慎，個性有點內向，不太懂得如何表達自己的情感面，很多時候你更喜歡自己待著，會讓你感到相較自在。"
            await interaction.response.edit_message(content=msg ,view=None)

@bot.command(name="選單")
async def click_click(ctx):
    await ctx.send('選單題目', view=ButtonView())

bot.run("MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w")


# select dice
# import discord
# from discord.ext import commands
# from discord import app_commands



# MY_GUILD = discord.Object(id=991905864162226177)  # replace with your guild id

# class MyClient(discord.Client):
#     def __init__(self, *, intents: discord.Intents):
#         super().__init__(intents=intents)
#         self.tree = app_commands.CommandTree(self)

#     async def setup_hook(self):
#         self.tree.copy_global_to(guild=MY_GUILD)
#         await self.tree.sync(guild=MY_GUILD)


# class ButtonView(discord.ui.View):
#     @discord.ui.select(placeholder = "選擇", min_values=1, max_values=1, options=[
#             discord.SelectOption(label="大小", description="大小的規則及賠率"),
#             discord.SelectOption(label="單雙", description="單雙的規則及賠率"),
#             discord.SelectOption(label="圍骰", description="圍骰的規則及賠率"),
#             discord.SelectOption(label="全圍", description="全圍的規則及賠率"),
#             discord.SelectOption(label="下注在單一個點數", description="下注在單一個點數的規則及賠率"),
#             discord.SelectOption(label="點數總和", description="點數總和的規則及賠率")
#         ])
#     async def select_callback(self, interaction:discord.Interaction,select:discord.ui.Select ):
#             embed = discord.Embed(
#                 # title='骰寶歸則',
#                 # description='This is a rule',   
#                 colour=discord.Colour.purple()
#             )
#             self.disabled = True
#             # await interaction.response.send_message(view=ButtonView())
#             if select.values[0] == "大小":embed.add_field(name=":regional_indicator_b: 大", 
#                     value="規則：總點數 11 至 17 ( 遇圍骰莊家通吃 )\n賠率：1 賠 1", 
#                     inline=True) and embed.add_field(name=":regional_indicator_s:小" ,value="規則：總點數為 4 至 10 ( 遇圍骰莊家通吃 )\n賠率：1 賠 1\n",inline=True)
#             elif select.values[0] == "單雙":embed.add_field(name="單", 
#                     value="規則：總點數為 5, 7, 9, 11, 13, 15, 17 點 ( 遇圍骰莊家通吃 )\n賠率：1 賠 1\n", 
#                     inline=True) and embed.add_field(name="雙",value="規則：總點數為 4, 6, 8, 10, 12, 14, 16 點 ( 遇圍骰莊家通吃 )賠率：1 賠 1\n",inline=True)
#             elif select.values[0] == "圍骰":embed.add_field(name="圍骰", 
#                     value="規則：3 顆骰子點數都一樣且是你指定的\n賠率：1 賠 180\n特別說明：「圍骰」跟「全圍」差別是在一個要指定點數一個不用。", 
#                     inline=False)  
#             elif select.values[0] == "全圍":embed.add_field(name="全圍（豹子）", 
#                     value="規則：3 顆骰子點數都一樣但你不需指定點數\n賠率：1 賠 30\n特別說明：「圍骰」跟「全圍」差別是在一個要指定點數一個不用。", 
#                     inline=True)  
#             elif select.values[0] == "下注在單一個點數":embed.add_field(name="對子 ( 雙骰、長牌 )", 
#                     value="規則：投注指定的雙骰 ( 如雙 1 點 ) ，至少開出 2 顆所投注的骰子\n賠率：1 賠 11\n", 
#                     inline=True),embed.add_field(name="牌九式 ( 骨牌、短牌 )", 
#                     value="規則：投注 15 種 2 顆骰子可能出現的組合 ( 如 1 、 2)\n賠率：1 賠 6\n", 
#                     inline=True),embed.add_field(name="單骰", 
#                     value="規則：投注每顆骰子 1 至 6 中指定的點數，點數出現 1 次\n賠率：1 賠 1\n", 
#                     inline=False),embed.add_field(name="雙骰", 
#                     value="規則：投注每顆骰子 1 至 6 中指定的點數，點數出現 2 次\n賠率：1 賠 2\n", 
#                     inline=False),embed.add_field(name="全骰", 
#                     value="規則：投注每顆骰子 1 至 6 中指定的點數，點數出現 3 次\n賠率：1 賠 3\n", 
#                     inline=False) 
#             elif select.values[0] == "點數總和":embed.add_field(name="點數總和", 
#                     value="規則：4 或 17 點\n賠率：1 賠 60\n\n規則：5 或 16 點\n賠率：1 賠 20\n\n規則：6 或 15 點\n賠率：1 賠 18\n\n規則：7 或 14 點\n賠率：1 賠 12\n\n規則：8 或 13 點\n賠率：1 賠 8\n\n規則：9, 10, 11, 或 12點\n賠率：1 賠 6\n", 
#                     inline=False)
#             await interaction.response.send_message(embed=embed,view=ButtonView())



# intents = discord.Intents.default()
# client = MyClient(intents=intents)




# @client.tree.command()
# async def select(interaction):
#     embed = discord.Embed(
#         title='Rule',
#         description='This is a rule',
#         colour=discord.Colour.purple()
#     )
    
#     await interaction.response.send_message(embed=embed, view=ButtonView())


# client.run("MTEyMjkwMTQzNjk5NzU3ODc5Mg.GTvVtj.BlmQ_sGQWvl_-MP9St0-TvA24wcURK0kqV376o")



# select exam
# import discord
# from discord.ext import commands
# from discord.ui import Select, View


# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='',intents=intents)

# class DropdownView(View):
#   @discord.ui.select(
#     placeholder="选择你喜欢的颜色",
#     options=[
#       discord.SelectOption(label="红色", value="红色"),
#       discord.SelectOption(label="绿色", value="绿色") 
#     ]
#   )
#   async def select_callback(self, interaction, select):
#     await interaction.response.send_message(f"你选择的颜色是:{select.values[0]}")

# @bot.command()
# async def embedtest(ctx):

#   embed = discord.Embed(title="选择你喜欢的颜色")

#   view = DropdownView()

#   await ctx.send(embed=embed, view=view)

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')
