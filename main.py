import asyncio

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

from bot import dp, bot
from services import CreateInvoiceService
from services import get_invoice_service

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PayRequest(BaseModel):
    user_id: int
    username: str
    full_name: str


@app.get("/webapp", response_class=HTMLResponse)
async def serve_webapp():
    with open("webapp/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/api/pay")
async def pay(
    data: PayRequest, invoice: CreateInvoiceService = Depends(get_invoice_service)
):
    user_id = data.user_id
    username = data.username
    full_name = data.full_name

    print(f"Payment received from user {user_id} ({username}, {full_name})")
    invoice_url = await invoice.create_invoice(user_id, username, full_name)
    return JSONResponse({"status": "ok", "invoice_url": f"{invoice_url}"})


@app.on_event("startup")
async def on_startup():
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot))
