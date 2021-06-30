from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
"""
Добавление файла с окном настройки
"""
import settings_ui, settings as s #добавляем файл окна настроек, в котором все находится и файла, в котором находятся все глоабльные переменные

winWidth = 549
winHeight = 454

class MainWindow(QMainWindow): # главное окно
    def __init__(self, parent=None):
        super().__init__(parent)
        """
        # Добавление при инициализации
        """
        self.secondWin = None
        self.setupUi() #ниже до конца функции __init__ - загрузка директорий из txt-файла
        ### по-хорошему, надо проверку на существование файла и уведомление, если пустой
        tempLines = []
        fileToRead = open("directories.txt", "r")
        tempLines = fileToRead.readlines()
        tempCreateDirectory = tempLines[0]
        s.createDirectory = tempCreateDirectory.replace("\n", "") # избавляемся от \n
        s.loadDirectory = tempLines[1]
        #print(s.createDirectory + " - загрузил в createDirectory")
        #print(s.loadDirectory + " - загрузил в loadDirectory")

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
        self.secondWin.setModal(True)
        self.secondWin.show()
        
    """
    # Запись директорий в txt при закрытии программы.
    """
    myclose = False # False не даст закрыться программе сразу
    def closeEvent(self,event):
        if self.myclose:
            print ("я закрылся и ничего не записал!!")
        else:
            event.ignore()
            fileToWrite = open("directories.txt","w")
            fileToWrite.write(s.createDirectory)
            fileToWrite.write("\n")
            fileToWrite.write(s.loadDirectory)
            fileToWrite.close()
            #print(s.createDirectory + " - записал в createDirectory")
            #print(s.loadDirectory + " - записал в loadDirectory")
            QCoreApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    