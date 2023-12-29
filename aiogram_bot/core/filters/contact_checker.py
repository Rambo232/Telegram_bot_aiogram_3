from aiogram.filters import BaseFilter
from aiogram.types import Message


class isTrueContact(BaseFilter):
    async def __call__(self, message: Message):
        try:
            if message.contact.user_id == message.from_user.id:
                return {'phone': message.contact.phone_number}
            else:
                return False

        except:
            print(f'Пользователь с id: {message.from_user.id} и именем '
                  f'{message.from_user.first_name}, отправил не свой контакт\n')
            return False

