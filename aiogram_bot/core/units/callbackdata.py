from aiogram.filters.callback_data import CallbackData


class MackInfo(CallbackData, prefix='mac'):
    model: str
    diagonal_size: int
    chip: str
    year: int
