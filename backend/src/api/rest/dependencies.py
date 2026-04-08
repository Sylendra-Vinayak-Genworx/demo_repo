from fastapi import Depends


async def get_common_query(q: str | None = None):
    return q
