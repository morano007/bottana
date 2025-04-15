from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("TOKEN_BOT")  # Legge il token da variabile d'ambiente

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono online! Usa /help per i comandi.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hai scritto: {update.message.text}")

# Configurazione webhook per Render
async def setup_webhook(app):
    url = "https://tuo-bot.onrender.com/"  # Sostituisci con il tuo URL
    await app.bot.set_webhook(url)

def main():
    app = ApplicationBuilder().token(TOKEN).post_init(setup_webhook).build()
    
    # Aggiungi gestori di comandi/messaggi
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Avvia il bot in modalità webhook
    app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url="https://tuo-bot.onrender.com/",
        secret_token=None
    )

if __name__ == "__main__":
    main()