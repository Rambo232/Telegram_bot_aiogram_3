import random
from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


tip = 0


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Покупка Киберонов онлайн',
        description='Вы можете обменять деньги на Кибероны',
        payload='Оплата через бота',
        provider_token='381764678:TEST:74455',
        currency='rub',
        prices=[
            LabeledPrice(
                label="50K",
                amount=50000
            ),
            LabeledPrice(
                label='НДС',
                amount=10000
            ),
            LabeledPrice(
                label="Скидка",
                amount=-5000
            ),
            LabeledPrice(
                label="Ваш бонус",
                amount=-10000
            )
        ],
        max_tip_amount=10000,
        suggested_tip_amounts=[1000, 1500, 3000, 5000],
        start_parameter='pay',
        provider_data=None,
        # photo_url='https://drive.google.com/file/d/1rI16mgWYyq13B4CMy9IdByQNkeGoAxx_/view?usp=sharing',
        # photo_url='/Users/kirill/PycharmProjects/Telegram_bot_aiogram_3/core/images/10K.png',
        photo_url='https://cdn.swisscows.com/image?url=https%3A%2F%2Ffranshiza.ru%2Ffiles%2Fup%2Ffranchise%2F5fabec2a98d58.png',
        photo_width=450,
        photo_height=450,
        need_name=True,
        need_email=True,
        need_shipping_address=False,
        send_email_to_provider=False,
        send_phone_number_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=True,
        reply_to_message_id=message.from_user.id,
        allow_sending_without_reply=True,
        reply_markup=None,  # доп клавиатура с первой кнопкой 'Оплатить'!!
        request_timeout=15
    )


async def pre_checkout_query2(pre_checkout: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)  # or need to implement logic of availability


async def successful_payment(message: Message):
    # global tip
    pay_description_1 = message.successful_payment.invoice_payload
    pay_description_2 = message.successful_payment.order_info
    print(pay_description_1)
    print(pay_description_2)



    discount = random.randint(10, 50)
    amount = message.successful_payment.total_amount // 1000

    msg = (f'Спасибо за оплату в {message.successful_payment.total_amount // 100}{message.successful_payment.currency}.'
           f'\r\nЧаевые доставщику -> {tip}{message.successful_payment.currency}.'
           f'\r\n============================\n'
           f'\r\n🥳Вы купили {50} kiberone!🥳\n'
           f'\r\n============================'
           f'\r\n<b> ↓ Менеджер  Киберван ↓</b>'
           f'\r\n⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺'
           f'\n🤑Я получил ваш заказ🤑'
           f'\r\n---------------------------------------'
           f'\r\n🤩Вам одобрена скидка!🤩'
           f'\r\n---------------------------------------'
           f'\r\nРазмер вашей скидки : {discount}{message.successful_payment.currency}!😎')

    await message.answer(msg)
