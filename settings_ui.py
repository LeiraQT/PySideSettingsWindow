# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

winWidth = 549
winHeight = 454

#import offsetwindow

class Ui_Dialog(QDialog):
    def __init__(self, parent=None):
        """
        Передаём ссылку на родительский элемент и чтобы виджет
        отображался как самостоятельное окно указываем тип окна
        """
        super().__init__(parent, Qt.Dialog)
        self.offsetWindow = None
        self.setupUi()
    def SaveData(self):
            multFieldValue = self.findChild(QLineEdit,"multField").property("text")
            heightFieldValue = self.findChild(QLineEdit,"heightField").property("text")
            vertStepFieldValue = self.findChild(QLineEdit,"vertStepField").property("text")
            OXLabelValue = self.findChild(QLabel,"OXLabel").property("text").split(":")[1]
            OYLabelValue = self.findChild(QLabel,"OYLabel").property("text").split(":")[1]
            thresholdCFFieldValue = self.findChild(QLineEdit,"thresholdCFField").property("text")
            thresholdСontourFieldValue = self.findChild(QLineEdit,"thresholdСontourField").property("text")
            delayFieldValue = self.findChild(QLineEdit,"delayField").property("text")
            IPFieldValue = self.findChild(QLineEdit,"IPField").property("text")
            portFieldValue = self.findChild(QLineEdit,"portField").property("text")
            print(multFieldValue)
            print(heightFieldValue)
            print(vertStepFieldValue)
            print(OXLabelValue)
            print(OYLabelValue)
            print(thresholdCFFieldValue)
            print(thresholdСontourFieldValue)
            print(delayFieldValue)
            print(IPFieldValue)
            print(portFieldValue)
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setWindowTitle("Настройки")
        self.resize(winWidth, winHeight)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.comboBox = QComboBox()

        """
        Поиск папки с конфигами в рабочей области приложения
        """
        configs = []
        folder = os.getcwd()
        folder += "/config"
        if not os.path.exists(folder):
                try:
                        os.mkdir(folder)
                except OSError:
                        QMessageBox.critical(self, "Ошибка ", "Создать директорию %s не удалось. Создайте директрорию используя права администратора" % folder, QMessageBox.Ok)
        
        """
        Проверка на существование конфига сделана в config_handler.
        Создается объект конфига
        """
        config = ch.get_config(folder + "/default.config")
        """
        Добавление всех существующих конфигов из папки в список
        Данный список будет выводиться в QComboBox
        """
        for config in os.listdir(folder):
                configs.append(config)
        self.comboBox.addItems(configs)
        self.comboBox.setCurrentIndex(-1)

        self.verticalLayout.addWidget(self.comboBox)

        self.tabWidget = QTabWidget()
        self.tabWidget.setObjectName("tabWidget")
