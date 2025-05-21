from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContextfrom 
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
import asyncio
from main import dp, bot


async def admin_handler(message: Message):
    await message.answer("Введи паоль: ")
@dp.message(F.text == "valera")
async def admin_handler(message: Message):
    await message.answer("ты в админке")




