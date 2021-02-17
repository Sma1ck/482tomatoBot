from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "1675007273:AAGS72uqpndNHI-HC4q6jFLZNX_fjiOoM5U"
admin_id = 304529214

# Основное меню, которые выводится на старте
global_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Расписание на сегодня"),
                KeyboardButton(text='Расписание на завтра'),
            ],
            [
                KeyboardButton(text="Расписание на неделю"),
            ],
            [
                KeyboardButton(text='Расписание на следующую неделю'),
            ],
            [
                KeyboardButton(text='Zoom ссылки'),
                KeyboardButton(text='Почты преподавателей')
            ],
            [
                KeyboardButton(text='Полезные ссылки'),
                KeyboardButton(text='Данные от сервисов'),
            ],
        ],
        resize_keyboard=True
    )
# Расписание на четную неделю
schedule_even = {
    1: ['<b>10:00 - 11:40:</b> ПРОЦЕССЫ И АППАРАТЫ - ПРАКТИКА АУД. КАФЕДРЫ БОРИСОВА Е.И.',
        '<b>12:00 - 13:40: </b>ТЕОРИЯ АВТОМАТИЧЕСКОГО УПРАВЛЕНИЯ - ЛАБОРАТОРНАЯ АУД. КАФЕДРЫ',
        '<b>14:30 - 16:10: </b>АВТОМАТИЗАЦИЯ ТЕХНОЛОГИЧЕСКИХ ПРОЦЕССОВ И ПРОИЗВОДСТВ - ЛАБОРАТОРНАЯ, ПРАКТИКА АУД. КАФЕДРЫ В.В. КУРКИНА',
        '<b>16:30 - 18:10: </b>АВТОМАТИЗАЦИЯ ТЕХНОЛОГИЧЕСКИХ ПРОЦЕССОВ И ПРОИЗВОДСТВ - ЛАБОРАТОРНАЯ, ПРАКТИКА АУД. КАФЕДРЫ В.В. КУРКИНА'
        ],
    2: ['<b>10:00 - 11:40: </b>ФИЗИЧЕСКАЯ КУЛЬТУРА И СПОРТ',
        '<b>12:00 - 13:40: </b>ТЕОРИЯ АВТОМАТИЧЕСКОГО УПРАВЛЕНИЯ - ЛЕКЦИЯ АУД. 394 ФОКИН А.Л.',
        '<b>14:30 - 16:10: </b>ТЕХНОЛОГИЧЕСКИЕ ИЗМЕРЕНИЯ И ПРИБОРЫ - ЛАБОРАТОРНАЯ, ПРАКТИКА НОВИКОВ Л.В.',
        '<b>16:30 - 18:10: </b>ТЕХНОЛОГИЧЕСКИЕ ИЗМЕРЕНИЯ И ПРИБОРЫ - ЛАБОРАТОРНАЯ, ПРАКТИКА НОВИКОВ Л.В.'
        ],
    3: ['<b>10:00 - 11:40: </b>ДИАГНОСТИКА И НАДЕЖНОСТЬ АВТОМАТИЗИРОВАННЫХ СИСТЕМ - ЛЕКЦИЯ АУД. 309 РУДАКОВА И.В.',
        '<b>12:00 - 13:40: </b>ДИАГНОСТИКА И НАДЕЖНОСТЬ АВТОМАТИЗИРОВАННЫХ СИСТЕМ - ПРАКТИКА АУД. 309 РУДАКОВА И.В.',
        '<b>14:30 - 16:10: </b>АВТОМАТИЗАЦИЯ ТЕХНОЛОГИЧЕСКИХ ПРОЦЕССОВ И ПРОИЗВОДСТВ - ЛЕКЦИЯ АУД. КАФЕДРЫ РЕМИЗОВА О.А.',
        '<b>16:30 - 18:10: </b>СРЕДСТВА АВТОМАТИЗАЦИИ И УПРАВЛЕНИЯ - ЛЕКЦИЯ, ЛАБОРАТОРНАЯ КАФЕДРА АПХП СЯГАЕВ Н.А. НОВИЧКОВ Ю.А.'],
    4: ['<b>10:00 - 11:40: </b>СОЦИОЛОГИЯ - ЛЕКЦИЯ АУД. 394 ЕЖОВ С.П.',
        '<b>12:00 - 13:40: </b>СОЦИОЛОГИЯ - ПРАКТИКА АУД. 255 ДРУЖИНИНА Ю.В.'
        ],
    5: ['<b>10:00 - 11:40: </b>ФИЗИЧЕСКАЯ КУЛЬТУРА И СПОРТ',
        '<b>12:00 - 13:40: </b>ПРОГРАММНО-ТЕХНИЧЕСКИЕ КОМПЛЕКСЫ ОБРАБОТКИ ИНФОРМАЦИИ И УПРАВЛЕНИЯ КАЧЕСТВОМ ПРОДУКЦИИ - ЛЕКЦИЯ, ПРАКТИКА АУД. САПРиУ КОРНИЕНКО И.Г. ФЕДИН А.К.',
        ],
}
# Расписание на нечетную неделю
schedule_odd = {
    1: ['<b>10:00 - 11:40: </b>ПРОЦЕССЫ И АППАРАТЫ - ПРАКТИКА АУД. КАФЕДРЫ БОРИСОВА Е.И.',
        '<b>12:00 - 13:40: </b>ТЕОРИЯ АВТОМАТИЧЕСКОГО УПРАВЛЕНИЯ - ЛАБОРАТОРНАЯ АУД. КАФЕДРЫ',
        ],
    2: ['<b>10:00 - 11:40: </b>ФИЗИЧЕСКАЯ КУЛЬТУРА И СПОРТ',
        '<b>12:00 - 13:40: </b>ТЕОРИЯ АВТОМАТИЧЕСКОГО УПРАВЛЕНИЯ - ЛЕКЦИЯ АУД. 394 ФОКИН А.Л.',
        '<b>14:30 - 16:10: </b>ПРОЦЕССЫ И АППАРАТЫ - ЛАБОРАТОРНАЯ АУД. ПРиАПП БОРИСОВА Е.И.',
        '<b>16:30 - 18:10: </b>ПРОЦЕССЫ И АППАРАТЫ - ЛАБОРАТОРНАЯ АУД. ПРиАПП БОРИСОВА Е.И.'
        ],
    3: ['<b>10:00 - 11:40: </b>ДИАГНОСТИКА И НАДЕЖНОСТЬ АВТОМАТИЗИРОВАННЫХ СИСТЕМ - ЛЕКЦИЯ АУД. 309 РУДАКОВА И.В.',
        '<b>12:00 - 13:40: </b>ДИАГНОСТИКА И НАДЕЖНОСТЬ АВТОМАТИЗИРОВАННЫХ СИСТЕМ - ПРАКТИКА АУД. 309 РУДАКОВА И.В.',
        '<b>14:30 - 16:10: </b>АВТОМАТИЗАЦИЯ ТЕХНОЛОГИЧЕСКИХ ПРОЦЕССОВ И ПРОИЗВОДСТВ - ЛЕКЦИЯ АУД. КАФЕДРЫ РЕМИЗОВА О.А.',
        '<b>16:30 - 18:10: </b>СРЕДСТВА АВТОМАТИЗАЦИИ И УПРАВЛЕНИЯ - ЛЕКЦИЯ, ЛАБОРАТОРНАЯ КАФЕДРА АПХП СЯГАЕВ Н.А. НОВИЧКОВ Ю.А.'
        ],
    4: ['<b>10:00 - 11:40: </b>ПРОЦЕССЫ И АППАРАТЫ - ЛЕКЦИЯ АУД. 290 БОРИСОВА Е.И.',
        '<b>12:00 - 13:40: </b>СОЦИОЛОГИЯ - ПРАКТИКА АУД. 255 ДРУЖИНИНА Ю.В.'
        ],
    5: ['<b>10:00 - 11:40: </b>ТЕХНОЛОГИЧЕСКИЕ ИЗМЕРЕНИЯ И ПРИБОРЫ - ЛЕКЦИЯ АУД. КАФЕДРЫ НОВИКОВ Л.В.',
        '<b>12:00 - 13:40: </b>ПРОГРАММНО-ТЕХНИЧЕСКИЕ КОМПЛЕКСЫ ОБРАБОТКИ ИНФОРМАЦИИ И УПРАВЛЕНИЯ КАЧЕСТВОМ ПРОДУКЦИИ - ЛЕКЦИЯ, ПРАКТИКА АУД. САПРиУ КОРНИЕНКО И.Г. ФЕДИН А.К.',
        ],
}


