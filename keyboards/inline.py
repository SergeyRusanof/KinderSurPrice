from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.database import DataBase

db = DataBase('mainbase.db')


class MyCallBack(CallbackData, prefix='my_callback'):
    zap: str


class MyLocation(CallbackData, prefix='my_location'):
    loc: str


class ToBuy(CallbackData, prefix='to_buy'):
    buy: str


class ToAdmin(CallbackData, prefix='to_adm'):
    adm: str


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
    gr = db.count_products('Грамм')
    pgr = db.count_products('Полка (0,5 грамма)')
    kr = db.count_products('Корабль')
    pkr = db.count_products('Полка (0,5 корабля)')
    decl = db.count_products('Пятка')
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=f'🥴Купить грамм *({gr}шт)*', callback_data=MyCallBack(zap='gramm'))
    keyboard.button(text=f'Полка(0.5гр)  *({pgr}шт)*', callback_data=MyCallBack(zap='polka'))
    keyboard.button(text=f'🚢Купить корабль  *({kr}шт)*', callback_data=MyCallBack(zap='full'))
    keyboard.button(text=f'Полка(0.5корабля)  *({pgr}шт)*', callback_data=MyCallBack(zap='path_full'))
    keyboard.button(text='🤯Купить стакан', callback_data=MyCallBack(zap='glass'))
    keyboard.button(text=f'🤫Пятка  *({decl}шт)*', callback_data=MyCallBack(zap='decl'))
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


def admin_start():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Добавить локацию', callback_data=ToAdmin(adm='add_loc'))
    keyboard.button(text='Просмотреть данные по id', callback_data=ToAdmin(adm='look_id'))
    keyboard.button(text='Выдать бонус по id', callback_data=ToAdmin(adm='get_bonus'))
    keyboard.button(text='Все участники', callback_data=ToAdmin(adm='all_users'))
    keyboard.button(text='Продажи', callback_data=ToAdmin(adm='stat_sales'))
    keyboard.adjust(2, 2, 2)
    return keyboard.as_markup()


def menu_profile():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Забрать бонус', callback_data='ghr')
    keyboard.button(text='Назад', callback_data='bdf')
    keyboard.adjust(2, 2, 2)
    return keyboard.as_markup()