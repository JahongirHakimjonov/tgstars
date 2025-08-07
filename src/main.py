import asyncio

from aiogram import Dispatcher
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import bot as handlers
from src.backend.api import router
from src.bot.config import bot

app = FastAPI()
dp = Dispatcher()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await bot.delete_webhook(drop_pending_updates=True)
    handlers.setup(dp)
    asyncio.create_task(dp.start_polling(bot))
