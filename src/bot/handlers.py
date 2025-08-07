from aiogram import F, Router
from aiogram.types import (
    Message,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReactionTypeEmoji,
)

from src.bot.config import bot

router = Router()


@router.message(F.text == "/start")
async def start(message: Message) -> None:
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
    caption = (
        "Welcome! Click below to buy with Stars\n\nExchange your stars for joy! ✨ "
        "Unlock special items, features, or moments that bring happiness – "
        "all with your Telegram Stars. "
        "Treat yourself or surprise a friend!"
    )
    await bot.set_message_reaction(
        message.chat.id,
        message.message_id,
        [ReactionTypeEmoji(emoji="❤️")],
        is_big=True,
    )
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://i.postimg.cc/fbM9RjsY/photo-2025-08-06-19-23-14.jpg",
        caption=caption,
        reply_markup=kb,
        reply_to_message_id=message.message_id,
    )


@router.message(F.successful_payment)
async def on_success(message: Message) -> None:
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
