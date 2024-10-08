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
    files = sorted(os.listdir("./data_files"))

    dates_full = [files[0][4:12], files[len(files) - 1][4:12]]
    self.dates = (create_QDate(dates_full[0]), create_QDate(dates_full[1]))


def get_lines(file_path: str, first_file_flag: bool):
    with open(file_path, "r") as file:
        if first_file_flag:
            lines = file.readlines()[26:]
        else:
            lines = file.readlines()[25:]
    file.close()
    return lines


def write_data_to_file(dir_path: str, data_file_path: str):
    first_file_flag = False
    files = os.listdir(dir_path)
    with open(data_file_path, "w") as data_file:
        for file in files:
            if first_file_flag:
                lines = get_lines(dir_path + file, True)
                data_file.writelines(lines)
            else:
                first_file_flag = True
                lines = get_lines(dir_path + file, False)
                data_file.writelines(lines)
    data_file.close()


def get_data(dir_path: str, data_file_path: str):
    write_data_to_file(dir_path, data_file_path)
    with open(data_file_path, "r") as file:
        lines = file.readlines()
        data = tuple(line.split("\t") for line in lines)
    file.close()
    return data