##########################################################
# Вкладка 1
##########################################################

        self.tab = QWidget()
        mainLayout1 = QVBoxLayout()

        # Слой для отступа
        offsetLayout = QHBoxLayout()
        # picture

        #l = QtGui.QLabel()
        # l.setPixmap(QtGui.QPixmap("folder.png"))

        labelLayout = QVBoxLayout()
        OXLabel = QLabel("OX:228")
        OXLabel.setObjectName("OXLabel")
        OYLabel = QLabel("OY:337")
        OYLabel.setObjectName("OYLabel")
        labelLayout.addWidget(OXLabel)
        labelLayout.addWidget(OYLabel)
        changeOffsetButton = QPushButton("Изменить смещение")
        #changeOffsetButton.clicked.connect()
        offsetLayout.addLayout(labelLayout)
        offsetLayout.addWidget(changeOffsetButton)

        # Слой для надписей
        textLayout = QVBoxLayout()
        multLabel = QLabel("Множитель шага при сканировании:")
        fromLabel = QLabel("Путь к источнику снимков:")
        toLabel = QLabel("Путь сохранения:")
        heightLabel = QLabel("Рабочая высота:")
        vertStepLabel = QLabel("Шаг высоты:")

        textLayout.addWidget(multLabel)
        textLayout.addWidget(fromLabel)
        textLayout.addWidget(toLabel)
        textLayout.addWidget(heightLabel)
        textLayout.addWidget(vertStepLabel)

        # Слой для полей
        fieldsLayout = QVBoxLayout()
        multField = QLineEdit()
        multField.setObjectName("multField")
        fromButton = QPushButton("Изменить путь...")
        toButton = QPushButton("Изменить путь...")
        global directory 
        toButton.clicked.connect(self.createDestination)
        
        heightField = QLineEdit()
        heightField.setObjectName("heightField")
        vertStepField = QLineEdit()
        vertStepField.setObjectName("vertStepField")

        fieldsLayout.addWidget(multField)
        fieldsLayout.addWidget(fromButton)
        fieldsLayout.addWidget(toButton)
        fieldsLayout.addWidget(heightField)
        fieldsLayout.addWidget(vertStepField)

        finalLayout = QHBoxLayout()
        finalLayout.addLayout(textLayout)
        finalLayout.addLayout(fieldsLayout)

        mainLayout1.addLayout(offsetLayout)
        mainLayout1.addLayout(finalLayout)

        self.tab.setLayout(mainLayout1)
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "Настройки смещения")
##########################################################
# Вкладка 2
##########################################################
        self.tab_2 = QWidget()
        mainLayout2 = QVBoxLayout()
        mainLayout2.addWidget(QLabel("Настройки отладки:"))

        debugLayout = QHBoxLayout()

        # Слой для надписей
        textLayout2 = QVBoxLayout()
        thresholdCFLabel = QLabel("Порог фильтра Canny:")
        thresholdСontourLabel = QLabel("Порог контура:")
        delayLabel = QLabel("Задержка между шагом:")

        textLayout2.addWidget(thresholdCFLabel)
        textLayout2.addWidget(thresholdСontourLabel)
        textLayout2.addWidget(delayLabel)

        # Слой для полей
        fieldsLayout2 = QVBoxLayout()
        thresholdCFField = QLineEdit()
        thresholdCFField.setObjectName("thresholdCFField")
        thresholdСontourField = QLineEdit()
        thresholdСontourField.setObjectName("thresholdСontourField")
        delayField = QLineEdit()
        delayField.setObjectName("delayField")

        fieldsLayout2.addWidget(thresholdCFField)
        fieldsLayout2.addWidget(thresholdСontourField)
        fieldsLayout2.addWidget(delayField)

        debugLayout.addLayout(textLayout2)
        debugLayout.addLayout(fieldsLayout2)

        mainLayout2.addLayout(debugLayout)
        mainLayout2.addWidget(QLabel("Настройки  подключения:"))

        serverLayout = QHBoxLayout()

        # Слой для надписей
        textLayout3 = QVBoxLayout()
        IPLabel = QLabel("IP: ")
        portLabel = QLabel("port: ")

        textLayout3.addWidget(IPLabel)
        textLayout3.addWidget(portLabel)

        # Слой для полей
        fieldsLayout3 = QVBoxLayout()
        IPField = QLineEdit()
        IPField.setObjectName("IPField")
        portField = QLineEdit()
        portField.setObjectName("portField")

        fieldsLayout3.addWidget(IPField)
        fieldsLayout3.addWidget(portField)

        serverLayout.addLayout(textLayout3)
        serverLayout.addLayout(fieldsLayout3)

        mainLayout2.addLayout(serverLayout)

        self.tab_2.setLayout(mainLayout2)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "Настройки отладки и подключения")
##########################################################
# Добавление
        self.verticalLayout.addWidget(self.tabWidget)
# Создание группы кнопок
##########################################################
        # Rнопки выхода из диалогового окна
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Apply | QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.SaveData)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.setLayout(self.verticalLayout)
##########################################################
# вызов окна
#########################################################

    # def callOffsetWindow(self):
    #     if not self.offsetWindow:
    #         self.offsetWindow = offsetwindow.OffsetWin(self)
    #         self.offsetWindow.show()
    def createDestination():
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        return directory
         
