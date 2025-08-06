import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Buy Diamond ⭐",
            web_app=WebAppInfo(url="https://tgstar.milliytech.uz/webapp")
        )]
    ])
    await message.answer("Welcome! Click below to buy with Stars:", reply_markup=kb)


@dp.message(F.successful_payment)
async def on_success(message: Message):
    await message.answer("✅ Payment successful! Your item is now activated.")
    # Optional: write to database or grant access


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
