# 加減法
# from discord.ext import commands 
# import discord

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# async def test(ctx, arg1, arg2):
#     await ctx.send(f'You passed {arg1} and {arg2}')

# @bot.command()
# async def plus(ctx, a: int, b: int):
#     await ctx.send(a + b)

# @bot.command()
# async def minus(ctx, a: int, b: int):
#     await ctx.send(a - b)

# @bot.command()
# async def multiply(ctx, a: int, b: int):
#     await ctx.send(a * b)

# @bot.command()
# async def divide(ctx, a: int, b: int):
#     if b == 0:
#         await ctx.send("Cannot divide by zero.")
#     else:
#         await ctx.send(a / b)

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')


# from discord.ext import commands 
# import discord

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# async def calculate(ctx, *args):
#     if len(args) < 3:
#         await ctx.send("Please provide at least two numbers and an operator.")
#         return
    
#     try:
#         num1 = float(args[0])
#         operator = args[1]
#         num2 = float(args[2])
#     except ValueError:
#         await ctx.send("Invalid input. Please provide valid numbers.")
#         return
    
#     result = None

#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             await ctx.send("Cannot divide by zero.")
#             return
#         result = num1 / num2
#     else:
#         await ctx.send("Invalid operator. Please use +, -, *, or /.")
#         return

#     await ctx.send(f'Result: {result}')

# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')




from discord.ext import commands
import discord

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def calculate(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.send(f'Result: {result}')
    except Exception as e:
        await ctx.send(f'Error: {str(e)}')

bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')
