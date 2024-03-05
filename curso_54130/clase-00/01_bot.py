#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

import requests
from telegram import ForceReply, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def consultar_capital(pais="argentina"):
    direccion = f"https://restcountries.com/v3.1/name/{pais}"

    try:
        respuesta = requests.get(direccion)
        informacion = respuesta.json()
        # print(type(informacion))
        # print(len(informacion))
        data = informacion[0]
        # print(type(data))
        # for clave in data:
        #     print(clave)
        capital = data["capital"]
        subregion = data["subregion"]

        # breakpoint()
        lat, long = data["latlng"]
        url = generar_link_a_google_maps(lat, long)
        return f"{capital}, {subregion}, {url}"
    except:
        return f"No se encontro informacion para: {pais}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    print("_" * 90)
    print(update.message.text)
    print("_" * 90)
    await update.message.reply_text(consultar_capital(update.message.text))


def generar_link_a_google_maps(lat, long):
    base_url = "https://www.google.com/maps/search/?api=1&query="
    link = base_url + f"{lat},{long}"
    return link


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    with open("token.txt", "r") as f:
        application = Application.builder().token(f.read()).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
