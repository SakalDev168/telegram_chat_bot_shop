from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes

from services.product_service import get_categories, get_products, get_product_by_id
from services.cart_service import add_to_cart


async def show_categories(update: Update, context: ContextTypes.DEFAULT_TYPE):

    categories = get_categories()

    keyboard = [[c] for c in categories]
    keyboard.append(["⬅ Back"])

    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Choose category:",
        reply_markup=markup
    )


async def show_products(update: Update, context: ContextTypes.DEFAULT_TYPE):

    category = update.message.text
    items = get_products(category)

    for p in items:

        keyboard = [
            [InlineKeyboardButton("Add to Cart 🛒", callback_data=f"add_{p['id']}")]
        ]

        markup = InlineKeyboardMarkup(keyboard)

        with open(p["image"], "rb") as img:

            await update.message.reply_photo(
                img,
                caption=f"{p['name']}\nPrice: ${p['price']}",
                reply_markup=markup
            )


async def add_cart_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    product_id = int(query.data.split("_")[1])

    product = get_product_by_id(product_id)

    user_id = query.from_user.id

    add_to_cart(user_id, product)

    await query.message.reply_text("✅ Added to cart")