from aiogram import Bot
from aiogram.types import LabeledPrice

from bot import bot


class CreateInvoiceService:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def create_invoice(self, user_id: int, username: str, full_name: str) -> str:
        title = "Buy Diamond"
        description = f"Diamond purchase for user {full_name} (@{username})"
        payload = f"diamond_purchase_{user_id}"
        provider_token = ""
        currency = "XTR"
        prices = [LabeledPrice(label="Buy Diamond", amount=5)]
        photo_url = "https://i.postimg.cc/cJTBFWPP/Group-10.png"
        photo_width = 300
        photo_height = 200

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
