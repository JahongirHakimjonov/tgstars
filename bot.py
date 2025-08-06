import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    PreCheckoutQuery,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN is not set in the environment variables")

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


@dp.pre_checkout_query()
async def pre_checkout(q: PreCheckoutQuery):
    await q.answer(ok=True)


@dp.message(F.successful_payment)
async def on_success(message: Message):
    assert message.successful_payment is not None, "No successful_payment found"
    assert message.from_user is not None, "No from_user found"

    payment = message.successful_payment
    user = message.from_user

    total_amount = payment.total_amount
    currency = payment.currency
    payload = payment.invoice_payload
    tg_charge = payment.telegram_payment_charge_id
    prov_charge = payment.provider_payment_charge_id

    print("========= PAYMENT =========")
    print(f"User: {user.full_name} ({user.id})")
    print(f"Payload: {payload}")
    print(f"Telegram charge ID: {tg_charge}")
    print(f"Provider charge ID: {prov_charge}")
    print(f"Amount paid: {total_amount} {currency}")
    print("===========================")

    text = (
        f"✅ <b>Payment successful!</b>\n\n"
        f"👤 <b>User:</b> {user.full_name} (<code>{user.id}</code>)\n"
        f"💎 <b>Product:</b> <code>{payload}</code>\n"
        f"💰 <b>Amount:</b> <code>{total_amount} {currency}</code>\n\n"
        f"🎉 Your item has been activated. Thank you!"
    )
    await message.answer(text, parse_mode="HTML")


async def main():
    await dp.start_polling(bot)
