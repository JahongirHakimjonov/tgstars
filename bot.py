import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Buy Diamond ⭐",
                    web_app=WebAppInfo(url="https://tgstar.milliytech.uz/webapp"),
                )
            ]
        ]
    )
    await message.answer("Welcome! Click below to buy with Stars:", reply_markup=kb)


@dp.message(F.successful_payment)
async def on_success(message: Message):
    payment = message.successful_payment
    user = message.from_user

    total_amount = payment.total_amount / 100  # For Stars, 1 = 100 units
    currency = payment.currency
    payload = payment.invoice_payload

    text = (
        f"✅ <b>Payment successful!</b>\n\n"
        f"👤 <b>User:</b> {user.full_name} (<code>{user.id}</code>)\n"
        f"💎 <b>Product:</b> <code>{payload}</code>\n"
        f"💰 <b>Amount paid:</b> <code>{total_amount:.2f} {currency}</code>\n\n"
        f"🎉 Your item has been activated. Thank you!"
    )

    await message.answer(text, parse_mode="HTML")


async def main():
    await dp.start_polling(bot)
