from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
import asyncio
from kb import main_kb, admin_kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from db1 import conn, cursor
from db2 import conn_f, cursor_f, food_insert

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

@dp.message(Command("form"))
async def from_FSM(message:Message, state: FSMContext):
    await message.answer("Привет введи своё имя")
    await state.set_state(From.name)

@dp.message(From.name)
async def name_FSM(message: Message, state: FSMContext):
    await message.answer("Супер! теперь введи свой возраст")
    await state.update_data(name=message.text)
    await state.set_state(From.age)

@dp.message(From.age)
async def age_FSM(message: Message, state: FSMContext):
    await message.answer("Отлично! Но какой у тебя любимый фильм? ")
    await state.update_data(age=message.text)
    await state.set_state(From.movie)

@dp.message(From.movie)
async def movie_FSM(message: Message, state: FSMContext):
    await message.answer("Отлично! Ты выполнил форму)")
    await state.update_data(movie=message.text)
    data = state.get_data()
    print(data)
    await state.clear()


@dp.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета отменена.")

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



#####################
####### ADMIN #######
#####################
class add_product(StatesGroup):
    name=State()
    price=State()



@dp.message(Command("admin"))
async def admin_handler(message: Message):
    await message.answer("Введи паоль: ")
@dp.message(F.text == "13211")
async def admin_handler(message: Message):
    await message.answer("Ты в админке", reply_markup=admin_kb)

@dp.callback_query(F.data == "add")
async def add_name(message: Message, state: FSMContext ):
    await message.answer("Привет! Чтобы добваить новый продукт напиши тут название: ")
    await state.set_state(add_product.name)

@dp.message(add_product.name)
async def add_price(message: Message, state: FSMContext):
    await message.answer("Мне ещё нужна цена этого продукта: ")
    await state.update_data(name=message.text)
    await state.set_state(add_product.price)

@dp.message(add_product.price)
async def all_data(message: Message, state: FSMContext):
    await message.answer("Супер! ") 
    await state.update_data(price=message.text)
    data = await state.get_data()
    await message.answer(str(data))
    food_insert(data["name"], data["price"])
    await message.answer("Данные сохраненны в базе данных")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
