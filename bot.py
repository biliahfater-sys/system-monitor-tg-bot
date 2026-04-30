import asyncio
import os
import platform
import subprocess

import psutil
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


TOKEN = os.getenv("TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

if not TOKEN:
    raise ValueError("TOKEN is not set in .env")

if OWNER_ID == 0:
    raise ValueError("OWNER_ID is not set in .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()


def is_owner(message: types.Message) -> bool:
    return message.from_user and message.from_user.id == OWNER_ID


def system_info() -> dict:
    return {
        "CPU": psutil.cpu_percent(interval=1),
        "RAM": psutil.virtual_memory().percent,
    }


def ping(host: str = "8.8.8.8") -> bool:
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
        )
        return result.returncode == 0
    except Exception:
        return False


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if not is_owner(message):
        return
    await message.answer("Бот запущен и работает.")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    if not is_owner(message):
        return
    await message.answer(
        "Доступные команды:\n"
        "/start — запуск\n"
        "/status — статус системы"
    )


@dp.message(Command("status"))
async def cmd_status(message: types.Message):
    if not is_owner(message):
        return

    info = system_info()
    network = "Да" if ping() else "Нет"

    await message.answer(
        f"CPU: {info['CPU']}%\n"
        f"RAM: {info['RAM']}%\n"
        f"Сеть: {network}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())