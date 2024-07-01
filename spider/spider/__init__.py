# ОБЩИЙ РАБОЧИЙ КОД прокручивает сайт и считывает значение, СЧИТАЕТ СУММУ И % КАЖДОЙ ОТ 100 ВАЛЮТ


from selenium import webdriver
import bs4
from time import sleep
from datetime import datetime
import csv
import re

def parser():
    driver = webdriver.Chrome()
    driver.get('https://coinmarketcap.com/ru/')
    driver.maximize_window()

    # Прокрутка страницы для динамической загрузки контента
    px = 0
    for i in range(10):
        px += 750
        driver.execute_script(f'window.scrollTo(0, {px})')
        sleep(2)  # Увеличенная задержка для уверенности в загрузке данных

    # Получение исходного кода страницы после прокрутки
    html = driver.page_source
    driver.close()
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Парсинг данных с использованием BeautifulSoup
    list_of_names = soup.find_all('div', {'class': 'sc-4c05d6ef-0 sc-1c5f2868-1 dlQYLv gunIRl'})
    list_of_values = soup.find_all('span', {'class': 'sc-11478e5d-1 hwOFkt'})

    # Получение времени и перевод в нужный формат
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H.%M %d.%m.%Y")

    # Использование времени в названии файла
    filename = f'output {formatted_time}.csv'

    # Регулярное выражение для извлечения числовых значений капитализации
    pattern = r'₽\s?(\d+(?:[.,]\d+)*)'

    # Сначала соберем все значения капитализации
    values = []
    for value in list_of_values[:100]:  # Ограничение до первых 100 значений
        match = re.search(pattern, value.text)
        if match:
            value_cleaned = match.group(1).replace(',', '').replace('.', '', match.group(1).count('.') - 1)
            values.append(float(value_cleaned))

    # Теперь вычислим общую сумму
    total_sum = sum(values)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerow(['Name', 'MC', 'MP'])  # Добавление нового столбца MP

        for name, value in zip(list_of_names, values):
            market_percentage = (value / total_sum) * 100  # Расчет процента рынка
            csvwriter.writerow([name.text, value, f'{market_percentage:.2f}%'])

    # Вывод суммы после цикла
    print(f'Сумма первых 100 значений капитализации: {total_sum}')

# Вызов функции парсера
parser()




# from selenium import webdriver
# import bs4
# from time import sleep
# from datetime import datetime
# import csv
# import re
#
# def parser():
#     driver = webdriver.Chrome()
#     driver.get('https://coinmarketcap.com/ru/')
#     driver.maximize_window()
#
#     # Прокрутка страницы для динамической загрузки контента
#     px = 0
#     for i in range(10):
#         px += 750
#         driver.execute_script(f'window.scrollTo(0, {px})')
#         sleep(2)  # Увеличенная задержка для уверенности в загрузке данных
#
#     # Получение исходного кода страницы после прокрутки
#     html = driver.page_source
#     driver.close()
#     soup = bs4.BeautifulSoup(html, 'html.parser')
#
#     # Парсинг данных с использованием BeautifulSoup
#     list_of_names = soup.find_all('div', {'class': 'sc-4c05d6ef-0 sc-1c5f2868-1 dlQYLv gunIRl'})
#     list_of_values = soup.find_all('span', {'class': 'sc-11478e5d-1 hwOFkt'})
#
#     # Получение времени и перевод в нужный формат
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("%H.%M %d.%m.%Y")
#
#     # Использование времени в названии файла
#     filename = f'output {formatted_time}.csv'
#
#     # Регулярное выражение для извлечения числовых значений капитализации
#     pattern = r'₽\s?(\d+(?:[.,]\d+)*)'
#
#     total_sum = 0  # Инициализация переменной для суммы
#     count = 0  # Инициализация счетчика
#
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=';')
#         csvwriter.writerow(['Name', 'MC'])  # Запись заголовков
#
#         for name, value in zip(list_of_names, list_of_values):
#             match = re.search(pattern, value.text)
#             if match and count < 100:  # Проверка наличия совпадения и лимита записей
#                 value_cleaned = match.group(1).replace(',', '')
#                 csvwriter.writerow([name.text, value_cleaned])
#                 total_sum += float(value_cleaned)  # Добавление значения к сумме
#                 count += 1  # Увеличение счетчика
#
#     # Вывод суммы после цикла
#     print(f'Сумма первых 100 значений капитализации: {total_sum}')
#
# # Вызов функции парсера
# parser()
#
#
#
#
#
#







