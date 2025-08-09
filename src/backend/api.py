from fastapi import Depends, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

from src.backend.schema import RefundRequest, PayRequest
from src.bot.services import CreateInvoiceService, get_invoice_service

router = APIRouter()


@router.get("/webapp", response_class=HTMLResponse)
async def serve_webapp() -> str:
    with open("src/web/index.html", "r", encoding="utf-8") as f:
        return f.read()


@router.get("/market", response_class=HTMLResponse)
async def serve_webapp() -> str:
    with open("src/market/market.html", "r", encoding="utf-8") as f:
        return f.read()


@router.post("/api/pay")
async def pay(
    data: PayRequest, invoice: CreateInvoiceService = Depends(get_invoice_service)
) -> JSONResponse:
    user_id = data.user_id
    username = data.username
    full_name = data.full_name
    amount = data.amount

    print(f"Payment received from user {user_id} ({username}, {full_name})")
    invoice_url = await invoice.create_invoice(user_id, username, full_name, amount)
    return JSONResponse({"status": "ok", "invoice_url": f"{invoice_url}"})


@router.post("/api/refund")
async def refund(
        data: RefundRequest, invoice: CreateInvoiceService = Depends(get_invoice_service)
) -> JSONResponse:
    user_id = data.user_id
    charge_id = data.charge_id

    print(f"Refund requested by user {user_id} (charge_id: {charge_id})")
    refund_status = await invoice.process_refund(user_id, charge_id)
    return JSONResponse({"status": "ok", "refund_status": refund_status})
