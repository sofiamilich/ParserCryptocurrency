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



