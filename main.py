import asyncio

from aiogram import F, Bot, Dispatcher, Router
from aiogram.types import Message, BotCommand, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

bot = Bot(token="7086038652:AAEKbcrL_Mod-9KNUf2jZGNBE_ZYj7ti0jg")
dp = Dispatcher()

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='help', description='Справка'),
        BotCommand(command='delete', description='Отчислиться'),
    ])
    
    markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Привет! Я бот, который напомнит тебе, какой сегодня праздник!')]])

    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперед', callback_data='next')]
    ])
    await msg.answer(text='Страница 1', reply_markup=inline_markup)

    @router.callback_query(F.data == 'next')
    async def next_handler(callback_query: CallbackQuery):
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='back')]
        ])
        await callback_query.message.delete()
        await callback_query.message.answer(
            text='страница 2',
            reply_markup=inline_markup)
        
@router.callback_query(F.data == 'back')
async def next_handler(callback_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперед', callback_data='next')]
    ])
    await callback_query
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Установить время', callback_data='1'),
            InlineKeyboardButton(text='Узнать праздник',callback_data='2')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='3')
        ]
    ])
    await msg.answer(text='Привет', reply_markup=inline_markup)


@router.callback_query(F.data == '1')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text='Выберете часовой пояс:')
    markup_for_time = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Выберете часовой пояс:')]])

    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='МСК', callback_data='1'),
        ],
        [
            InlineKeyboardButton(text='МСК+2',callback_data='2')
        ],
        [
            InlineKeyboardButton(text='МСК+3', callback_data='3'),
        ],
        [
            InlineKeyboardButton(text='МСК+4', callback_data='4'),
        ],
        [
            InlineKeyboardButton(text='МСК+5', callback_data='5'),
        ],
        [
            InlineKeyboardButton(text='МСК+6', callback_data='6'),
        ],
        [
            InlineKeyboardButton(text='МСК+7', callback_data='7'),
        ],
        [
            InlineKeyboardButton(text='МСК+8', callback_data='8'),
        ],
        [
            InlineKeyboardButton(text='МСК+9', callback_data='9'),
        ],
        [
            InlineKeyboardButton(text='МСК+10', callback_data='10'),
        ],
        [
            InlineKeyboardButton(text='МСК+11', callback_data='11'),
        ],
        
    ])
    await callback_query.answer(text='Выберете часовой пояс:', reply_markup=inline_markup)


@router.callback_query(F.data == '2')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text='Нету')

@router.callback_query(F.data == '3')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer(text='Пока')

async def main():
    await dp.start_polling(bot)

dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())