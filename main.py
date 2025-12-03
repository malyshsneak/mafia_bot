import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp import web
import os

TOKEN = os.getenv("BOT_TOKEN")  # Убедись, что токен в Environment Variables на Render

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главное меню
keyboard_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Расписание игр")],
        [KeyboardButton(text="Другое")]
    ],
    resize_keyboard=True
)

@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Главное меню", reply_markup=keyboard_main)

@dp.message(lambda message: message.text == "Расписание игр")
async def schedule_handler(message: types.Message):
    # Мини-приложение имитация выбора игры
    games = ["Игра 1", "Игра 2", "Игра 3"]
    text = "Выберите игру:\n" + "\n".join(f"{i+1}. {g}" for i, g in enumerate(games))
    await message.answer(text)

async def main():
    # Запуск polling
    await dp.start_polling(bot)

# Фиктивный сервер для Render
async def handle(request):
    return web.Response(text="OK")

app = web.Application()
app.add_routes([web.get("/", handle)])

# Запускаем одновременно polling и сервер
loop = asyncio.get_event_loop()
loop.create_task(main())
web.run_app(app, port=10000)
