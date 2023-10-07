
import discord
from discord.ext import commands
from discord.ui import Select, View


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='',intents=intents)

class DropdownView(View):
  @discord.ui.select(
    placeholder="选择你喜欢的颜色",
    options=[
      discord.SelectOption(label="红色", value="红色"),
      discord.SelectOption(label="绿色", value="绿色") 
    ]
  )
  async def select_callback(self, interaction, select):
    await interaction.response.send_message(f"你选择的颜色是:{select.values[0]}")

@bot.command()
async def embedtest(ctx):

  embed = discord.Embed(title="选择你喜欢的颜色")

  view = DropdownView()

  await ctx.send(embed=embed, view=view)

bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')


