import asyncio
from mt5_reader import connect_mt5
from telegram_sender import send_signal

async def main():

    if connect_mt5():
        await send_signal("✅ MT5 Connected Successfully")
    else:
        await send_signal("❌ MT5 Connection Failed")

if __name__ == "__main__":
    asyncio.run(main())
