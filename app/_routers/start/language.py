from aiogram import html, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from app.utils.enums import BotLanguage

start_router = Router()


class UserState(StatesGroup):
    choose_language = State()


@start_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
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
    await state.set_state(UserState.choose_language)


@start_router.message(F.text.in_({"English", "Русский"}), UserState.choose_language)
async def save_language_choice(message: Message, state: FSMContext) -> None:
    language = message.text

    # TODO save to user
    tg_user_id = message.from_user.id

    if language == BotLanguage.en:
        response = "Thank you! Your start has been set to English."
    elif language == BotLanguage.ru:
        response = "Спасибо! Ваш язык установлен на Русский."
    else:
        response = "..."

    await message.answer(response)
    await state.clear()
