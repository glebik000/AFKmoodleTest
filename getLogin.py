from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


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

what_course = 0
if logging_succes:
    print("Logging succes, pls choose course:<1-6>")

    what_course = input()
    time.sleep(2)
    if what_course !=0:
        select_course(what_course)
print("Your chose: ", what_course)

while True:
    time.sleep(360)
    browser.refresh()


