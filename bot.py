from aiogram import Bot, Dispatcher, types, Router
from aiogram.enums import ParseMode
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="7919086638:AAHBFMgyxvIKskatxodF6pESKvVlucsWOrk")
dp = Dispatcher()
router = Router()


@router.message()
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Open WebApp",
            web_app=WebAppInfo(url="https://tgstar.milliytech.uz")  # Update to your domain
        )]
    ])
    await message.answer("Click below to open the store and pay with Stars!", reply_markup=kb)


dp.include_router(router)
