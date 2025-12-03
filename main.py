from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio

TOKEN = "8598398574:AAEwWXrv_WXb5xfyH7nN9c4V_5Q7pO_n9oE"

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Команда /start
@dp.message(Command(commands=["start"]))
async def start(message: types.Message):
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Расписание игр")
    keyboard.button(text="Профиль")
    keyboard.button(text="Достижения")
    keyboard.button(text="Рейтинг")
    keyboard.adjust(2)  # 2 кнопки в ряд
    await message.answer("Главное меню", reply_markup=keyboard.as_markup(resize_keyboard=True))

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
