import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv)

API_TOKEN = os.getenv("API_TOKEN")
MINI_APP_URL = os.getenv("MINI_APP_URL")


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Открыть приложение")],
        [KeyboardButton(text="Поддержка")]
    ],
    resize_keyboard=True
)

@dp.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать! Используйте кнопки ниже:", reply_markup=kb)

@dp.message()
async def handle_text(message: types.Message):
    if message.text == "Открыть приложение":
        await message.reply(
            "Открыть приложение для оценок:",
            reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[
                types.InlineKeyboardButton(
                    text="Запустить приложение",
                    web_app=types.WebAppInfo(url=MINI_APP_URL)
                )
            ]])
        )
    elif message.text == "Поддержка":
        await message.reply("Свяжитесь с поддержкой: @ВашИмяПоддержки")

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())