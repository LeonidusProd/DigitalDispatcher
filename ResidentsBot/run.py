import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.utils.token import TokenValidationError

from handlers import router
from backend_connection import get_bot_token
from exceptions import StartBotException


dp = Dispatcher()

CONNECTION_ATTEMPTS_COUNT = int(os.environ.get(
    "CONNECTION_ATTEMPTS_COUNT",
    default='5'
))

CONNECTION_CYCLES_COUNT = int(os.environ.get(
    "CONNECTION_CYCLES_COUNT",
    default='3'
))

CONNECTION_ATTEMPTS_DELAY = float(os.environ.get(
    "CONNECTION_ATTEMPTS_DELAY",
    default='5'
))

CONNECTION_CYCLES_DELAY = float(os.environ.get(
    "CONNECTION_CYCLES_DELAY",
    default='60'
))


async def main():
    for cycle in range(CONNECTION_CYCLES_COUNT):
        for attempt in range(CONNECTION_ATTEMPTS_COUNT):
            try:
                bot_token = str(await get_bot_token())
                bot = Bot(token=bot_token)
                dp.include_router(router=router)
                await dp.start_polling(bot)
            except TokenValidationError:
                print(f"Cycle {cycle + 1}: Attempt {attempt + 1} of {CONNECTION_ATTEMPTS_COUNT} failed. Invalid token.")
                await asyncio.sleep(delay=CONNECTION_ATTEMPTS_DELAY)

        print(f"Cycle {cycle + 1} of {CONNECTION_CYCLES_COUNT} completed without success.")
        await asyncio.sleep(delay=CONNECTION_CYCLES_DELAY)

    raise StartBotException("It is impossible to launch the bot. Token is invalid!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print(f'Bot is stopped. Reason: Manual exit.')
    except StartBotException as e:
        print(f'Bot is stopped. Reason: {e}')
