import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN is not set in the environment variables")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
