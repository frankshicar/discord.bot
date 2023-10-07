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