from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def get_all_orders():
    return {"message": "Hello, you have accessed the order route"}