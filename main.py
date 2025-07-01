import os
import asyncio

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

IS_RAILWAY = os.getenv("RAILWAY_ENVIRONMENT") is not None

if not IS_RAILWAY:
    import nest_asyncio
    nest_asyncio.apply()

TOKEN = "7779612821:AAHkNicErmDf9Jux8jON49QQi-ZUCGxx528"
GROUP_ID = -1002707585664

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

async def clear_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    async for message in context.bot.get_chat_history(chat_id, limit=100):
        try:
            await context.bot.delete_message(chat_id, message.message_id)
        except:
            pass  # Ignora errores si no puede borrar algún mensaje

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(CommandHandler("clear", clear_history))


    print("🤖 Bot corriendo en Railway...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())