# Просто названия дней недели
weekdays_iteration = {
    1: 'ПОНЕДЕЛЬНИК',
    2: 'ВТОРНИК',
    3: 'СРЕДА',
    4: 'ЧЕТВЕРГ',
    5: 'ПЯТНИЦА',
}

# Клавиатура для полезных ссылок
links_keyboard = InlineKeyboardMarkup(row_width=2)
media_btn = InlineKeyboardButton('Медиачат', url='https://media.technolog.edu.ru/index.php?lang=ru')
moodle_btn = InlineKeyboardButton('Мудл', url='http://moodle.technolog.edu.ru/')
google_drive481_btn = InlineKeyboardButton('Гугл диск 482', url='https://drive.google.com/drive/u/2/my-drive')
google_drive481_482_btn = InlineKeyboardButton('Гугл диск 481-482', url='https://drive.google.com/drive/folders/1ekq_IUs32KSZ9hO5nKxwPU-p7Wh0WYMx')
sociology_drive_btn = InlineKeyboardButton('Облако социология', url='https://cloud.mail.ru/public/9fzv/Jeuri1J2Q/')
gmail_btn = InlineKeyboardButton('Гугл почта', url='https://mail.google.com/mail/u/2/?tab=om#inbox')
links_keyboard.row(media_btn, moodle_btn)
links_keyboard.row(google_drive481_btn, gmail_btn)
links_keyboard.row(google_drive481_482_btn, sociology_drive_btn)

