import asyncio
from datetime import datetime
from typing import List

import aioping
from model import Result, Server
from settings import settings


async def ping(server: Server) -> Result:
    try:
        delay_ms = await aioping.ping(str(server.ip), timeout=1)
        return Result(server=server, result=delay_ms)
    except (TimeoutError, OSError):
        return Result(server=server)


async def ping_servers(servers: List[Server]) -> List[Result]:
    return await asyncio.gather(*[ping(server) for server in servers])


def pretty_output(results: List[Result]) -> str:
    text = f'{datetime.now(tz=settings.TIMEZONE).strftime("%H:%M:%S %Z")}\n\n'
    for r in results:
        status = '🔴down' if r.result is None else f'🟢{r.result} ms'
        text += f'{status} {r.server.name}, {r.server.ip}\n'
    return text
