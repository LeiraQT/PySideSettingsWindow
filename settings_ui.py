# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os, config_handler as ch, offsetwindow, settings as s
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
winWidth = 549
winHeight = 454
directory = ""

class Ui_Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel("Вы действительно хотите применить изменения?")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setContextMenuPolicy(Qt.CustomContextMenu)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.accept)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(Ui_Dialog().saveDataToCurrent)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)
        self.verticalLayout.addWidget(self.buttonBox)
        self.setWindowTitle("Предупреждение")


# class Ui_Form2(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.verticalLayout = QVBoxLayout(self)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.label = QLabel("Укажите название новой конфигурации:")
#         self.label.setLayoutDirection(Qt.LeftToRight)
#         self.label.setAlignment(Qt.AlignCenter)
#         self.label.setObjectName("label")
#         self.verticalLayout.addWidget(self.label)
#         self.buttonBox = QDialogButtonBox(self)
#         self.buttonBox.setEnabled(True)
#         self.buttonBox.setContextMenuPolicy(Qt.CustomContextMenu)
#         self.buttonBox.setStandardButtons(QDialogButtonBox.Apply)
#         self.buttonBox.setCenterButtons(True)
#         self.buttonBox.setObjectName("buttonBox")
#         obj = QLineEdit()
#         self.verticalLayout.addWidget(obj)
#         self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.accept)
#         self.verticalLayout.addWidget(self.buttonBox)
#         self.setWindowTitle("Предупреждение")
          

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

    def saveDataToCurrent(self):
        """
        Сохранение введенных пользователем данных в выбранный конфиг
        """

        path = os.getcwd() + "/config/" + self.comboBox.currentText()

        s.multFieldValue = self.findChild(QLineEdit,"multField").property("text")
        s.heightFieldValue = self.findChild(QLineEdit,"heightField").property("text")
        s.vertStepFieldValue = self.findChild(QLineEdit,"vertStepField").property("text")
        s.OXLabelValue = self.findChild(QLabel,"OXLabel").property("text").split(":")[1]
        s.OYLabelValue = self.findChild(QLabel,"OYLabel").property("text").split(":")[1]
        s.thresholdCFFieldValue = self.findChild(QLineEdit,"thresholdCFField").property("text")
        s.thresholdСontourFieldValue = self.findChild(QLineEdit,"thresholdСontourField").property("text")
        s.delayFieldValue = self.findChild(QLineEdit,"delayField").property("text")
        s.IPFieldValue = self.findChild(QLineEdit,"IPField").property("text")
        s.portFieldValue = self.findChild(QLineEdit,"portField").property("text")

        ch.update_setting(path, "Offset settings", "multiplier", s.multFieldValue)
        ch.update_setting(path, "Offset settings", "height", s.heightFieldValue)
        ch.update_setting(path, "Offset settings", "vertical step", s.vertStepFieldValue)
        ch.update_setting(path, "Offset settings", "OX", s.OXLabelValue)
        ch.update_setting(path, "Offset settings", "OY", s.OYLabelValue)

        ch.update_setting(path, "Debug settings", "threshold canny filter", s.thresholdCFFieldValue)
        ch.update_setting(path, "Debug settings", "threshold contour", s.thresholdСontourFieldValue)
        ch.update_setting(path, "Debug settings", "delay", s.delayFieldValue)

        ch.update_setting(path, "Connection settings", "IP", s.IPFieldValue)
        ch.update_setting(path, "Connection settings", "port", s.portFieldValue)
        
    
    def saveDataToCurrent(self, path=os.getcwd()+"/config/"):
            """
            Сохранение введенных пользователем данных в выбранный конфиг
            """

            path = os.getcwd() + "/config/" + self.comboBox.currentText()

            s.multFieldValue = self.findChild(QLineEdit,"multField").property("text")
            s.heightFieldValue = self.findChild(QLineEdit,"heightField").property("text")
            s.vertStepFieldValue = self.findChild(QLineEdit,"vertStepField").property("text")
            s.OXLabelValue = self.findChild(QLabel,"OXLabel").property("text").split(":")[1]
            s.OYLabelValue = self.findChild(QLabel,"OYLabel").property("text").split(":")[1]
            s.thresholdCFFieldValue = self.findChild(QLineEdit,"thresholdCFField").property("text")
            s.thresholdСontourFieldValue = self.findChild(QLineEdit,"thresholdСontourField").property("text")
            s.delayFieldValue = self.findChild(QLineEdit,"delayField").property("text")
            s.IPFieldValue = self.findChild(QLineEdit,"IPField").property("text")
            s.portFieldValue = self.findChild(QLineEdit,"portField").property("text")

            ch.update_setting(path, "Offset settings", "multiplier", s.multFieldValue)
            ch.update_setting(path, "Offset settings", "height", s.heightFieldValue)
            ch.update_setting(path, "Offset settings", "vertical step", s.vertStepFieldValue)
            ch.update_setting(path, "Offset settings", "OX", s.OXLabelValue)
            ch.update_setting(path, "Offset settings", "OY", s.OYLabelValue)

            ch.update_setting(path, "Debug settings", "threshold canny filter", s.thresholdCFFieldValue)
            ch.update_setting(path, "Debug settings", "threshold contour", s.thresholdСontourFieldValue)
            ch.update_setting(path, "Debug settings", "delay", s.delayFieldValue)

            ch.update_setting(path, "Connection settings", "IP", s.IPFieldValue)
            ch.update_setting(path, "Connection settings", "port", s.portFieldValue)
            

    def loadDataFromCurrent(self):
        """
        Загрузка данных из выбранного конфига в окно
        """

        path = os.getcwd() + "/config/" + self.comboBox.currentText()

        s.multFieldValue = ch.get_setting(path, "Offset settings", "multiplier")
        s.heightFieldValue = ch.get_setting(path, "Offset settings", "height")
        s.vertStepFieldValue = ch.get_setting(path, "Offset settings", "vertical step")
        s.OXLabelValue = ch.get_setting(path, "Offset settings", "OX")
        s.OYLabelValue = ch.get_setting(path, "Offset settings", "OY")

        s.thresholdCFFieldValue = ch.get_setting(path, "Debug settings", "threshold canny filter")
        s.thresholdСontourFieldValue = ch.get_setting(path, "Debug settings", "threshold contour")
        s.delayFieldValue = ch.get_setting(path, "Debug settings", "delay")

        s.IPFieldValue = ch.get_setting(path, "Connection settings", "IP")
        s.portFieldValue = ch.get_setting(path, "Connection settings", "port")

        self.findChild(QLineEdit,"multField").setProperty("text", s.multFieldValue)
        self.findChild(QLineEdit,"heightField").setProperty("text", s.heightFieldValue)
        self.findChild(QLineEdit,"vertStepField").setProperty("text", s.vertStepFieldValue)
        self.findChild(QLabel,"OXLabel").setProperty("text", "OX:" + s.OXLabelValue)
        self.findChild(QLabel,"OYLabel").setProperty("text", "OY:" + s.OYLabelValue)
        self.findChild(QLineEdit,"thresholdCFField").setProperty("text", s.thresholdCFFieldValue)
        self.findChild(QLineEdit,"thresholdСontourField").setProperty("text", s.thresholdСontourFieldValue)
        self.findChild(QLineEdit,"delayField").setProperty("text", s.delayFieldValue)
        self.findChild(QLineEdit,"IPField").setProperty("text", s.IPFieldValue)
        self.findChild(QLineEdit,"portField").setProperty("text", s.portFieldValue)

    """
    Вызов окна, в котором можно изменить текущий отступ по осям
    """

    def callOffsetWindow(self):
        if not self.offsetWindow:
            self.offsetWindow = offsetwindow.Ui_Dialog(self)
            self.offsetWindow.exec()
        
    def createDestination(self):
        s.createDirectory = str(QFileDialog.getExistingDirectory(self, "Выберите папку, куда сохранять результат"))
    def loadDestination(self):
        s.loadDirectory = str(QFileDialog.getExistingDirectory(self, "Выберите папку, откуда будут загружаться файлы"))
         
    # def saveDataToNewConfig(self):
    #     """
    #     Сохранение введенных пользователем данных в новый конфиг
    #     """

    #     path = os.getcwd() + "/config/" + self.comboBox.currentText()
        
    #     s.multFieldValue = self.findChild(QLineEdit,"multField").property("text")
    #     s.heightFieldValue = self.findChild(QLineEdit,"heightField").property("text")
    #     s.vertStepFieldValue = self.findChild(QLineEdit,"vertStepField").property("text")
    #     s.OXLabelValue = self.findChild(QLabel,"OXLabel").property("text").split(":")[1]
    #     s.OYLabelValue = self.findChild(QLabel,"OYLabel").property("text").split(":")[1]
    #     s.thresholdCFFieldValue = self.findChild(QLineEdit,"thresholdCFField").property("text")
    #     s.thresholdСontourFieldValue = self.findChild(QLineEdit,"thresholdСontourField").property("text")
    #     s.delayFieldValue = self.findChild(QLineEdit,"delayField").property("text")
    #     s.IPFieldValue = self.findChild(QLineEdit,"IPField").property("text")
    #     s.portFieldValue = self.findChild(QLineEdit,"portField").property("text")
        
    #     ch.update_setting(path, "Offset settings", "multiplier", s.multFieldValue)
    #     ch.update_setting(path, "Offset settings", "height", s.heightFieldValue)
    #     ch.update_setting(path, "Offset settings", "vertical step", s.vertStepFieldValue)
    #     ch.update_setting(path, "Offset settings", "OX", s.OXLabelValue)
    #     ch.update_setting(path, "Offset settings", "OY", s.OYLabelValue)

    #     ch.update_setting(path, "Debug settings", "threshold canny filter", s.thresholdCFFieldValue)
    #     ch.update_setting(path, "Debug settings", "threshold contour", s.thresholdСontourFieldValue)
    #     ch.update_setting(path, "Debug settings", "delay", s.delayFieldValue)

    #     ch.update_setting(path, "Connection settings", "IP", s.IPFieldValue)
    #     ch.update_setting(path, "Connection settings", "port", s.portFieldValue)

    def diagWindowApply(self):
        dialog = Ui_Form(self)
        dialog.exec_()

    def initDialogWindowSave(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialogWindowSave)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Предупреждение')
        self.show()
    def showDialogWindowSave(self):
        text, ok = QInputDialog.getText(self, 'Предупреждение','Укажите название новой конфигурации:')
        if ok:
            self.le.setText(str(text))

    # def diagWindowSave(self):
    #     dialog = Ui_Form2(self)
    #     dialog.exec_()
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
        folder = os.getcwd() + "/config"
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
        self.comboBox.setCurrentText("default.config")
        self.comboBox.currentTextChanged.connect(self.loadDataFromCurrent)

        self.verticalLayout.addWidget(self.comboBox)

        self.tabWidget = QTabWidget()
        self.tabWidget.setObjectName("tabWidget")

        """
        Вкладка 1:
        """

        self.tab = QWidget()
        mainLayout1 = QVBoxLayout()

        # Слой для отступа
        offsetLayout = QHBoxLayout()
        # picture

        #l = QtGui.QLabel()
        # l.setPixmap(QtGui.QPixmap("folder.png"))

        labelLayout = QVBoxLayout()
        OXLabel = QLabel("OX:")
        OXLabel.setObjectName("OXLabel")
        OYLabel = QLabel("OY:")
        OYLabel.setObjectName("OYLabel")
        labelLayout.addWidget(OXLabel)
        labelLayout.addWidget(OYLabel)
        changeOffsetButton = QPushButton("Изменить смещение")
        changeOffsetButton.clicked.connect(self.callOffsetWindow)
        offsetLayout.addLayout(labelLayout)
        offsetLayout.addWidget(changeOffsetButton)

        """
        Слой для надписей
        """
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

        """
        Слой для полей
        """
        fieldsLayout = QVBoxLayout()
        multField = QLineEdit()
        multField.setObjectName("multField")
        fromButton = QPushButton("Изменить путь...")
        fromButton.clicked.connect(self.loadDestination)
        toButton = QPushButton("Изменить путь...")
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

        """
        Вкладка 2:
        """

        self.tab_2 = QWidget()
        mainLayout2 = QVBoxLayout()
        mainLayout2.addWidget(QLabel("Настройки отладки:"))

        debugLayout = QHBoxLayout()

        """
        Слой для надписей
        """
        textLayout2 = QVBoxLayout()
        thresholdCFLabel = QLabel("Порог фильтра Canny:")
        thresholdСontourLabel = QLabel("Порог контура:")
        delayLabel = QLabel("Задержка между шагом:")

        textLayout2.addWidget(thresholdCFLabel)
        textLayout2.addWidget(thresholdСontourLabel)
        textLayout2.addWidget(delayLabel)

        """
        Слой для полей
        """
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

        """
        Слой для надписей
        """
        textLayout3 = QVBoxLayout()
        IPLabel = QLabel("IP: ")
        portLabel = QLabel("port: ")

        textLayout3.addWidget(IPLabel)
        textLayout3.addWidget(portLabel)

        """
        Слой для полей
        """
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
        """
        Добавление всего tabWidget на окно настроек
        """
        self.verticalLayout.addWidget(self.tabWidget)
        """
        Добавление группы кнопок снизу
        """
        # Rнопки выхода из диалогового окна
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply | QDialogButtonBox.Save | QDialogButtonBox.Cancel)          
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.diagWindowApply)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.saveDataToCurrent)
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.showDialogWindowSave)
        #Вместо self.reject можно вставить свою функцию, которая также будет отправлять сигнал reject
        #TODO - переделать кнопки в отдельные объекты
        self.buttonBox.rejected.connect(self.reject)
        #ВЫЗЫВАТЬ ОКНО ПОДТВЕРЖДЕНИЯ "Введные вами данные могут изменить config. Вы уверены? yn"
        #self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.accept) #ВЫЗЫВАТЬ ОКНО ПОДТВЕРЖДЕНИЯ "Введные вами данные могут изменить config. Вы уверены? yn"
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.setLayout(self.verticalLayout)
        self.loadDataFromCurrent()

    def callOffsetWindow(self):
         if not self.offsetWindow:
             self.offsetWindow = offsetwindow.OffsetWin(self)
             self.offsetWindow.show()
        
    def createDestination(self):
        s.createDirectory = str(QFileDialog.getExistingDirectory(self, "Выберите папку, куда сохранять результат"))
    def loadDestination(self):
        s.loadDirectory = str(QFileDialog.getExistingDirectory(self, "Выберите папку, откуда будут загружаться файлы"))




        