# from selenium import webdriver
# import bs4
# from time import sleep
# from datetime import datetime
# import csv
# import re
# # ПАРСЕР - СЧИТЫВАЕТ, ЗАПИСЫВАЕТ В csv, УБИРАЕТ ЗНАКИ
# def parser():
#     driver = webdriver.Chrome()
#     driver.get('https://coinmarketcap.com/ru/')
#     driver.maximize_window()
#
#     # Прокрутка страницы для динамической загрузки контента
#     px = 0
#     for i in range(10):
#         px += 750
#         driver.execute_script(f'window.scrollTo(0, {px})')
#         sleep(2)  # Увеличенная задержка для уверенности в загрузке данных
#
#     # Получение исходного кода страницы после прокрутки
#     html = driver.page_source
#     driver.close()
#     soup = bs4.BeautifulSoup(html, 'html.parser')
#
#     # Парсинг данных с использованием BeautifulSoup
#     list_of_names = soup.find_all('div', {'class': 'sc-4c05d6ef-0 sc-1c5f2868-1 dlQYLv gunIRl'})
#     list_of_values = soup.find_all('span', {'class': 'sc-11478e5d-1 hwOFkt'})
#
#     # Получение времени и перевод в нужный формат
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("%H.%M %d.%m.%Y")
#
#     # Использование времени в названии файла
#     filename = f'output {formatted_time}.csv'
#
#     # Регулярное выражение для извлечения числовых значений капитализации
#     pattern = r'₽\s?(\d+(?:[.,]\d+)*)'
#
#
#
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=';')
#
#         # Запись заголовков
#         csvwriter.writerow(['Name', 'MC'])
#
#         # Запись данных
#         for name, value in zip(list_of_names, list_of_values):
#             # Обработка текста с использованием регулярного выражения
#             match = re.search(pattern, value.text)
#             if match:
#                 # Извлечение числового значения без символа валюты
#                 value_cleaned = match.group(1).replace(',', '')
#             else:
#                 value_cleaned = 'N/A'  # Если число не найдено, записываем 'N/A'
#             # Запись имени криптовалюты без изменений
#             name_cleaned = name.text
#             csvwriter.writerow([name_cleaned, value_cleaned])
#
# # Вызов функции парсера
# parser()

















# from selenium import webdriver
# import bs4
# from time import sleep
# from datetime import datetime


# import csv
# import re
#
# def parser():
#     driver = webdriver.Chrome()
#     driver.get('https://coinmarketcap.com/all/views/all/')
#     driver.maximize_window()
#
#     # Прокрутка страницы для динамической загрузки контента
#     px = 0
#     for i in range(10):
#         px += 1000
#         driver.execute_script(f'window.scrollTo(0, {px})')
#         sleep(2)  # Увеличенная задержка для уверенности в загрузке данных
#
#     # Получение исходного кода страницы после прокрутки
#     html = driver.page_source
#     driver.close()
#     soup = bs4.BeautifulSoup(html, 'html.parser')
#
#     # Парсинг данных с использованием BeautifulSoup
#     list_of_values = soup.find_all('div', {'class': 'sc-4c05d6ef-0 sc-1c5f2868-1 dlQYLv gunIRl'})
#     list_of_names = soup.find_all('span', {'class': 'sc-11478e5d-0 fepLYC'})
#
#     # Извлечение числовых значений капитализации и расчет общей суммы
#     market_caps = []
#     for value in list_of_values[:100]:
#         market_cap_str = re.findall(r'\d+[\.,]?\d*', value.get_text().replace(',', ''))[0]
#         market_cap = float(market_cap_str.replace('.', '').replace(',', '.'))
#         market_caps.append(market_cap)
#     total_market_cap = sum(market_caps)
#
#     # Получение времени и перевод в нужный формат
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("%H.%M %d.%m.%Y")
#
#     # Использование времени в названии файла
#     filename = f'output {formatted_time}.csv'
#
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=';')
#
#         # Запись заголовков
#         csvwriter.writerow(['Название', 'Рыночная капитализация', 'Процент от общей капитализации'])
#
#         # Запись данных
#         for market_cap, name in zip(market_caps, list_of_names[:100]):
#             percentage = (market_cap / total_market_cap) * 100
#             csvwriter.writerow([name.get_text(), f'{market_cap}', f'{percentage:.2f}%'])
#
# # Вызов функции парсера
# parser()
#







