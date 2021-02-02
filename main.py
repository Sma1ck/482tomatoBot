from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from aiogram.bot import api
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()  # создание локального хранилища данных
dp = Dispatcher(bot, storage=storage)


# Обход блокировки телеграмма
PATCHED_URL = "https://telegg.ru/orig/bot{token}/{method}"
setattr(api, 'API_URL', PATCHED_URL)


def main():
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)


if __name__ == '__main__':
    main()