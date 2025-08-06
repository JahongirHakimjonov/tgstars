import asyncio

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from bot import dp, bot

app = FastAPI()


@app.post("/api/pay")
async def handle_stars_payment(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    username = data.get("username")
    full_name = data.get("full_name")

    # You can add Telegram WebApp initData verification here if needed

    print(f"[✅] Stars payment received from {username} ({user_id}) - {full_name}")

    # Here you would normally store to DB, update user balance, etc.
    return JSONResponse({"status": "ok"})


@app.on_event("startup")
async def on_startup():
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot))
