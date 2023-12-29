import json
import random
import typing
import aiogram.types
from aiogram import Bot
from aiogram.types import Message, KeyboardButton
from aiogram import F
from core.settings import settings
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from typing import Dict
from core.keyboards.reply import reply_keyboard, tele_poll_location_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard

image_count = 0
violations_count = 0


async def get_start(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id, f'<b>Привет {message.from_user.first_name}, рад тебя видеть!(Жирно)</b>')
    # await message.answer(
    # f'<s>Привет {message.from_user.first_name}. Это сообщение.</s>(Зачеркнуто)')
    await message.reply(
        f'<tg-spoiler>Привет {message.from_user.first_name}. Это ответ.</tg-spoiler>(Спойлер)')

    await message.answer(
        f'<i>Привет {message.from_user.first_name}. Это сообщение.(Курсивом)</i>',
        reply_markup=get_reply_keyboard())


async def get(message: Message):
    data_message = message.dict()
    print(json.dumps(data_message, default=str))
    result_data_message = await get_data_message(data_message=data_message)
    for key, value in result_data_message.items():
        print(f'{key} - {value}')
        if isinstance(value, str):
            print(f'Используя magic_filter к данным {key} можно обратиться через F.{key} == {value}')
        elif isinstance(value, int):
            print(f'Используя magic_filter к данным {key} можно обратиться через F.{key} == {value}')


async def get_user_info(message: Message, bot: Bot):
    global violations_count

    answers = [f'Слышь <b>{message.from_user.first_name}</b>, ебало завалил!',
               f'Пожалуйста <b>{message.from_user.first_name}</b>, фильтруйте ваши сообщения, это не уважительно.!',
               f'Уважаемый <b>{message.from_user.first_name}</b>, ебало завалил.',
               f'<b>{message.from_user.first_name}</b>, мне стыдно за вашу манеру общения!',
               f'<b>{message.from_user.first_name}</b>, вы могли бы быть по вежливее..',
               f'<b>{message.from_user.first_name}</b>, подобные слова не допустимы в нашем чате!',
               f'Ебаный в рот! <b>{message.from_user.first_name}</b>, хуля ты за базаром не следишь?!',
               f'<b>{message.from_user.first_name}</b>, думаю другие не оценят ваше высказывание.'
               ]

    ban_answers = [f'<b>{message.from_user.first_name}</b>, тебе бан.',
                   f'<b>{message.from_user.first_name}</b>, ты доигрался, теперь ты в чс.',
                   f'Ну все <b>{message.from_user.first_name}</b>, теперь тебе придется подостыть, тебе БАН!',
                   f'За не уважение к другим пользователь с именем --> <b>{message.from_user.first_name}</b>, был забанен до завтра.',
                   f'За непотребство в чате пользователь с именем --> <b>{message.from_user.first_name}</b>, был наказан бананом, тоесть баном.',
                   f'За конченный базар пользователь с именем --> <b>{message.from_user.first_name}</b>, был выебан и забанен!',
                   f'За пиздешь в чате пользователю с именем --> <b>{message.from_user.first_name}</b>, был надет кляп, пока не перестанет пиздеть!',
                   f'Все помнят как вы умели красиво говорить <b>{message.from_user.first_name}</b>, но то время ушло и вы были забанены за оскорбительные высказывания!'
                   ]

    if violations_count < 8:
        await message.answer(answers[random.randint(0, len(answers)-1)])
        violations_count += 1
        answer_json = json.dumps(message.dict(), default=str)
        print(answer_json)
        # count = len(answer_json)
        for key, value in message.dict().items():
            print(key, value)
    else:
        await message.answer(ban_answers[random.randint(0, len(ban_answers)-1)])
        # AFTER THIS MESSAGE NEED TO MUTE USER, LATER...



        #==============================================
        answer_json = json.dumps(message.dict(), default=str)
        print(answer_json)
        for key, value in message.dict().items():
            print(key, value)


async def get_user_location(message: Message, bot: Bot):
    await message.answer(f'Ты оптравил свою локацию!\r\a'
                         f'\nШирота---> {message.location.latitude}\r\a\nДолгота---> {message.location.longitude}')


async def get_data_message(data_message: Dict, prefix: str = '', sep: str = '.'):
    correct_values = {}
    for key, value in data_message.items():
        if isinstance(value, Dict):
            correct_values.update(await get_data_message(data_message=value, prefix=f'{prefix}{key}{sep}'))
        else:
            correct_values[f'{prefix}{key}'] = value
    return correct_values


async def get_photo(message: Message, bot: Bot):
    global image_count
    await message.answer(f'Я получил твою картинку, пожалуй сохраню ее себе😄')
    file = await bot.get_file(message.photo[-1].file_id)
    # print(message.photo[-1].file_id)
    await bot.download_file(file.file_path, f'core/images/photo_{image_count}.jpg')
    image_count += 1
    print(image_count)


async def get_admin_message(message: Message):
    print(F.from_user_id == settings.bots.admin_id)
    await message.answer(f'Здравствуйте админ {message.from_user.first_name}!\n!')


# async def get_inline_keyboard():
#     keyboard_builder = InlineKeyboardBuilder()
#     keyboard_builder.button(text="Да", callback_data='button_1')
#     keyboard_builder.button(text="Нет", callback_data='button_2')
#     keyboard_builder.adjust(1)
#     return keyboard_builder.as_markup()


async def get_inline(message: Message, bot: Bot):
    await message.answer(f'<s> Привет {message.from_user.first_name}. показываю инлайн клавиатуру!</s>',
                         reply_markup=get_inline_keyboard())


async def get_keyboard(message: Message):
    await message.answer("Вот тебе кнопки, жми...", reply_markup=get_inline_keyboard())


async def call_data(call: CallbackQuery):
    print(call.data)
    await call.answer()
    result = await get_data_message(data_message=call.dict())
    for key, value in result.items():
        print(f'{key} - {value}')
