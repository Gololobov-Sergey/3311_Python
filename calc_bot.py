from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes):
    await update.message.reply_text(f"Привіт {update.effective_user.username}! Це бот, який вміє виконувати нескладні арифметичні операції. Введіть щось типу 4+5, і я надам відповідь")

async def calculate(update: Update, context: ContextTypes):
    text = update.message.text
    result = 0
    if '+' in text:
        arr = text.split('+')
        result = int(arr[0]) + int(arr[1])
    elif '-' in text:
        arr = text.split('-')
        result = int(arr[0]) - int(arr[1])
    elif '*' in text:
        arr = text.split('*')
        result = int(arr[0]) * int(arr[1])
    elif '/' in text:
        arr = text.split('/')
        if int(arr[1]) == 0:
            result = "На 0 ділити не можна!!!"
        else:
            result = int(arr[0]) / int(arr[1])
    elif '^' in text:
        arr = text.split('^')
        result = int(arr[0]) ** int(arr[1])

    await update.message.reply_text(f"{text}={result}")

app = ApplicationBuilder().token('token!!!!').build()
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

app.run_polling()