import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

API_TOKEN = os.getenv("BOT_TOKEN")  # твой токен, добавленный в Render

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Главное меню с кнопкой "Расписание игр"
@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Расписание игр", callback_data="schedule"))
    await message.answer("Главное меню", reply_markup=keyboard.as_markup())

# Обработка нажатия кнопки "Расписание игр"
@dp.callback_query(lambda c: c.data == "schedule")
async def show_schedule(callback_query: types.CallbackQuery):
    # Mini app с выбором игр
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text="Игра 1", callback_data="game_1"),
        InlineKeyboardButton(text="Игра 2", callback_data="game_2"),
        InlineKeyboardButton(text="Игра 3", callback_data="game_3"),
    )
    await callback_query.message.edit_text(
        "Выберите игру:", reply_markup=keyboard.as_markup()
    )

# Обработка выбора игры
@dp.callback_query(lambda c: c.data.startswith("game_"))
async def game_selected(callback_query: types.CallbackQuery):
    await callback_query.answer(f"Вы выбрали {callback_query.data.replace('game_', 'Игра ')}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
