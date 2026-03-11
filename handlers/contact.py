from telegram import Update
from telegram.ext import ContextTypes
from config import CONTACT_USERNAME, CONTACT_PHONE


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        f"Contact us\nTelegram: {CONTACT_USERNAME}\nPhone: {CONTACT_PHONE}"
    )