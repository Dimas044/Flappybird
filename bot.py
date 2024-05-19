from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('7197533888:AAHsSj5P_8HTlGW_GnfSptHNtfPvGa4papg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton('',web_app=WebAppInfo(url='')))

executor.start_polling(dp)
