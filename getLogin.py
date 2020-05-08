from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math
import random

logging_succes = False
USERNAME = ''
PASSWORD = ''
ARR_ID_COURSE = ['13509', '14498', '14643', '14506', '14425', '14534']
#               1-Иностранный язык
#                        2-Сети ЭВМ и телекоммуникации
#                                 3-Предметно-ориентированное программирование
#                                          4-Философия
#                                                   5-Программирование на Java
#                                                            6-Математическая логика и теория алгоритмов
#
#

URL_TO_COURSE = 'https://edu.vvsu.ru/course/view.php?id='
url_to_course = URL_TO_COURSE

localtime = time.localtime(time.time())


browser = webdriver.Firefox()
browser.get('http://edu.vvsu.ru')
assert "СЭО ВГУЭС" in browser.title


def log_in(username, password):
    username_elem = browser.find_element_by_name('username')
    print("Enter your username")
    username = input()
    USERNAME = username
    username_elem.send_keys(username)

    password_elem = browser.find_element_by_name('password')
    print("Enter your password")
    password = input()
    PASSWORD = password
    password_elem.send_keys(password + Keys.RETURN)
    password = None
    PASSWORD = None
    time.sleep(8)
    print(browser.current_url)
    return True

def select_course(var):
    print(url_to_course, ARR_ID_COURSE[int(var)-1])
    browser.get(url_to_course + ARR_ID_COURSE[int(var)-1])
    time.sleep(10)


if browser.find_element_by_name('btnlogin'):
    chk_btnlogin = True

logging_succes = log_in(USERNAME, PASSWORD)

def getCurWeekday():
    times = time.localtime(time.time())
    curweek = times.tm_wday
    return curweek

def getCurTimeLesson():
    times = time.localtime(time.time())
    curHour = times.tm_hour
    curMinute = times.tm_min
    curLesson = 0
    if curHour == 8 and curMinute >= 30 or curHour == 9:
        curLesson = 0
        print("Now lesson - ", (curLesson+1))
        return curLesson
    if curHour == 10 and curMinute >= 5 or curHour == 11 and curMinute <= 40:
        curLesson = 1
        print("Now lesson - ", (curLesson + 1))
        return curLesson
    if curHour == 11 and curMinute >= 45 or curHour == 12 or curHour == 13 and curMinute <=20:
        curLesson = 2
        print("Now lesson - ", (curLesson + 1))
        return curLesson
    if curHour == 13 and curMinute >= 25 or curHour == 14 or curHour == 15 and curMinute <= 3:
        curLesson = 3
        print("Now lesson - ", (curLesson + 1))
        return curLesson
    if curHour == 15 and curMinute >= 5 or curHour == 16 and curMinute <= 40:
        curLesson = 4
        print("Now lesson - ", (curLesson + 1))
        return curLesson
    if curHour == 16 and curMinute >= 45 or curHour == 17 or curHour == 18 and curMinute <= 20:
        curLesson = 5
        print("Now lesson - ", (curLesson + 1))
        return curLesson


def getCurrentCourse():
    curWeekday = getCurWeekday()
    curLesson = getCurTimeLesson()
    curWeekday = 0
    curLesson = 2
    if curWeekday == 0:
        if curLesson == 0:
            print()
        if curLesson == 1:
            print()
        if curLesson == 2:

            print()
            return 2
        if curLesson == 3:
            print()
        if curLesson == 4:
            print()
            return 4
        if curLesson == 5:
            print()

    if curWeekday == 1:
        if curLesson == 0:
            print()
        if curLesson == 1:
            print()
            return 5
        if curLesson == 2:
            print()
            return 5
        if curLesson == 3:
            print()
        if curLesson == 4:
            print()
        if curLesson == 5:
            print()

    if curWeekday == 2:
        if curLesson == 0:
            print()
        if curLesson == 1:
            print()
        if curLesson == 2:
            print()
            return 0
        if curLesson == 3:
            print()
        if curLesson == 4:
            print()
        if curLesson == 5:
            print()

    if curWeekday == 3:
        if curLesson == 0:
            print()
        if curLesson == 1:
            print()
        if curLesson == 2:
            print()
            return 3
        if curLesson == 3:
            print()
        if curLesson == 4:
            print()
            return 2
        if curLesson == 5:
            print()

    if curWeekday == 4:
        if curLesson == 0:
            print()
        if curLesson == 1:
            print()
        if curLesson == 2:
            print()
            return 3
        if curLesson == 3:
            print()
            return 1
        if curLesson == 4:
            print()
            return 0
        if curLesson == 5:
            print()

    if curWeekday == 5:
        if curLesson == 0:
            print()
        if curLesson == 1:
            print()
        if curLesson == 2:
            print()
            return 1
        if curLesson == 3:
            print()
            return 4
        if curLesson == 4:
            print()
        if curLesson == 5:
            print()


what_course = 0

what_course = getCurrentCourse()

if logging_succes:

    print("Logging succes, now we're studying on:", (what_course))
    #what_course = input()
    time.sleep(2)
    if what_course != 0:
        select_course(what_course+1)
print("Your chose: ", what_course)

while True:
    sleep_time = 180 + (random.random()*360)
    time.sleep(360)
    print("Refreshing...")
    browser.refresh()


