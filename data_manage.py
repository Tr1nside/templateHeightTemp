import os
from PySide2.QtCore import QDate


# Функция создания QDate объекта, функция принимает строку в виде "20001231", где 2000 - год, 12 - месяц, 31 - день 
def create_QDate(date):
    y = int(date[:4])
    m = int(date[4:6])
    d = int(date[6:])
    return QDate(y, m, d)

# Функция получения первой и последней даты из имен файлов в папке ./data_files
def get_first_last_date(self):
    files = sorted(os.listdir('./data_files'))
    
    dates_full = [files[0][4:12], files[len(files)-1][4:12]]
    self.dates = (create_QDate(dates_full[0]), create_QDate(dates_full[1]))
