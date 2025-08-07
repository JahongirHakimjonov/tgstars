from aiogram.types import PreCheckoutQuery

from src.bot.config import dp


@dp.pre_checkout_query()
async def pre_checkout(q: PreCheckoutQuery) -> None:
    await q.answer(ok=True)
