import asyncio

async def get_user():
    await asyncio.sleep(2)
    return "User Data"

async def get_orders():
    await asyncio.sleep(3)
    return "Orders Data"

async def get_payments():
    await asyncio.sleep(1)
    return "Payment Data"

async def main():
    user, orders, payments = await asyncio.gather(
        get_user(),
        get_orders(),
        get_payments()
    )

    print(user)
    print(orders)
    print(payments)

asyncio.run(main())