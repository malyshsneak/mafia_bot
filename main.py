from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
import os
import json

API_TOKEN = os.getenv("BOT_TOKEN")  # твой токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Кнопка для открытия мини-приложения
web_app_button = KeyboardButton(
    text="Расписание игр",
    web_app=WebAppInfo(url="https://your-domain.com/schedule.html")  # сюда вставь ссылку на веб-app
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[[web_app_button]],
    resize_keyboard=True
)

# Старт бота
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Главное меню", reply_markup=main_menu)

# Обработка данных от mini app
@dp.message(F.web_app_data)
async def handle_webapp_data(message: Message):
    data = json.loads(message.web_app_data.data)
    await message.answer(f"Вы выбрали: Игра {data['game']}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
