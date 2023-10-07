import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# 遊戲板，初始化為空的3x3列表
game_board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'  # 當前玩家，初始化為X

# 檢查遊戲是否已結束的函數
def check_game_over():
    # 在這裡添加檢查遊戲是否結束的邏輯
    pass

@bot.command()
async def start_game(ctx):
    global game_board, current_player
    # 初始化遊戲板和當前玩家
    game_board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    await ctx.send('遊戲開始！')

@bot.command()
async def mark(ctx, row: int, col: int):
    global game_board, current_player

    if 0 <= row < 3 and 0 <= col < 3 and game_board[row][col] == ' ':
        game_board[row][col] = current_player

        # 切換玩家
        current_player = 'X' if current_player == 'O' else 'O'

        # 生成帶有分隔線的遊戲板消息
        game_board_message = ''
        for i in range(3):
            game_board_message += ' | '.join(game_board[i]) + '\n'
            if i < 2:
                game_board_message += '---------\n'

        await ctx.send(f'位置已標記為 {game_board[row][col]}。\n```\n{game_board_message}```')

        # 檢查遊戲是否結束
        if check_game_over():
            await ctx.send('遊戲結束，平局或某人獲勝。')
    else:
        await ctx.send('無效的位置。')

bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')



# import discord
# from discord.ext import commands

# intents = discord.Intents.all()
# #

# bot = commands.Bot(command_prefix='!', intents=intents)

# # 遊戲板，初始化為空的3x3列表
# game_board = [[' ' for _ in range(3)] for _ in range(3)]

# # 檢查遊戲是否已結束的函數
# def check_game_over():
#     # 在這裡添加檢查遊戲是否結束的邏輯
#     pass

# @bot.command()
# async def start_game(ctx):
#     global game_board
#     # 初始化遊戲板
#     game_board = [[' ' for _ in range(3)] for _ in range(3)]
#     await ctx.send('遊戲開始！')

# @bot.command()
# async def mark(ctx, row: int, col: int):
#     global game_board

#     if 0 <= row < 3 and 0 <= col < 3 and game_board[row][col] == ' ':
#         game_board[row][col] = 'X'  # 假設玩家為X，您可以設計成交替玩家

#         # 生成遊戲板的消息
#         game_board_message = ''
#         for i in range(3):
#             game_board_message += ' '.join(game_board[i]) + '\n'

#         await ctx.send(f'位置已標記為 X。\n```\n{game_board_message}```')

#         # 檢查遊戲是否結束
#         if check_game_over():
#             await ctx.send('遊戲結束，平局或某人獲勝。')
#     else:
#         await ctx.send('無效的位置。')


# bot.run('MTEyMjkwMTQzNjk5NzU3ODc5Mg.GSP5iN.o3gvaEY_bUlz3kJkiDuvCpREy_vJ4a7_9rVG8w')

