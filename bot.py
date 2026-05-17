from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "PUT_YOUR_REAL_TOKEN_HERE"

# Web server for Render
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is running!"

def run_web():
    web_app.run(host="0.0.0.0", port=10000)

# Telegram command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Your bot works 24/7.")

# Main bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

# Start web server
Thread(target=run_web).start()

print("Bot started...")
app.run_polling()
