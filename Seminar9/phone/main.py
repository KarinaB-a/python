from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5618668137:AAEd1QRMuOti7jtL8BTl-1Gnc99olqoByzo").build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("export", export_command))
app.add_handler(CommandHandler("import", import_command))

print ("server start")
app.run_polling()


