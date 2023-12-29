from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChatAdministrators


async def set_command(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начать'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='reset', description='Сбросить'),
        BotCommand(command='inline', description='Показать инлайн клавиатуру'),
        BotCommand(command='pay', description='Купить кибероны')

    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


# async def set_admin_command(bot: Bot):
#     commands = [
#         BotCommand(command='start', description='Начать'),
#         BotCommand(command='help', description='Помощь'),
#         BotCommand(command='reset', description='Сбросить')
#     ]
#
#     admin_commands = [
#         BotCommand(command='logging', description='Посмотреть логи'),
#         BotCommand(command='start -> bot', description='Запустить бота'),
#         BotCommand(command='stop -> bot', description='Остановить бота')
#     ]
#
#     await bot.set_my_commands(admin_commands, BotCommandScopeChatAdministrators())
#     await bot.set_my_commands(commands, BotCommandScopeDefault())
