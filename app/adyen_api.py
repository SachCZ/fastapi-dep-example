from fastapi import APIRouter, Depends
from app.adyen_client import AdyenClient


router = APIRouter(prefix="/api")


@router.get("/items")
async def read_items(adyen_client: AdyenClient = Depends(AdyenClient)):
    return adyen_client.get_items()
