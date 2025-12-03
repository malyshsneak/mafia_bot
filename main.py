import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
from aiogram import F
from dotenv import load_dotenv
from aiogram.types.web_app_info import WebAppInfo

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главная клавиатура
def main_menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(
        text="Расписание игр",
        web_app=WebAppInfo(url=f"{os.getenv('WEBAPP_URL')}/index.html")
    )
    return kb.as_markup()

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("Главное меню", reply_markup=main_menu_kb())

if __name__ == "__main__":
    import asyncio
    from aiogram import executor

    asyncio.run(dp.start_polling(bot))
