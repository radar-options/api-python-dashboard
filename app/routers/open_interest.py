from typing import List
import datetime as dt
from fastapi import APIRouter
from starlette.requests import Request

from core.APILayer import APILayer

router = APIRouter(prefix="/api/v1/open_interest", tags=["open_interest"])


@router.get("/{date}")
async def get_open_interest(
    request: Request,
    date: dt.date
) -> List[dict]:
    apilayer: APILayer = request.app.state.APILayer
    return apilayer.find(
        date=date
    )