import random

from aiogram import Bot
from aiogram.methods import RefundStarPayment
from aiogram.types import LabeledPrice

from bot import bot


class CreateInvoiceService:
    def __init__(self, tg_bot: Bot):
        self.bot = tg_bot

    async def create_invoice(self, user_id: int, username: str, full_name: str, amount: int) -> str:
        images = [
            "https://i.postimg.cc/DwTdr6xW/download-6.jpg",
            "https://i.postimg.cc/JhTNWLMJ/download-7.jpg",
            "https://i.postimg.cc/L6dzSvKy/download-8.jpg",
        ]
        title = "Buy 1 Diamond in 1 Game"
        description = f"Diamond purchase for user {full_name} (@{username})"
        payload = f"diamond_purchase_{user_id}"
        provider_token = ""
        currency = "XTR"
        prices = [LabeledPrice(label="Buy 1 Diamond in 1 Game", amount=amount)]
        photo_url = random.choice(images)
        photo_width = 400
        photo_height = 400

        invoice_url = await self.bot.create_invoice_link(
            title=title,
            description=description,
            payload=payload,
            provider_token=provider_token,
            currency=currency,
            prices=prices,
            photo_url=photo_url,
            photo_width=photo_width,
            photo_height=photo_height,
        )

        return invoice_url

    async def process_refund(self, user_id: int, charge_id: str) -> bool:
        try:
            result = await bot(
                RefundStarPayment(user_id=user_id, telegram_payment_charge_id=charge_id)
            )
            if result:
                await self.bot.send_message(
                    user_id, "✅ Refund has been made. Please check your account."
                )
                return True
            else:
                await self.bot.send_message(
                    user_id, "❌ Refund failed. Please try again later."
                )
                return False
        except Exception as e:
            await self.bot.send_message(user_id, f"❌ An error occurred: {str(e)}")
            return False


def get_invoice_service():
    return CreateInvoiceService(tg_bot=bot)
