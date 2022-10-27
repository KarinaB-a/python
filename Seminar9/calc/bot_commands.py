from warnings import catch_warnings
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *

async def help_command(update: Update, context: ContextTypes):
    await log(update, context)  
    await update.message.reply_text(f'/help\n/calc')

async def calc_command(update: Update, context: ContextTypes):
    await log(update, context)  
    msg = update.message.text
    print(msg) 
    items = msg.split()
    expr = items[1]
    try: 
        await update.message.reply_text(f'Результат = {eval(expr)}')
    except SyntaxError:
        await update.message.reply_text(f'Ошибка в выражении {expr}')

        

