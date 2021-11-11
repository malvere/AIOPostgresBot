from functions import request as isClaimed, rawincount as rcount
from tqdm.contrib.telegram import tqdm

from db import DataBase
from testTable import TestTable

from aiogram import Bot, Dispatcher, executor
import asyncio
import logging

import envars

# Logs level
logging.basicConfig(level=logging.INFO)

# AIO init
bot = Bot(token=envars.API_TOKEN)
dp = Dispatcher(bot)

# DB init
DB = DataBase(url=envars.DB_URL)

# File with generated usernames
fileName = 'generated.txt'


@dp.message_handler(commands=['start'])
async def parseLoop(self):
    with open(fileName, 'r') as f:
        pbar = tqdm(
            f,
            total=rcount(fileName),
            token=envars.API_TOKEN,
            chat_id=envars.ADMIN)

        for line in pbar:
            line = line[:-1]
            pbar.set_description(line)

            if isClaimed(line) is False:
                DB.add(TestTable, line)
                print(line)
                await bot.send_message(chat_id=envars.ADMIN, text=line)

            elif isClaimed(line) == 'wait':
                pbar.set_description(f'Limit reached, waiting 60 s. ({line})')
                await bot.send_message(
                    chat_id=envars.ADMIN,
                    text=f'{line} was skipped')
                await asyncio.sleep(60)
            await asyncio.sleep(1)

    DB.commit()
    DB.close()


@dp.message_handler(commands=['help'])
async def infoCommand(self):
    await bot.send_message(chat_id=envars.ADMIN, text=envars.USER_AGENT)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
