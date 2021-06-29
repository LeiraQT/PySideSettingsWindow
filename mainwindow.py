from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
"""
Добавление файла с окном настройки
"""
import settings_ui #добавляем файл окна настроек, в котором все находится

winWidth = 549
winHeight = 454

class MainWindow(QMainWindow): # главное окно
    def __init__(self, parent=None):
        super().__init__(parent)
        """
        # Добавление при инициализации
        """
        self.secondWin = None
        self.setupUi()
    def setupUi(self):
        self.setWindowTitle("Настройки") # заголовок окна
        self.move(300, 300) # положение окна
        self.resize(winWidth, winHeight) # размер окна
        """
        # Добавление кнопки
        """
        self.pushButton = QPushButton("Настройки", self)
        self.pushButton.setBaseSize(100, 100)
        self.pushButton.clicked.connect(self.callAnotherWidget)
    """
    # Работа кнопки
    """
    def callAnotherWidget(self):
        if not self.secondWin:
            self.secondWin = settings_ui.Ui_Dialog(self)
        self.secondWin.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    