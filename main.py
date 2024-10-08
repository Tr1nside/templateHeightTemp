from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import sys
import data_manage as DataM


class MainWidget(QWidget):
    def __init__(self, width: int, height: int, parent=None):
        QWidget.__init__(self, parent)
        designer_file = QFile("mainWin.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(designer_file, self)
        designer_file.close()

        self.setWindowTitle("Фамилия И.О.")
        
        self.dates = tuple # Создаем пустой кортеж для хранения первой и последней даты 
        DataM.get_first_last_date(self)
        self.ui.timeEdit.setDateRange(self.dates[0], self.dates[1])

def start_program():
    app = QApplication(sys.argv)
    screen_rect = app.primaryScreen().availableGeometry()
    mainwin = MainWidget(screen_rect.width(), screen_rect.height())
    mainwin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_program()
