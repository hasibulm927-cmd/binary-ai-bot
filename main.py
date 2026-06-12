import asyncio
from telegram_sender import send_signal

async def main():
    await send_signal("✅ Binary AI Bot Started")

if __name__ == "__main__":
    asyncio.run(main())
