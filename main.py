import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Токен бота
TOKEN = "8598398574:AAEwWXrv_WXb5xfyH7nN9c4V_5Q7pO_n9oE"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Главное меню
def main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Расписание игр"), KeyboardButton(text="Профиль")],
            [KeyboardButton(text="Достижения"), KeyboardButton(text="Рейтинг")]
        ],
        resize_keyboard=True
    )
    return keyboard

# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_menu())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
