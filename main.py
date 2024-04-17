import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command 

bot = Bot(token="7086038652:AAEKbcrL_Mod-9KNUf2jZGNBE_ZYj7ti0jg")
dp = Dispatcher()

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text="123")

async def main():
    await dp.start_polling(bot)

dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())