import aiogram
import os
from aiogram import Dispatcher, types, executor, Bot
import logging
import filter
import btn

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5172724216:AAFMYh6YgbwF0ii9CaDyMU8hiWfsZmOxdhA')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Assalomu aleykum {message.from_user.full_name}!\n\n<b>Iltmos ismingizni kiriting: </b>", parse_mode='html')

@dp.message_handler()
async def ism(message: types.Message):
    file = filter.edit(message.text)
    await bot.send_photo(chat_id=message.chat.id, photo=open(f"{file}", 'rb'), reply_markup=btn.markup)
    os.remove(file)



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)