# from selenium import webdriver
# import bs4
# from time import sleep
# from datetime import datetime
# import csv
# import re
#
# def parser():
#     driver = webdriver.Chrome()
#     driver.get('https://coinmarketcap.com/ru/')
#     driver.maximize_window()
#
#     # Прокрутка страницы для динамической загрузки контента
#     px = 0
#     for i in range(10):
#         px += 150
#         driver.execute_script(f'window.scrollTo(0, {px})')
#         sleep(2)  # Увеличенная задержка для уверенности в загрузке данных
#
#     # Получение исходного кода страницы после прокрутки
#     html = driver.page_source
#     driver.close()
#     soup = bs4.BeautifulSoup(html, 'html.parser')
#
#     # Парсинг данных с использованием BeautifulSoup
#
#     list_of_names = soup.find_all('div', {'class': 'sc-4c05d6ef-0 sc-1c5f2868-1 dlQYLv gunIRl'})
#     list_of_values = soup.find_all('span', {'class': 'sc-11478e5d-1 hwOFkt'})
#
#
#     # Получение времени и перевод в нужный формат
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("%H.%M %d.%m.%Y")
#
#     # Использование времени в названии файла
#     filename = f'output {formatted_time}.csv'
#
#     # Регулярное выражение для извлечения числовых значений капитализации
#     pattern = r'₽(\d*\.\d*)'
#     replacement = r'\1'
#
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=';')
#
#         # Запись заголовков
#         csvwriter.writerow(['Name', 'MC'])
#
#         # Запись данных
#         for name, value in zip(list_of_names, list_of_values):
#             # Обработка текста с использованием регулярного выражения
#             value_cleaned = re.sub(pattern, replacement, value.text)
#             # Запись имени криптовалюты без изменений
#             name_cleaned = name.text
#             csvwriter.writerow([value_cleaned, name_cleaned])
#
# # Вызов функции парсера
# parser()




# from selenium import webdriver
# import bs4
# from time import sleep
# from datetime import datetime
# import csv
#
# def parser() -> dict:
#     driver = webdriver.Chrome()
#     driver.get('https://coinmarketcap.com/ru/')
#     driver.maximize_window()
#
#     # Прокрутка страницы для динамической загрузки контента
#     px = 0
#     for i in range(10):
#         px += 1000
#         driver.execute_script(f'window.scrollTo(0, {px})')
#         sleep(2)  # Увеличенная задержка для уверенности в загрузке данных
#
#     # Получение исходного кода страницы после прокрутки
#     html = driver.page_source
#     driver.close()
#     soup = bs4.BeautifulSoup(html, 'html.parser')
#
#     # Парсинг данных с использованием BeautifulSoup
#     list_of_values = soup.find_all('div', {'class': 'sc-4c05d6ef-0 sc-1c5f2868-1 dlQYLv gunIRl'})
#     list_of_names = soup.find_all('span', {'class': 'sc-11478e5d-0 fepLYC'})
#
#     # Получение времени и перевод в нужный формат
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("%H.%M %d.%m.%Y")
#
#     # Использование времени в названии файла
#     filename = f'output {formatted_time}.csv'
#
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=' ')
#
#         # Запись данных
#         for values, names in zip(list_of_values, list_of_names):
#             csvwriter.writerow([values.text, names.text])
#
# # Вызов функции парсера
# parser()