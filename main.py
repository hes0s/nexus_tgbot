from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
import asyncio
from aiogram.types import CallbackQuery, callback_query, callback_game
from kb import main_kb

bot = Bot(
    token='8003890596:AAGG1lvosdjD38_atfrdiTO_mZ4Jdf9fekU',
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
"""
@dp.message(Command("game"))
async def echo(message: Message):
    await message.answer("Какое из животных не умеет прыгать", reply_markup=game_kb)
    


@dp.callback_query(F.data=="right")
async def menu_callback(callback: Message):
    await callback.message.answer("Дааа!! это же кит")
    await callback.answer()

@dp.callback_query(F.data=="wrong")
async def menu_callback(callback: Message):
    await callback.message.answer("О нееет попробуй еще разок")
    await callback.message.answer("Какое из животных не умеет прыгать", reply_markup=game_kb)
    await callback.answer()

    

"""

@dp.message(Command("start"))
async def start_com(message: Message):
    await message.answer("Привет, это бот для заказа еды", reply_markup=main_kb)

@dp.message(Command("admin"))
async def admin_(message:Message):
    await message.answer("Если ты админ напиши пароль: ")

@dp.message(F.text=="1234")
async def admin__(message:Message):
    await message.answer("Ты теперь админ")

@dp.message(F.text == "Меню")
async def ech(message: Message):
    await message.answer("Вот ваше меню)", reply_markup=main_kb)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

@dp.message(F.text == "О нас")
async def ec(message: Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.answer("Тут о нас)",reply_markup=main_kb)


@dp.message(F.text == "Контакты")
async def e(message: Message):
    await message.answer("Наш номер телефона: +373 600 00 00", reply_markup=main_kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
