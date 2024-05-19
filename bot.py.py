import asyncio

from aiogram import Bot, dispatcher, F 
from aiogram.types import Message

bot = Bot("7197533888:AAHsSj5P_8HTlGW_GnfSptHNtfPvGa4papg") 
dp = dispatcher()


async def main():

  await dp.start_polling(bot)