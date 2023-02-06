import datetime

import telebot

from evenWeek import even_week_list
from oddWeek import odd_week_list
from util import today_schedule, tomorrow_schedule

# odd - нечетная неделя
# even - четная неделя

access_token = "5879036251:AAGRYqxsKkxkd3OeH3Uc0B_LR_dx-kio4ME"
bot = telebot.TeleBot(access_token)
list_of_commands = """
/з - расписание на завтра
/с - расписание на сегодня
/облако - ссылка на облако
"""
link = """
Ссылка на онлайн расписание с портала
https://portal.omgups.ru/extranet/raspisanie/semester2_2022-2023/raspisanie_iatit/42.htm\n
"""

is_odd_week = datetime.datetime.utcnow().isocalendar()[1] % 2 == 0
what_week_text = "Неделя: "

if is_odd_week:
    what_week_text += "четная\n"
else:
    what_week_text += "не четная\n"


def get_day_of_week():
    return datetime.datetime.today().weekday()


week_day = get_day_of_week()


def get_schedule(offset):
    if week_day % 2 == 0:
        return even_week_list[week_day + offset]
    else:
        return odd_week_list[week_day + offset]


@bot.message_handler(commands=['з'])
def send_message(message):
    bot.send_message(message.chat.id, what_week_text + link + tomorrow_schedule + get_schedule(1))


@bot.message_handler(commands=['с'])
def send_message(message):
    bot.send_message(message.chat.id, what_week_text + link + today_schedule + get_schedule(0))


@bot.message_handler(commands=['облако'])
def send_message(message):
    bot.send_message(message.chat.id, "https://disk.yandex.ru/client/disk/ОМГУПС/2%20курс")


@bot.message_handler(commands=['команды'])
def send_message(message):
    bot.send_message(message.chat.id, list_of_commands)


if __name__ == '__main__':
    bot.polling(none_stop=True)
