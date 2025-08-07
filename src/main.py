import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.backend.api import router
from src.bot.config import bot, dp

app = FastAPI()

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
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot))
