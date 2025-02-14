from aiogram import html, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from app.main import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/start` command
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="English"), KeyboardButton(text="Русский")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await message.answer(
        f"""
        Привет! {html.bold(message.from_user.full_name)}! Я Сомнобот, помогу тебе следить за сном.
        Выбери, пожалуйста, язык:
        Hello, {html.bold(message.from_user.full_name)}! I'm Somnobot - sleep monitoring diary.
        Please, choose start:
        """,
        reply_markup=keyboard,
    )
    await state.set_state("choose_language")


@dp.message(F.text.in_({"English", "Русский"}), state="choose_language")
async def save_language_choice(message: Message, state: FSMContext) -> None:
    """
    Save the user's start choice in the environment
    """
    language = message.text
    tg_user_id = message.from_user.id

    if language == "English":
        response = "Thank you! Your start has been set to English."
    else:
        response = "Спасибо! Ваш язык установлен на Русский."

    await message.answer(response)
    await state.clear()
