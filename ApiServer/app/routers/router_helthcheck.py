from fastapi import APIRouter

import asyncio


router = APIRouter()


@router.get("")
def get_helthcheck():
    return {"status": "ok"}


@router.get("/test")
async def get_test():
    await asyncio.sleep(3)
    return {"key": "value"}
