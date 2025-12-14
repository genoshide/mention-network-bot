import asyncio
import sys
import ctypes
from src.starter import start_system

if sys.platform == 'win32':
    ctypes.windll.kernel32.SetConsoleTitleW("Genoshide Mention Bot v1.0 (Premium Edition)")
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == "__main__":
    try:
        asyncio.run(start_system())
    except KeyboardInterrupt:
        pass