from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

BOT_TOKEN = "1675007273:AAGS72uqpndNHI-HC4q6jFLZNX_fjiOoM5U"
admin_id = 304529214

global_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Расписание на сегодня"),
            ],
            [
                KeyboardButton(text="Расписание на неделю")
            ],
        ],
        resize_keyboard=True
    )

schedule_even = {
    1: ['пара1', 'пара2', 'пара3'],
    2: ['пара1', 'пара2', 'пара3'],
    3: ['пара1', 'пара2', 'пара3'],
    4: ['пара1', 'пара2', 'пара3'],
    5: ['пара1', 'пара2', 'пара3'],
}

schedule_odd = {
    1: ['пара1', 'пара2', 'пара3'],
    2: ['пара1', 'пара2', 'пара3'],
    3: ['пара1', 'пара2', 'пара3'],
    4: ['пара1', 'пара2', 'пара3'],
    5: ['пара1', 'пара2', 'пара3'],
}

weekdays_iteration = {
    1: 'Понедельник',
    2: 'Вторник',
    3: 'Среда',
    4: 'Четверг',
    5: 'Пятница',
}