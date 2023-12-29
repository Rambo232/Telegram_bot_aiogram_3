from aiogram import Bot
from aiogram.types import CallbackQuery
from core.units.callbackdata import MackInfo


async def select_macbook(call: CallbackQuery, bot: Bot, callback_data: MackInfo):
    model = callback_data.model
    diagonal_size = callback_data.diagonal_size
    chip = callback_data.chip
    year = callback_data.year

    answer = (f'{call.message.from_user.first_name}\n'
              f'                                         \n'
              f'<b>↓ You choose ↓</b>\n'
              f'============================\n'
              f'Apple Macbook:     <b>({model})</b>               \n'
              f'--------------------------------------\n'
              f'Diagonal size :         <b>({diagonal_size})</b>               \n'
              f'--------------------------------------\n'
              f'Year :                    <b>({year})</b>              \n'
              f'--------------------------------------\n'
              f'Chip :                       <b>({chip})</b>             \n'
              f'============================\n')

    await call.message.answer(answer)

    # handler call
    await call.answer()
    print(f'{call.answer()}\n was handled!\n')
