from main import bot, dp
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, callback_query
from config import admin_id, global_menu


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler(commands=['start'])
async def greeting(message: Message):
    text = ' Введи команду /help чтобы узнать,шо вообще тут можно сделать'
    await message.answer(text=text)


@dp.message_handler(commands=['help'])
async def show_commands(message: Message):
    text = "Здесь можно посмотреть расписание на один день или на неделю, найти ссылки на необходимые сервисы и узнать данные от почты"
    await message.answer(text=text, reply_markup=global_menu)

@dp.message_handler(text='Расписание на сегодня')
async def show_today_schedule(message: Message):
    '''
    Возвращает расписание на один день(сегодня)
    :param message:
    :return:
    '''
    from config import schedule_even, schedule_odd
    from datetime import datetime
    week_count = datetime.now().isocalendar()[1]
    today = datetime.isoweekday(datetime.now())
    # четная неделя
    if week_count % 2 == 0:
        for weekday, classes in schedule_even.items():
            if weekday == today:
                today_schedule = '\n'.join(classes)
            if today == 6 or today == 7:
                today_schedule = 'Сегодня выходной'
                break
    # нечетная неделя
    if week_count % 2 != 0:
        for weekday, classes in schedule_odd.items():
            if weekday == today:
                today_schedule = '\n'.join(classes)
            if today == 6 or today == 7:
                today_schedule = 'Сегодня выходной'
                break
    await message.answer(text=today_schedule)


@dp.message_handler(text='Расписание на завтра')
async def show_tomorrow_schedule(message: Message):
    '''
    Вывод расписания на следующую неделю
    :param message:
    :return:
    '''
    from config import schedule_even, schedule_odd
    from datetime import datetime
    week_count = datetime.now().isocalendar()[1]
    tomorrow = datetime.isoweekday(datetime.now()) + 1
    if tomorrow == 8:
        tomorrow = 1
    # четная неделя
    if week_count % 2 == 0:
        for weekday, classes in schedule_even.items():
            if weekday == tomorrow:
                tomorrow_schedule = '\n'.join(classes).lower()
            if tomorrow == 6 or tomorrow == 7:
                tomorrow_schedule = 'Завтра выходной'
                break
    # нечетная неделя
    if week_count % 2 != 0:
        for weekday, classes in schedule_odd.items():
            if weekday == tomorrow:
                tomorrow_schedule = '\n'.join(classes).lower()
            if tomorrow == 6 or tomorrow == 7:
                tomorrow_schedule = 'Завтра выходной'
                break
    await message.answer(text=tomorrow_schedule)


@dp.message_handler(text='Расписание на неделю')
async def show_week_schedule(message: Message):
    '''
    Возвращает расписание на всю неделю
    :param message:
    :return:
    '''
    from config import schedule_even, schedule_odd, weekdays_iteration
    from datetime import datetime
    week_count = datetime.now().isocalendar()[1]
    week_schedule = []
    # четная неделя
    if week_count % 2 == 0:
        for weekday, classes in schedule_even.items():
            for weekday_number, weekday_name in weekdays_iteration.items():
                if weekday == weekday_number:
                    weekday = weekday_name
            week_schedule_for_day = weekday + ':' + '\n' + '\n'.join(classes).lower()
            week_schedule.append(week_schedule_for_day)
    # Нечетная неделя
    if week_count % 2 != 0:
        for weekday, classes in schedule_odd.items():
            for weekday_number, weekday_name in weekdays_iteration.items():
                if weekday == weekday_number:
                    weekday = weekday_name
            week_schedule_for_day = weekday + ':' + '\n' + '\n'.join(classes).lower()
            week_schedule.append(week_schedule_for_day)
    text = '\n'.join(week_schedule)
    await message.answer(text=text)


@dp.message_handler(text='Расписание на следующую неделю')
async def show_week_schedule(message: Message):
    '''
    Возвращает расписание на всю следующую неделю
    :param message:
    :return:
    '''
    from config import schedule_even, schedule_odd, weekdays_iteration
    from datetime import datetime
    week_count = datetime.now().isocalendar()[1] + 1
    week_schedule = []
    # четная неделя
    if week_count % 2 == 0:
        for weekday, classes in schedule_even.items():
            for weekday_number, weekday_name in weekdays_iteration.items():
                if weekday == weekday_number:
                    weekday = weekday_name
            week_schedule_for_day = weekday + ':' + '\n' + '\n'.join(classes).lower()
            week_schedule.append(week_schedule_for_day)
    # нечетная неделя
    if week_count % 2 != 0:
        for weekday, classes in schedule_odd.items():
            for weekday_number, weekday_name in weekdays_iteration.items():
                if weekday == weekday_number:
                    weekday = weekday_name
            week_schedule_for_day = weekday + ':' + '\n' + '\n'.join(classes).lower()
            week_schedule.append(week_schedule_for_day)
    text = '\n'.join(week_schedule)
    await message.answer(text=text)



@dp.message_handler(text='Полезные ссылки')
async def show_useful_links(message: Message):
    '''
    Дает ссылки на самые важные сайты или полезные для учебы сайты
    :param message:
    :return:
    '''
    from config import links_keyboard
    text = 'Выбери необходимый сервис:'
    await message.answer(text=text, reply_markup=links_keyboard)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: callback_query):
    '''
    Ловим колбэки от кнопок и выводим информацию
    :param callback_query:
    :return:
    '''
    code = callback_query.data[4:]
    if code == 'gmail_info':
        # await bot.answer_callback_query(callback_query.id, text='mail password')
        await bot.send_message(callback_query.from_user.id, 'login: 482groupp@gmail.com \npassword: 999999999group')
    if code == 'mailru_info':
        await bot.send_message(callback_query.from_user.id, 'login: 482group@mail.ru \npassword: 999999999group')


@dp.message_handler(text='Данные от сервисов')
async def show_mail_info(message: Message):
    '''
    Вывод кнопок для данных от почт
    :param message:
    :return:
    '''
    from config import mail_info_keyboard
    text = 'Выбери почту, от которой нужны данные:'
    await message.answer(text=text, reply_markup=mail_info_keyboard)