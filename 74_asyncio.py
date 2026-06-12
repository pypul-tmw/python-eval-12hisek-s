import asyncio

async def send_email(user):
    print(f"Sending email to {user}")
    await asyncio.sleep(1)
    print(f"Email sent to {user}")

async def main():
    await asyncio.gather(
        send_email("A"),
        send_email("B"),
        send_email("C"),
        send_email("D"),
    )

asyncio.run(main())