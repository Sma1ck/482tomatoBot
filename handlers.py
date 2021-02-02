from main import bot, dp
from aiogram import types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from config import admin_id, global_menu


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler(commands=['start'])
async def greeting(message: Message):
    text = ' Введи команду /help чтобы узнать,шо вообще тут можно сделать'
    await message.answer(text=text)


@dp.message_handler(commands=['help'])
async def show_commands(message: Message):
    text = "Ничего нельзя тут делать."
    await message.answer(text=text, reply_markup=global_menu)

@dp.message_handler(text='Расписание на сегодня')
async def show_today_schedule(message: Message):
    from config import schedule_even, schedule_odd
    from datetime import datetime
    week_count = datetime.now().isocalendar()[1]
    today = datetime.isoweekday(datetime.now())
    # нечетная неделя
    if week_count % 2 == 0:
        for weekday, classes in schedule_odd.items():
            if weekday == today:
                today_schedule = '\n'.join(classes)
            if today == 6 or today == 7:
                today_schedule = 'Сегодня выходной'
                break
    # четная неделя
    if week_count % 2 != 0:
        for weekday, classes in schedule_even.items():
            if weekday == today:
                today_schedule = '\n'.join(classes)
            if today == 6 or today == 7:
                today_schedule = 'Сегодня выходной'
                break
    await message.answer(text=today_schedule)


@dp.message_handler(text='Расписание на неделю')
async def show_week_schedule(message: Message):
    from config import schedule_even, schedule_odd, weekdays_iteration
    from datetime import datetime
    week_count = datetime.now().isocalendar()[1]
    week_schedule = []
    if week_count % 2 == 0:
        for weekday, classes in schedule_odd.items():
            for weekday_number, weekday_name in weekdays_iteration.items():
                if weekday == weekday_number:
                    weekday = weekday_name
            week_schedule_for_day = weekday + ':' + '\n' + '\n'.join(classes)
            week_schedule.append(week_schedule_for_day)
    if week_count % 2 != 0:
        for weekday, classes in schedule_even.items():
            for weekday_number, weekday_name in weekdays_iteration.items():
                if weekday == weekday_number:
                    weekday = weekday_name
            week_schedule_for_day = weekday + ':' + '\n' + '\n'.join(classes)
            week_schedule.append(week_schedule_for_day)
    text = '\n'.join(week_schedule)
    await message.answer(text=text)