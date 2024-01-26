from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



menu_start = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Твой Профиль', callback_data='buy'),
        InlineKeyboardButton(text='🤙Купить курить🤙', callback_data='profile')
    ],
    [
        InlineKeyboardButton(text='‼️Акция "Приведи друга"‼️', callback_data='refs')
    ],
    [
        InlineKeyboardButton(text='Информация📌', callback_data='inform'),
        InlineKeyboardButton(text='Связь', callback_data='call_back')
    ]
])



sale_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='🥴Купить грамм', callback_data='gramm'),
        InlineKeyboardButton(text='Полка(0.5гр)', callback_data='polka')
    ],
    [
        InlineKeyboardButton(text='🚢Купить корабль', callback_data='full'),
        InlineKeyboardButton(text='Полка(0.5корабля)',callback_data='path_full')
    ],
    [
        InlineKeyboardButton(text='🤯Купить стакан', callback_data='glass')
    ],
    [
        InlineKeyboardButton(text='🤫Пятка', callback_data='decl')
        ]
    ])


profile = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='')
    ]
])