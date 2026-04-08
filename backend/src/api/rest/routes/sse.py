import asyncio

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()


async def event_generator():
    for i in range(1, 6):
        yield f"data: event {i}\n\n"
        await asyncio.sleep(1)


@router.get("/", summary="Server-Sent Events")
async def sse_stream():
    return StreamingResponse(event_generator(), media_type="text/event-stream")
