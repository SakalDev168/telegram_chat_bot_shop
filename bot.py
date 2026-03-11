from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from config import BOT_TOKEN

from handlers.menu import start
from handlers.product import show_categories, show_products, add_cart_callback
from handlers.cart import view_cart
from handlers.contact import contact
from handlers.about import about


async def router(update, context):

    text = update.message.text

    if text == "🛍 Browse Products":
        await show_categories(update, context)

    elif text in ["Phones", "Laptops"]:
        await show_products(update, context)

    elif text == "🛒 View Cart":
        await view_cart(update, context)

    elif text == "📞 Contact":
        await contact(update, context)

    elif text == "ℹ️ About":
        await about(update, context)

    elif text == "⬅ Back":
        await start(update, context)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, router))
app.add_handler(CallbackQueryHandler(add_cart_callback, pattern="add_"))

app.run_polling()