# Клавиатура для данных от почты
mail_info_keyboard = InlineKeyboardMarkup()
gmail_info_btn = InlineKeyboardButton('Гугл почта', callback_data='btn_gmail_info')
mailru_info_btn = InlineKeyboardButton('Меил.ру', callback_data='btn_mailru_info')
mail_info_keyboard.add(gmail_info_btn, mailru_info_btn)

# Клавиатура для почт преподавателей
teachers_mails_keyboard = InlineKeyboardMarkup()
fokin_btn = InlineKeyboardButton('Фокин Александр Леонидович(ТАУ)', callback_data='btn_fokin')
kurkina_btn = InlineKeyboardButton('Куркина Виктория Вадимовна', callback_data='btn_kurkina')
csharp_btn = InlineKeyboardButton('C#', callback_data='btn_C#')
borisova_btn = InlineKeyboardButton('Борисова Екатерина Игоревна', callback_data='btn_borisova')
sociology_btn = InlineKeyboardButton('Социология', callback_data='btn_sociology')
teachers_mails_keyboard.add(fokin_btn)
teachers_mails_keyboard.add(kurkina_btn)
teachers_mails_keyboard.add(csharp_btn)
teachers_mails_keyboard.add(borisova_btn)
teachers_mails_keyboard.add(sociology_btn)


zoom_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text='Кафедра АПХП')
        ],
        [
          KeyboardButton(text='Назад')
        ],
    ],
    resize_keyboard=True
)
