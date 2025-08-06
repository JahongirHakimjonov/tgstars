import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.methods import RefundStarPayment
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
    payment = message.successful_payment
    user = message.from_user
    print(str(payment))

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


@dp.message(Command("refund"))
async def refund_command(message: Message):
    charge_ids = [
        "stxJCpqI0VYGFDMiMgy0sBFvHT5OM5kT5yUH4KrOODEOoFIOGC-kIOtSR0fIpphCFyTNfLyD4idM1ZDY_SCtJaqV0eYlfMnlnaSUwDv5LxlNFRQCg0pBNz2e4nPqw73nhv5",
        "stxkiMEHR6jzGLvtdm4Wjo6XnehXDkY-MVVfiXXH7xCBXDZ8x6jw6xRBTje-mZCgbZEQHDD4o21lx2Ga9Ys5O_0SgPcl3xerIGAdStIDdU7L9eFNgirgkrlJUpvwd_HU5u3",
        "stxTpv3jVy1tomna5RHVGUqkTVjwFP4glNH31ueOBN8smBNdX8kMLwRzNS6-musRbV-crqvHiX19UlOMWcEG40_1WG7sV13KcUlMIijEym_5AiypS5BpUbHhq-j9xlxLTMI",
    ]
    user_id = message.from_user.id
    try:
        for charge_id in charge_ids:
            result = await bot(
                RefundStarPayment(user_id=user_id, telegram_payment_charge_id=charge_id)
            )
            if result:
                await message.answer("✅ Refund has been made. Please check your account.")
            else:
                await message.answer("❌ Refund failed. Please try again later.")
    except Exception as e:
        await message.answer(f"❌ An error occurred: {str(e)}")


async def main():
    await dp.start_polling(bot)
