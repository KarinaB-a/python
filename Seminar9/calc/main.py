from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5590584718:AAHcP-gY2G6m4ao6xLsEXsWZZYX9ta5kWmw").build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))


print ("server start")
app.run_polling()


