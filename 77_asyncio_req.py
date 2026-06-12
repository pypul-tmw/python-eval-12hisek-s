import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.google.com") as response:
            html = await response.text()
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())