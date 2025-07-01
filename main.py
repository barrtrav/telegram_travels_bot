import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

import os

TOKEN = "7779612821:AAHkNicErmDf9Jux8jON49QQi-ZUCGxx528"
GROUP_ID = int(os.getenv("-1002707585664"))

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"👋 ¡Bienvenido(a), {member.first_name}!\n"
            "📍 Al grupo oficial de *King Travels*\n\n"
            "🚗 Servicio de taxi:\n"
            "• Confiable\n"
            "• Cómodo\n"
            "• Puntual\n\n"
            "💬 Este es tu espacio.\n"
            "👑 ¡Viaja como rey!",
            parse_mode="Markdown"
        )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    print("🤖 Bot corriendo en Railway...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())