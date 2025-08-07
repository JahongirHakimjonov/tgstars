from pydantic import BaseModel


class PayRequest(BaseModel):
    user_id: int
    username: str
    full_name: str
    amount: int


class RefundRequest(BaseModel):
    user_id: int
    charge_id: str
