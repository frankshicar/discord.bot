import discord
from discord import app_commands



MY_GUILD = discord.Object(id=991905864162226177)  # replace with your guild id

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.all()
client = MyClient(intents=intents)


@client.tree.command()
async def rule(interaction):
    embed = discord.Embed(
        title='Rule',
        description='骰寶規則',
        colour=discord.Colour.purple()
    )
    embed.add_field(name=":regional_indicator_b: 大", 
                    value="規則：總點數 11 至 17 ( 遇圍骰莊家通吃 )\n賠率：1 賠 1", 
                    inline=True) and embed.add_field(name=":regional_indicator_s:小" ,value="規則：總點數為 4 至 10 ( 遇圍骰莊家通吃 )\n賠率：1 賠 1\n",inline=True)

    await interaction.response.send_message(embed=embed)



client.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GTvVtj.BlmQ_sGQWvl_-MP9St0-TvA24wcURK0kqV376o')

    