from telegram import Update
from telegram.ext import ContextTypes
from services.cart_service import get_cart


async def view_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id
    cart = get_cart(user_id)

    if not cart:
        await update.message.reply_text("🛒 Your cart is empty")
        return

    text = "🛒 Your Cart\n\n"
    total = 0

    for item in cart:
        text += f"{item['name']} - ${item['price']}\n"
        total += item["price"]

    text += f"\nTotal: ${total}"

    await update.message.reply_text(text)