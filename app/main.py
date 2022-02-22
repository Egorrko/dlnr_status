import asyncio

from bot import send_info_to_channel
from ping import ping_servers, pretty_output
from settings import settings


async def main_loop():
    while True:
        results = await ping_servers(settings.SERVERS)
        pretty_text = pretty_output(results)
        await send_info_to_channel(pretty_text)
        await asyncio.sleep(5)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main_loop())
    loop.run_forever()
