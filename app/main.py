import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


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
        Please, choose language:
        """,
        reply_markup=keyboard,
    )
    await state.set_state("choose_language")


@dp.message(F.text.in_({"English", "Русский"}), state="choose_language")
async def save_language_choice(message: Message, state: FSMContext) -> None:
    """
    Save the user's language choice in the environment
    """
    language = message.text
    tg_user_id = message.from_user.id

    if language == "English":
        response = "Thank you! Your language has been set to English."
    else:
        response = "Спасибо! Ваш язык установлен на Русский."

    await message.answer(response)
    await state.clear()


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
