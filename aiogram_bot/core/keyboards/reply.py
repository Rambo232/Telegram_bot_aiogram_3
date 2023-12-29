from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ряд 1. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 1. Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 1. Кнопка 3'
        )
    ],
    [
        KeyboardButton(
            text='Ряд 2. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 2. Кнопка 2'
        )
    ],
    [
        KeyboardButton(
            text='Ряд 3. Кнопка 1'

        )
    ]

], resize_keyboard=True, input_field_placeholder='Выберите кнопку ↓')

tele_poll_location_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Создать викторину',
            request_poll=KeyboardButtonPollType()
        )
    ],
    [
        KeyboardButton(
            text='Отправить геолокацию\n(только с телефона)',
            request_location=True

        )
    ],
    [
        KeyboardButton(
            text='Отправить свой контакт',
            request_contact=True
        )
    ],
],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='Создать викторину||опрос, отправить локацию, или свой контакт. ↓'
)


# BUILDER


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text="Key 1")
    keyboard_builder.button(text="Key 2")
    keyboard_builder.button(text="Key 3")
    keyboard_builder.button(text="Send your geolocation", request_location=True)
    keyboard_builder.button(text="Send your contact", request_contact=True)
    keyboard_builder.button(text="Create quiz or poll", request_poll=KeyboardButtonPollType())
    keyboard_builder.adjust(3, 2, 1)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='Create quiz or poll, your location, send your contact. ↓'
    )
