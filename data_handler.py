from PyQt5.QtWidgets import *
import settings_ui

class DataConfig():
    def __init__(self) -> None:
        self.getData()
    def getData(self):
        IP = settings_ui.IPField