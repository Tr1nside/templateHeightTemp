from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import sys
import data_manage as DataM
from ohata import OhataWindow
from data_manage import get_data


class MainWidget(QWidget):
    def __init__(self, width: int, height: int, parent=None):
        QWidget.__init__(self, parent)
        designer_file = QFile("mainWin.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(designer_file, self)
        designer_file.close()
        self.setMinimumSize(600, 400)
        self.setWindowTitle("Фамилия И.О.")

        # Создаю layout и добавляю в него фреймы c объектами
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.ui.buttonsFrame)
        main_layout.addWidget(self.ui.frame_2)

        # Подключаем кнопки
        self.ui.ohataButton.clicked.connect(self.open_ohata)

        self.dates = tuple  # Создаем пустой кортеж для хранения первой и последней даты
        DataM.get_first_last_date(self)
        self.ui.timeEdit.setDateRange(self.dates[0], self.dates[1])

        self.data = get_data("./data_files/", "./data.txt")

    def open_ohata(self):
        self.win = OhataWindow(self.width, self.height)
        self.win.show()


def start_program():
    app = QApplication(sys.argv)
    screen_rect = app.primaryScreen().availableGeometry()
    mainwin = MainWidget(screen_rect.width(), screen_rect.height())
    mainwin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_program()
