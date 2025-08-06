import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

from bot import dp, bot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/webapp", response_class=HTMLResponse)
async def serve_webapp():
    with open("webapp/index.html", "r", encoding="utf-8") as f:
        return f.read()


class PayRequest(BaseModel):
    user_id: int
    username: str | None
    full_name: str | None


@app.post("/api/pay")
async def pay(data: PayRequest):
    # Normally you'd validate user, log transaction, check inventory, etc.
    print(data)
    return JSONResponse({
        "status": "ok",
        "slug": "buy_diamond_5_stars"  # Must be pre-configured in Telegram Stars
    })


@app.on_event("startup")
async def on_startup():
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot))
