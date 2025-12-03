import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Главное меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("Расписание игр"))
main_menu.add(KeyboardButton("Профиль"))
main_menu.add(KeyboardButton("Достижения"))
main_menu.add(KeyboardButton("Рейтинг"))

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в клуб Мафии!", reply_markup=main_menu)

# Обработчик кнопок главного меню
@dp.message_handler(lambda message: message.text == "Расписание игр")
async def schedule(message: types.Message):
    await message.answer("Здесь будет расписание игр.")

@dp.message_handler(lambda message: message.text == "Профиль")
async def profile(message: types.Message):
    await message.answer("Здесь будет ваш профиль.")

@dp.message_handler(lambda message: message.text == "Достижения")
async def achievements(message: types.Message):
    await message.answer("Здесь будут достижения.")

@dp.message_handler(lambda message: message.text == "Рейтинг")
async def rating(message: types.Message):
    await message.answer("Здесь будет рейтинговая таблица.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
