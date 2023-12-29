import aiogram.enums
from aiogram import Bot, Dispatcher
from core.units.commands import set_command
import asyncio
import logging
from aiogram.types import Message
from core.settings import settings
from aiogram import F
from core.handlers.pay import order, pre_checkout_query2, successful_payment
from aiogram.filters import Command, CommandStart
from core.filters.contact_checker import isTrueContact
from core.handlers.contact import get_fake_contact, get_true_contact
from core.handlers.callback import select_macbook
from core.units.callbackdata import MackInfo
from core.handlers.basic import (get_start, get_photo, get_admin_message,
                                 get_keyboard, get_inline_keyboard, call_data,
                                 get_user_info, get_user_location, get_inline)


async def bot_start(bot: Bot):
    # if  == settings.bots.admin_id:
    await set_command(bot)
    # await set_admin_command(bot)
    # else:
    #     await set_command(bot)
    await bot.send_message(settings.bots.admin_id, text="\nBot is running..\n")


async def bot_end(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="\nBot was terminated.\n")


async def start():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s-[%(levelname)s]-%(name)s -'
                        '(%(filename)s).%(funcName)s(%(lineno)d)%(message)s')

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(bot_start)
    dp.shutdown.register(bot_end)
    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query2)
    dp.message.register(successful_payment, F.successful_payment)
    dp.message.register(get_inline, Command(commands='inline'))
    # dp.callback_query.register(select_macbook, F.data.startswith('apple_'))
    dp.callback_query.register(select_macbook, MackInfo.filter())
    dp.message.register(get_user_location, F.location)
    dp.callback_query.register(call_data)
    dp.message.register(get_keyboard, F.text == 'К')
    dp.message.register(get_user_info, F.text.lower().regexp(
        r'(.+?)?(хуй|нах|хер|ебал|пидор|ебан|ёбан|гандон|шлюх|пизд|ебал'
        r'|жоп|срак|пердак|очко|бля|конченный|конченый|дебил|хуев|лох).?'))


    # dp.message.register(get)
    # dp.message.register(get_admin_message, F.from_user_id == settings.bots.admin_id and F.photo | F.text)  # MANY -> F.from_user_id.in_({settings.bots.admin_id,4534534534})
    dp.message.register(get_true_contact, F.contact, isTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    # dp.message.register(get_start, CommandStart()

    try:
        await dp.start_polling(bot)
    finally:
        print("\nERROR DETECTED!!!\n")
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())



