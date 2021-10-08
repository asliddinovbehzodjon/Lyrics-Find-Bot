import logging

from aiogram import Dispatcher

from data.config import ADMINS
from loader import bot

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=admin,text='Bot faollashdi!!!')

        except Exception as err:
            logging.exception(err)
