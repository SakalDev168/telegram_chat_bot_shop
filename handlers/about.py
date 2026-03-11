from telegram import Update
from telegram.ext import ContextTypes


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "This is a Telegram Shopping Bot.\nBrowse products and order easily."
    )