from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
)

TOKEN = "7765574964:AAEBz6GK-qg9vPj3serC05Dss-VvR86tetY"
anonymous_messages = []

# Start komandasini dasturlash
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salem! Bul jerde siz anonim xabarlar jiberiwin'iz mumkin. Sonin ushin pikirlerin'izdi erkin bolisin', bul jerde heshkim sizdi tanimaydi. Men sizdi esitiwge tayyarman.\nДавай поговорим!))")

# Anonim xabarlarni qabul qilish
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    message = update.message.text
    
    # Anonim xabarni lug‘atga saqlash
    anonymous_messages.append({"from": chat_id, "text": message})
    # Anonim xabarni maqsadli IDga yuboring
    target_id = "7772310913"  # Maqsadli foydalanuvchi ID si
    await context.bot.send_message(chat_id=target_id, text=f"У тебя новое анонимное сообщение!\n\n{message}\n\n↩️ Свайпни для ответа.")
    
    await update.message.reply_text("Xabariniz anonim tarizde jiberildi!")

# Javobni foydalanuvchiga yuborish
async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Foydalanuvchi yuborgan javobni olish
    reply_message = update.message.text
    sender_id = update.message.chat_id

    # Javobni anonim xabarga yuborish (bu yerda javob maqsadli IDga yuboriladi)
    for anonymous_message in anonymous_messages:
        if anonymous_message["from"] != sender_id:
            # Javob yuboriladi
            await context.bot.send_message(chat_id=anonymous_message["from"], text=f"Javob: {reply_message}")
            # Javob yuborilgan xabarni ro'yxatdan o'chirish
            anonymous_messages.remove(anonymous_message)
            break

    await update.message.reply_text("Javob yuborildi!")

# Botni ishga tushirish
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))  # Javob yuborish qo'shildi

    application.run_polling()

if __name__ == "__main__":
    main()