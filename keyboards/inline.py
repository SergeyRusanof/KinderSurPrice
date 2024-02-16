from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MyCallBack(CallbackData, prefix='my_callback'):
    zap: str


class MyLocation(CallbackData, prefix='my_location'):
    loc: str


class ToBuy(CallbackData, prefix='to_buy'):
    buy: str


def menu_start():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='🖥 Твой Профиль', callback_data=MyCallBack(zap='profile'))
    keyboard.button(text='🤙Купить курить🤙', callback_data=MyCallBack(zap='buy'))
    keyboard.button(text='‼️Акция "Приведи друга"‼️', callback_data=MyCallBack(zap='refs'))
    keyboard.button(text='Информация 📌', callback_data=MyCallBack(zap='inform'))
    keyboard.button(text='Связь 📲', callback_data=MyCallBack(zap='call_back'))
    keyboard.adjust(2, 1, 2)
    return keyboard.as_markup()


def sale_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='🥴Купить грамм', callback_data=MyCallBack(zap='gramm'))
    keyboard.button(text='Полка(0.5гр)', callback_data=MyCallBack(zap='polka'))
    keyboard.button(text='🚢Купить корабль', callback_data=MyCallBack(zap='full'))
    keyboard.button(text='Полка(0.5корабля)', callback_data=MyCallBack(zap='path_full'))
    keyboard.button(text='🤯Купить стакан', callback_data=MyCallBack(zap='glass'))
    keyboard.button(text='🤫Пятка', callback_data=MyCallBack(zap='decl'))
    keyboard.adjust(2,2,2)
    return keyboard.as_markup()


def location():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Центр', callback_data=MyLocation(loc='city'))
    keyboard.button(text='Блочок', callback_data=MyLocation(loc='block'))
    keyboard.button(text='Фильтры', callback_data=MyLocation(loc='filtry'))
    keyboard.button(text='Ватутино', callback_data=MyLocation(loc='vatut'))
    keyboard.button(text='Красный', callback_data=MyLocation(loc='red'))
    keyboard.button(text='Зуевский', callback_data=MyLocation(loc='zuev'))
    keyboard.adjust(2,2,2)
    return keyboard.as_markup()


def list_pay():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Купить', callback_data=ToBuy(buy='ok_pay'))
    keyboard.button(text='Отменить', callback_data=ToBuy(buy='cancel'))
    keyboard.adjust(2,2,2)
    return keyboard.as_markup()