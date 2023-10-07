import discord
from discord.ext import commands
from discord import app_commands



MY_GUILD = discord.Object(id=991905864162226177)  # replace with your guild id

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


class ButtonView(discord.ui.View):
    @discord.ui.select(placeholder = "選擇", min_values=1, max_values=1, options=[
            discord.SelectOption(label="A", description="讓他告訴你未來一年間發生的事"),
            discord.SelectOption(label="B", description="讓他告訴你明天發生的事"),
            discord.SelectOption(label="C", description="讓他什麼都不要說")
        ])
    async def select_callback(self, interaction:discord.Interaction,select:discord.ui.Select ):
            embed = discord.Embed(
                title='Rule',
                description='This is a rule',
                colour=discord.Colour.purple()
            )
            self.disabled = True
            # await interaction.response.send_message(view=ButtonView())
            if select.values[0] is "A":embed.add_field(name=":regional_indicator_b: 大", 
                    value="規則：總點數 11 至 17 ( 遇圍骰莊家通吃 )\n賠率：1 賠 1", 
                    inline=True)  # 添加 "value" 参数
            elif select.values[0] is "B":embed.add_field(name=":regional_indicator_s:小", 
                    value="規則：總點數為 4 至 10 ( 遇圍骰莊家通吃 )\n賠率：1 賠 1\n", 
                    inline=True)  
            else : msg = "你總是非常的小心謹慎，個性有點內向，不太懂得如何表達自己的情感面，很多時候你更喜歡自己待著，會讓你感到相較自在。"
            await interaction.response.send_message(embed=embed,view=ButtonView())



intents = discord.Intents.default()
client = MyClient(intents=intents)




@client.tree.command()
async def select(interaction):
    embed = discord.Embed(
        title='Rule',
        description='This is a rule',
        colour=discord.Colour.purple()
    )
    
    await interaction.response.send_message(embed=embed, view=ButtonView())


client.run("MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w")


