# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

winWidth = 549
winHeight = 454


class Ui_Dialog(QDialog):
    def __init__(self, parent=None):
        # Передаём ссылку на родительский элемент и чтобы виджет
        # отображался как самостоятельное окно указываем тип окна
        super().__init__(parent, Qt.Dialog)
        self.setupUi()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setWindowTitle("Настройки")
        self.resize(winWidth, winHeight)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.comboBox = QComboBox()
        configs = []
        field = os.getcwd()
        print(field)
        self.verticalLayout.addWidget(self.comboBox)

        self.tabWidget = QTabWidget()
        self.tabWidget.setObjectName("tabWidget")
##########################################################
# Вкладка 1
##########################################################
        
        self.tab = QWidget()
        mainLayout1 = QVBoxLayout()

        #Слой для отступа
        offsetLayout = QHBoxLayout()
        #picture

        #l = QtGui.QLabel()
        #l.setPixmap(QtGui.QPixmap("folder.png"))

        labelLayout = QVBoxLayout()
        OXLabel = QLabel("OX:")
        OYLabel = QLabel("OY:")
        labelLayout.addWidget(OXLabel)
        labelLayout.addWidget(OYLabel)
        changeOffsetButton = QPushButton("Изменить смещение")
        offsetLayout.addLayout(labelLayout)
        offsetLayout.addWidget(changeOffsetButton)

        #Слой для надписей
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

        #Слой для полей
        fieldsLayout = QVBoxLayout()
        multField = QLineEdit()
        fromButton = QPushButton("Изменить путь...")
        toButton = QPushButton("Изменить путь...")
        heightField = QLineEdit()
        vertStepField = QLineEdit()

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

        #Слой для надписей
        textLayout2 = QVBoxLayout()
        thresholdCFLabel = QLabel("Порог фильтра Canny:")
        thresholdСontourLabel = QLabel("Порог контура:")
        delayLabel = QLabel("Задержка между шагом:")
        
        textLayout2.addWidget(thresholdCFLabel)
        textLayout2.addWidget(thresholdСontourLabel)
        textLayout2.addWidget(delayLabel)

        #Слой для полей
        fieldsLayout2 = QVBoxLayout()
        thresholdCFField = QLineEdit()
        thresholdСontourField = QLineEdit()
        delayField = QLineEdit()

        fieldsLayout2.addWidget(thresholdCFField)
        fieldsLayout2.addWidget(thresholdСontourField)
        fieldsLayout2.addWidget(delayField)

        debugLayout.addLayout(textLayout2)
        debugLayout.addLayout(fieldsLayout2)

        mainLayout2.addLayout(debugLayout)
        mainLayout2.addWidget(QLabel("Настройки  удаленного сервера:"))


        serverLayout = QHBoxLayout()

        #Слой для надписей
        textLayout3 = QVBoxLayout()
        IPLabel = QLabel("IP: ")
        portLabel = QLabel("port: ")

        textLayout3.addWidget(IPLabel)
        textLayout3.addWidget(portLabel)

        #Слой для полей
        fieldsLayout3 = QVBoxLayout()
        IPField = QLineEdit()
        portField = QLineEdit()

        fieldsLayout3.addWidget(IPField)
        fieldsLayout3.addWidget(portField)

        serverLayout.addLayout(textLayout3)
        serverLayout.addLayout(fieldsLayout3)
        
        mainLayout2.addLayout(serverLayout)

        self.tab_2.setLayout(mainLayout2)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "Настройки подключения и отладки")
##########################################################
# Добавление
        self.verticalLayout.addWidget(self.tabWidget)
#Создание группы кнопок
##########################################################
        #Rнопки выхода из диалогового окна
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.setLayout(self.verticalLayout)
##########################################################