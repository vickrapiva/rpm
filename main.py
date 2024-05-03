import asyncio

from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import Message


# Замените этот токен на свой токен бота
TOKEN = '7086038652:AAEKbcrL_Mod-9KNUf2jZGNBE_ZYj7ti0jg'

# Создание бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def start_bot(bot: Bot):
    await bot.send_message(1324023825, text="Бот запущен!")

async def stop_bot(bot: Bot):
    await bot.send_message(1324023825, text='Бот остановлен!')

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет{message.from_user.first_name}. С помощью этого бота ты не забудешь, какой сегодня праздник!!!')
    await message.answer(f'Привет{message.from_user.first_name}. С помощью этого бота ты не забудешь, какой сегодня праздник!!!')
    await message.reply(f'Привет{message.from_user.first_name}. С помощью этого бота ты не забудешь, какой сегодня праздник!!!')
    
dp.message.register(get_start)

