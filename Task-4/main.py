"""
Требуется создать csv-файл rows_300.csv со следующими столбцами:
– № - номер по порядку (от 1 до 300);
– Секунда – текущая секунда на вашем ПК;
– Микросекунда – текущая миллисекунда на часах.
На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
"""

import csv
import time
from datetime import datetime as dtime

with open('temp.csv', 'w', newline='') as csvfile:
    names = ['№', 'sec', 'msec']
    write = csv.DictWriter(csvfile, fieldnames=names)
    sec_now, msec_now = dtime.now().second, dtime.now().microsecond
    write.writeheader()
    for i in range(1, 301):
        time.sleep(0.01)
        write.writerow({'№': i, 'sec': sec_now, 'msec': msec_now})

with open('temp.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)