from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="О нас"),
            KeyboardButton(text="Контакты"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)


menu_kbjj = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню"),
            KeyboardButton(text="Далее")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

contacts_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Номер телефона"),
            KeyboardButton(text="Адрес"),
            KeyboardButton(text="Главное меню")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

main_kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Меню", callback_data="menu"),
            InlineKeyboardButton(text="О нас", callback_data="about"),
            InlineKeyboardButton(text="Контакты", callback_data="contacts")
        ]
    ]
)
