from aiogram import Bot
from aiogram.types import LabeledPrice
import random
from bot import bot


class CreateInvoiceService:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def create_invoice(self, user_id: int, username: str, full_name: str) -> str:
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
        prices = [LabeledPrice(label="Buy 1 Diamond in 1 Game", amount=1)]
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


def get_invoice_service():
    return CreateInvoiceService(bot=bot)
