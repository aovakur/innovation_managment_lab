import pandas as pd
import numpy as np
import csv
import sys

result=0
result2=0
b=[]
num = 1
d=0
day=0
tend_max=0
tmin_min=200
bank2=0

def scv_data():
    while 1:
        try:
            a=str(input('Введите название файла = '))
            data = pd.read_csv(a, sep=';', decimal=',', encoding='cp1251', header=1)
            print('Файл',a,'обнаружен')
            return data
        except (IOError, Exception):
            print('Файл не обнаружен. Повтори еще раз')

def salary():
    while 1:
        try:
            b=int(input('Введите зарплату н/час от 500 до 1500 = '))
            if (b>=500 and b<=1500):
                print('Ставка заработной платы в размере',b,'принята')
                return b
        except (IOError, Exception):
            print('Введи корректное число')

def rate_bank():
    while 1:
        try:
            d=int(input('Введи ставку рефинансирования от 5 до 15% годовых = '))
            if (d<=15 and d>=5):
                print('Ставка рефинансирования', d, 'принята')
                return d
        except [IOError, Exception]:
            print('Введи корректное число')


data = scv_data()
salary = salary()
bank = rate_bank()

for index, row in data.iterrows():
        row[4] = float(row[4].replace(' ', '')) # TendDS
        row[6] = float(row[6].replace(' ',''))  # Tш
        row[7] = float(row[7].replace(' ', '')) # Тпз
        row[14]= float(row[14].replace(' ', '')) #  КОЛds
        row[5] = float(row[5].replace(' ', ''))  # Тпз

        if row[5]>tend_max:
            tend_max=row[5]

        if row[4] < tmin_min:
            tmin_min = row[4]

        day=tend_max-tmin_min
        year = day / 365

        bank2 = bank * year
        result += (row[4] * (row[6] * row[14] + row[7])) # Статический момент
        result2 += ((row[4] * bank2)* (row[6] * row[14] + (row[7]*salary))) # Результат

result=round(result,2)
result2=round(result2,2)
year=round(year,2)

print ('Максимальное кол-во дней =', tend_max)
print ('Минимальное кол-во дней =', tmin_min)
print ('Итог дней', day,'в годах',year)
print('Статический момент = ', result, ' н.ч на смену')
print('Стоимость проекта = ',result2, 'рублей')