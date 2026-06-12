import asyncio

class APIClient:
    async def __aenter__(self):
        print("API session started")
        return self

    async def __aexit__(self,exc_type,exc, tb):
        print("API session closed")

    async def get_data(self,url):
        print(f"Fetching {url}")
        await asyncio.sleep(2)
        return f"Data from(url)"

async def main():
    async with APIClient() as client:
        data1 = await client.get_data("api/user")
        data2 = await client.get_data("api/orders")

        print(data1)
        print(data2)


asyncio.run(main())