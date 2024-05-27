from aiogram import Router, F 
from aiogram.filters import Command 
from aiogram.types import Message, CallbackQuery 
from aiogram.fsm.context import FSMContext 
from states.anketa import Anketa 
from keyboards.anketa import *


router = Router()

@router.message(Command("anketa"))
async def anketa_handler(msg: Message, state: FSMContext):
    await state.set_state(Anketa.name)
    await msg.answer('Введите ваше имя', reply_markup=kb_apteka_cancel)


@router.callback_query(F.data == 'cancel_apteka')
async def cancel_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.answer('Регистрация отменена')

@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    await state.update_data(name = str(msg.text))
    await state.set_state(Anketa.age) 
    await msg.answer( 
        "Введите Ваш возраст", reply_markup=kb_apteka_cancel_and_back)
    
@router.callback_query(F.data == "back_anketa")
async def back_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == Anketa.gender: 
        await state.set_state(Anketa.age) 
        await callback_query.message.answer( 
            "Введите Ваш возраст", reply_markup=kb_apteka_cancel_and_back)
    
    elif current_state == Anketa.age:
        await state.set_state(Anketa.name) 
        await callback_query.message.answer( 
            "Введите Ваше имя", reply_markup=kb_apteka_cancel)
 
@router.message(Anketa.age)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer('Вы не верно ввели возраст!')
        await msg.answer(
            'Введите Ваш возраст', reply_markup=kb_apteka_cancel_and_back)
        return
    await state.set_state(Anketa.gender)
    await msg.answer(
        'Введите ваш пол', reply_markup=kb_apteka_by_gender)
    
@router.callback_query(F.data.startswith('gender_') and Anketa.gender)
async def set_gender_anketa_handler(callback_query: CallbackQuery, state: FSMContext): 
    gender = {'gender_m': 'Мужской','gender_w':'Женский'}[callback_query.data]
    await state.update_data(gender=gender)
    await callback_query.message.answer(str(await state.get_data()))
    await state.clear()


@router.message(Anketa.gender)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext): 
    await msg.answer('Нужно выбрать пол кнопкой!')