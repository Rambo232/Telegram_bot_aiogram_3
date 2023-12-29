from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.units.callbackdata import MackInfo


select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Macbook Air 13" M1 2020',
            callback_data='apple_air_13_m1_2020'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Air 13" M2 2022',
            callback_data='apple_air_13_m2_2022'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 14" M1 2021',
            callback_data='apple_pro_14_m1_2021'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 16 M1 2021',
            callback_data='apple_pro_16_m1_2021'
        )
    ],
    [
        InlineKeyboardButton(
            text='Link',
            url='https://vodovod.site',

        )
    ],
    [
        InlineKeyboardButton(
            text='Telegram profile',
            url='tg://user?id=5907028036'
        )
    ],
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text='Macbook Air 13" M1 2020',
        callback_data=MackInfo(model='Air', diagonal_size=13, chip='M1', year=2020)
    )

    keyboard_builder.button(
        text='Macbook Air 13" M2 2022',
        callback_data=MackInfo(model='Air', diagonal_size=13, chip='M2', year=2022)
    )

    keyboard_builder.button(
        text='Macbook Pro 14" M2 2021',
        callback_data=MackInfo(model='Pro', diagonal_size=14, chip='M1', year=2021)
    )

    keyboard_builder.button(
        text='Macbook Pro 16" M2 2021',
        callback_data=MackInfo(model='Pro', diagonal_size=16, chip='M1', year=2021)
    )

    keyboard_builder.button(text="Link", url='https://vodovod.site')
    keyboard_builder.button(text="User profile", url='tg://user?id=5907028036')

    keyboard_builder.adjust(1, 1, 1, 1, 2)

    return keyboard_builder.as_markup()
