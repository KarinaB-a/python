from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
from model import write_format_csv, format_lines, read_format_csv, format_csv, from_csv, from_lines

# async def hi_command(update: Update, context: ContextTypes):
#     await log(update, context)  
    # await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

PHONES_DB = 'csv.txt'

async def help_command(update: Update, context: ContextTypes):
    await log(update, context)  
    await update.message.reply_text(f'/help\n/import\n/export')

async def export_command(update: Update, context: ContextTypes):
    await log(update, context)  
    msg = update.message.text
    print(msg) # "/export csv" "/export lines" "/export json" 
    items = msg.split()
    format = items[1]

    data = read_format_csv(PHONES_DB)

    if format == 'csv':
        await update.message.reply_text(format_csv(data))
    elif format == 'lines':
        await update.message.reply_text(format_lines(data))
    else:
        await update.message.reply_text('Формат не поддерживается')
        

async def import_command(update: Update, context: ContextTypes):
    await log(update, context)  
    msg = update.message.text
    print(msg)
    lines = msg.split('\n') # "/import lines\n"
    items = lines[0].split()
    format = items[1]

    if format == 'csv':
        write_format_csv(from_csv(lines[1:]), PHONES_DB)
        await update.message.reply_text("Формат сsv импортирован")
    elif format == 'lines':
        write_format_csv(from_lines(lines[1:]), PHONES_DB)
        await update.message.reply_text("Формат lines импортирован")
    else:
        await update.message.reply_text('Формат не поддерживается')

    