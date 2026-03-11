from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["🛍 Browse Products"],
        ["🛒 View Cart"],
        ["📞 Contact", "ℹ️ About"],
    ]

    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Welcome to the shop 🛒",
        reply_markup=markup
    )