from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8585597579:AAEm6mgsvd9I88kTw95JhsBDz1DL0tKdhoo"

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("عکس گرفتم 👍")

    photo = update.message.photo[-1]
    file = await photo.get_file()

    await file.download_to_drive("input.jpg")

    await update.message.reply_photo(photo=open("input.jpg", "rb"))


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

print("Bot is running...")
app.run_polling()