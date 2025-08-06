import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton, LabeledPrice, InlineQueryResultUnion
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

    total_amount = payment.total_amount
    currency = payment.currency
    payload = payment.invoice_payload

    text = (
        f"✅ <b>Payment successful!</b>\n\n"
        f"👤 <b>User:</b> {user.full_name} (<code>{user.id}</code>)\n"
        f"💎 <b>Product:</b> <code>{payload}</code>\n"
        f"💰 <b>Amount paid:</b> <code>{total_amount:.2f} {currency}</code>\n\n"
        f"🎉 Your item has been activated. Thank you!"
    )
    print("=======================================")
    print(f"User: {user.full_name} ({user.id})")
    print(f"Product: {payload}")
    print(f"Amount paid: {total_amount:.2f} {currency}")
    print("=======================================")

    await message.answer(text, parse_mode="HTML")

@dp.message(F.web_app_data)
async def webapp_handler(message: Message):
    query_id = message.web_app_data.query_id
    data = message.web_app_data.data
    prices = [LabeledPrice(label="Buy Diamond", amount=1)]
    await bot.answer_web_app_query(
        web_app_query_id=query_id,
        result=InlineQueryResultUnion(  # aiogram.types.inline_query_result.InlineQueryResultInvoice
            id=query_id,
            title="Diamond",
            description="Purchase a diamond",
            payload=data,
            provider_token="",
            currency="XTR",
            prices=prices,
        ),
    )
    print("=================================")
    print(data)
    print("=================================")



async def main():
    await dp.start_polling(bot)
