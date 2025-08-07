from aiogram import Router
from aiogram.types import PreCheckoutQuery

router = Router()


@router.pre_checkout_query()
async def pre_checkout(q: PreCheckoutQuery) -> None:
    await q.answer(ok=True)
