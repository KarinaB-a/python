from warnings import catch_warnings
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
import random

HELP = """
/help - показать полное меню
/play - начать игру
/move - сделать ход
/stop - завершить игру
"""
# признак/флаг начала игры
game_start = False
candies = 0
comp_candies = 0
player_candies = 0

async def help_command(update: Update, context: ContextTypes):
    await log(update, context)  
    await update.message.reply_text(HELP)

async def move_command(update: Update, context: ContextTypes):
    await log(update, context) 

    if game_start:
        msg = update.message.text #"/move 10"
        print(msg)
        items = msg.split() #["/move","10"]
        await player_move(update, int(items[1])) #количество конфет игрока
        await comp_move(update) #количество конфет игрока
    else:
        await update.message.reply_text('Введите команду /play')

async def player_move(update: Update, take_candies):
    global game_start
    global candies
    global comp_candies
    global player_candies
    if take_candies <= 0 or take_candies > min(28, candies):
        await update.message.reply_text('За ход можно забрать не более 28 конфет и не более оставшихся конфет! ')
    else:
        player_candies = player_candies + take_candies
        candies = candies - take_candies
        await update.message.reply_text(f'У игрока {player_candies} конфет ')
        await update.message.reply_text(f'На столе осталось {candies} конфет ')

        if candies == 0:
            game_start = False
            player_candies = player_candies + comp_candies
            await update.message.reply_text(f'Игрок забирает все конфеты. Игрок выйграл с количеством конфет {player_candies}')
            

async def comp_move(update: Update):
    global game_start
    global candies
    global comp_candies
    global player_candies
    take_comp_candies = random.randint(1,min(28, candies))
    comp_candies = comp_candies + take_comp_candies
    candies = candies - take_comp_candies
    await update.message.reply_text(f'Компьютер забирает {take_comp_candies} конфет\nУ компьютера {comp_candies} конфет\nКонфет на столе осталось {candies}')

    if candies == 0:
        game_start = False
        comp_candies = comp_candies + player_candies
        await update.message.reply_text(f'Компьютер выйграл, с количеством конфет {comp_candies}')

async def stop_command(update: Update, context: ContextTypes):
    global game_start
    await log(update, context)  
    game_start = False
    await update.message.reply_text(f'игра завершена ')
    print(f"{game_start}")

async def play_command(update: Update, context: ContextTypes):
    global game_start
    global candies
    global comp_candies
    global player_candies
    await log(update, context)
    msg = update.message.text #"/play 10"
    items = msg.split() #["/play","10"]
    game_start = True
    if len(items) > 1:
        candies = int(items[1])
    else:
        candies = 50
    comp_candies = 0
    player_candies = 0
    skip_first = random.randint(0,1) == 1

    await update.message.reply_text(f'Игра началась\nколичество конфет = {candies}\nРежим игрок против компьютера')
    if skip_first:       
        await comp_move(update)
    else:
        await update.message.reply_text(f'Ваш ход, используйте команду "/move <количество конфет>"')

