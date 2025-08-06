import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.methods import RefundStarPayment
from aiogram.types import (
    Message, PreCheckoutQuery, WebAppInfo,
    InlineKeyboardMarkup, InlineKeyboardButton
)
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text="Buy Diamond ⭐",
                web_app=WebAppInfo(url="https://tgstar.milliytech.uz/webapp")
            )
        ]]
    )
    await message.answer("Welcome! Click below to buy with Stars:", reply_markup=kb)


@dp.pre_checkout_query()
async def pre_checkout(q: PreCheckoutQuery):
    await q.answer(ok=True)


@dp.message(F.successful_payment)
async def on_success(message: Message):
    payment = message.successful_payment
    user = message.from_user

    total_amount = payment.total_amount / 100  # to‘liq summa
    currency = payment.currency
    payload = payment.invoice_payload
    tg_charge = payment.telegram_payment_charge_id
    prov_charge = payment.provider_payment_charge_id

    print("========= PAYMENT =========")
    print(f"User: {user.full_name} ({user.id})")
    print(f"Payload: {payload}")
    print(f"Telegram charge ID: {tg_charge}")
    print(f"Provider charge ID: {prov_charge}")
    print(f"Amount paid: {int(total_amount * 100)} {currency}")
    print("===========================")

    text = (
        f"✅ <b>Payment successful!</b>\n\n"
        f"👤 <b>User:</b> {user.full_name} (<code>{user.id}</code>)\n"
        f"💎 <b>Product:</b> <code>{payload}</code>\n"
        f"💰 <b>Amount:</b> <code>{int(total_amount * 100)} {currency}</code>\n\n"
        f"🎉 Your item has been activated. Thank you!"
    )
    await message.answer(text, parse_mode="HTML")


@dp.message(Command("refund"))
async def refund_command(message: Message):
    charge_id = "stxPnVqs9M0PztkdCF0aAFD5ePd6suymPMgPoE7SaxKmMf11ZRLEIX6Ttt66DqOu4LeJQXuQHejvKq5B7tkbzEUjJxBEFRYB3N1YykSA1sHIB3WYLybX5qmvkEdBOT4p5Zc"
    user_id = message.from_user.id

    result = await bot(RefundStarPayment(
        user_id=user_id,
        telegram_payment_charge_id=charge_id
    ))
    if result:
        await message.answer("✅ Refund has been made. Please check your account.")
    else:
        await message.answer("❌ Refund failed. Please try again later.")


async def main():
    await dp.start_polling(bot)
