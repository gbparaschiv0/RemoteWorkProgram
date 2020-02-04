from __future__ import annotations
import sys
from remote_UI import Ui_mainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class button:
    __green = "rgb(0, 170, 127);"
    __red = "rgb(170, 0, 0);"
    __linked = False
    uiButton = {}

    def __init__(self, uiButton: QtWidgets.QPushButton):
        self.uiButton = uiButton
        self.__connectUi()
    
    def specialAction(self):
        pass

    def __action(self):
        print("Doar Test")
        self.__swapColors()
        self.specialAction()

    def __connectUi(self):
        self.uiButton.clicked.connect(self.__action)

    def __swapColors(self):
        self.uiButton.setStyleSheet("background-color: " + self.__green)
        self.__linkedButton.uiButton.setStyleSheet("background-color: " + self.__red)

    def link(self, linkedButton: button):
        if(self.__linked == False):
            self.__linked = True
            self.__linkedButton = linkedButton
            linkedButton.link(self)

class RemoteApp:
    def __init__(self, ui: Ui_mainWindow):
        # Assigned Buttons
        self.ui = ui
        self.__connect = button(ui.ConnectButton)
        self.__disconnect = button(ui.DisconnectButton)
        self.__connect.link(self.__disconnect)


if __name__ == "__main__":
    # Init the UI
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)

    MagnaRemote = RemoteApp(ui)

    mainWindow.show()
    sys.exit(app.exec_())