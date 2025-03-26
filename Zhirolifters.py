import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from shared.config import TELEGRAM_BOT_TOKEN

# Загружаем переменные окружения
load_dotenv()
TOKEN = TELEGRAM_BOT_TOKEN
if not TOKEN:
    raise ValueError("TOKEN не найден! Проверь .env файл")

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Создание бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главная клавиатура
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❓ Помощь")],
        [KeyboardButton(text="Купить план тренировок🎁")]
    ],
    resize_keyboard=True
)

# Клавиатура для выбора программы
buy_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Программа на массу 💪")],
        [KeyboardButton(text="Подробная программа питания🥬")],
        [KeyboardButton(text="Программа на рельеф 🔥")],
        [KeyboardButton(text="Функциональный тренинг 🏃")],
        [KeyboardButton(text="⬅️ Назад в меню")]
    ],
    resize_keyboard=True
)

# Клавиатура с прайсом и оплатой
payment_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ Назад к программам")]
    ],
    resize_keyboard=True
)

# Установка команд
async def set_bot_commands():
    commands = [
        types.BotCommand(command="start", description="Запустить бота 🔍"),
        types.BotCommand(command="help", description="Помощь 🚑"),
        types.BotCommand(command="buy", description="Программы тренировок🏆"),
    ]
    await bot.set_my_commands(commands)

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я твой фитнес-бот. Чем могу помочь?", reply_markup=main_keyboard)

# Обработчик команды /help и кнопки "Помощь"
@dp.message(Command("help"))
@dp.message(lambda message: message.text == "❓ Помощь")
async def help_handler(message: types.Message):
    await message.answer("Если у тебя есть вопросы, пиши мне в Telegram: [@Guts_berserk_griffith](https://t.me/Guts_berserk_griffith)", parse_mode="Markdown", reply_markup=main_keyboard)

# Обработчик кнопки "Купить план тренировок"
@dp.message(Command("buy"))
@dp.message(lambda message: message.text == "Купить план тренировок🎁")
async def buy_handler(message: types.Message):
    await message.answer("Выберите тип тренировочной программы:", reply_markup=buy_keyboard)

# Обработчик выбора программы
@dp.message()
async def message_handler(message: types.Message):
    if message.text == "Советы по тренировкам🥊":
        await message.answer("Отдых между подходами должен быть 3 минуты!")
        await message.answer("Если не понимаешь правильную технику, то лучше подойди к людям из зала!")
        await message.answer("Если ты хочешь добиться больших целей, то советую купить программу тренировок!")

    elif message.text == "Программа на массу 💪":
        await message.answer("🔥 Программа на массу:\n💵 Цена: 7 000 тенге.\n\nДля покупки свяжитесь со мной: [@Guts_berserk_griffith](https://t.me/Guts_berserk_griffith)", parse_mode="Markdown", reply_markup=payment_keyboard)

    elif message.text == "Программа на рельеф 🔥":
        await message.answer("🔥 Программа на рельеф:\n💵 Цена: 7 000 тенге.\n\nДля покупки свяжитесь со мной: [@Guts_berserk_griffith](https://t.me/Guts_berserk_griffith)", parse_mode="Markdown", reply_markup=payment_keyboard)

    elif message.text == "Подробная программа питания🥬":
        await message.answer("Подробная программа питания🥬:\n💵 Цена: 12 000 тенге.\n\nДля покупки свяжитесь со мной: [@Guts_berserk_griffith](https://t.me/Guts_berserk_griffith)", parse_mode="Markdown", reply_markup=payment_keyboard)

    elif message.text == "Функциональный тренинг 🏃":
        await message.answer("🔥 Функциональный тренинг:\n💵 Цена: 10 000 тенге.\n\nДля покупки свяжитесь со мной: [@Guts_berserk_griffith](https://t.me/Guts_berserk_griffith)", parse_mode="Markdown", reply_markup=payment_keyboard)

    elif message.text == "⬅️ Назад к программам":
        await message.answer("Выберите программу:", reply_markup=buy_keyboard)

    elif message.text == "⬅️ Назад в меню":
        await message.answer("Возвращаюсь в главное меню", reply_markup=main_keyboard)

    elif message.text.lower() == "спасибо":
        await message.answer("Не за что, обращайся! 😊")

    else:
        await message.answer("Я не понимаю эту команду. Попробуй /help.")

# Основная функция
async def main():
    await set_bot_commands()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())