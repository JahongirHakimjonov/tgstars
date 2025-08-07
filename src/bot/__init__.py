from aiogram import Dispatcher

from src.bot.handlers import router as start_router
from src.bot.querys import router as query_router


def setup(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(query_router)
