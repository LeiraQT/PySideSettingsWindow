import config_handler as ch

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_Dialog(QDialog):

    def __init__(self, parent=None):
        """
        Передаём ссылку на родительский элемент и чтобы виджет
        отображался как самостоятельное окно указываем тип окна
        """
        super().__init__(parent, Qt.Dialog)
        self.setWindowFlag(Qt.Dialog)
        self.offsetWindow = None
        self.setupUi()
    def setupUi(self):
        self.setObjectName("InnerDialog")
        self.setWindowTitle("Настройки смещения картинок по осям") # заголовок окна
        self.move(300, 300) # положение окна
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.setLayout(self.verticalLayout)

