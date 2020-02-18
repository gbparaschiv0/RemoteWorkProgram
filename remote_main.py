from __future__ import annotations
import sys
from remote_UI import Ui_mainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ctypes import*
import time

on = 1
off = 0

class usbControl:
    __ECU_pins = 12
    __power = 1
    def __init__(self):
        self.mydll = cdll.LoadLibrary(".\libMCP2200.dll")
        self.__pinStatus = 0

    def connect(self):
        retVal = 0
        retVal = self.mydll.MCP2200_connect()

        # If connection
        if(retVal == 0):
            self.mydll.update_pins(self.__pinStatus)

        return retVal

    def disconnect(self):
        self.mydll.MCP2200_disconnect()

    def reset_to_default(self):
        self.__pinStatus = 0
        self.__write()

    def __write(self):
        self.mydll.update_pins(self.__pinStatus)

    def power(self, setState):
        if(setState == on):
            self.__pinStatus |= self.__power
        else:
            self.__pinStatus &= ~self.__power
        self.__write()
        return

    def flash_mode(self):
        self.__pinStatus &= ~self.__ECU_pins
        self.power(off)
        time.sleep(1)
        self.power(on)

    def run_mode(self):
        self.__pinStatus |= self.__ECU_pins
        self.power(off)
        time.sleep(1)
        self.power(on)

class operationsType:
    def __init__(self, bt: button):
        self.__bt = bt
    
    def swapColors(self):
        __green = "rgb(0, 170, 127);"
        __red = "rgb(170, 0, 0);"
        self.__bt.uiButton.setStyleSheet("background-color: " + __green)
        self.__bt.link.lButton.uiButton.setStyleSheet("background-color: " + __red)

    def swapFrames(self):
        self.__bt.link.lFrame.setEnabled(True)
        self.__bt.link.lButton.link.lFrame.setEnabled(False)

    def swapButtonActivation(self):
        self.__bt.uiButton.setEnabled(False)
        self.__bt.link.lButton.uiButton.setEnabled(True)

class commands:
    def __init__(self, bt: button):
        self.bt = bt
        self.operation = operationsType(bt)

    def execute(self):
        pass

class connectCm(commands):
    def execute(self):
        if(MCP2200.connect() == 0):
            self.operation.swapColors()
            self.operation.swapFrames()

class disconnectCm(commands):
    def execute(self):
        MCP2200.disconnect()
        self.operation.swapColors()
        self.operation.swapFrames()

class flashCm(commands):
    def execute(self):
        MCP2200.flash_mode()
        self.operation.swapColors()
        self.operation.swapButtonActivation()

class runCm(commands):
    def execute(self):
        MCP2200.run_mode()
        self.operation.swapColors()
        self.operation.swapButtonActivation()

class onCm(commands):
    def execute(self):
        MCP2200.power(on)
        self.operation.swapColors()
        self.operation.swapButtonActivation()

class offCm(commands):
    def execute(self):
        MCP2200.power(off)
        self.operation.swapColors()
        self.operation.swapButtonActivation()

class restartPwCm(commands):
    def execute(self):
        print("restartPwCm")

class fastRestartCm(commands):
    def execute(self):
        MCP2200.power(off)
        time.sleep(1)
        MCP2200.power(on)

class reloadCm(commands):
    def execute(self):
        print("reloadCm")

class linkType:
    __buttonLinked = False
    def __init__(self, bt: button):
        self.__bt = bt

    def buttonLink(self, bt: button):
        if(self.__buttonLinked == False):
            self.__buttonLinked = True
            self.lButton = bt
            bt.link.buttonLink(self.__bt)

    def frameLink(self, frame: QtWidgets.QFrame):
        self.lFrame = frame

class button:
    def __init__(self, uiButton: QtWidgets.QPushButton, cm: commands):
        self.uiButton = uiButton
        self.cm = cm(self)
        uiButton.clicked.connect(self.cm.execute)
        self.link = linkType(self)

class RemoteApp:
    def __init__(self, ui: Ui_mainWindow):
        # Assigned Buttons
        self.ui = ui
        self.connectBt = button(ui.ConnectButton, connectCm)
        self.disconnectBt = button(ui.DisconnectButton, disconnectCm)
        self.flashBt = button(ui.FlashButton, flashCm)
        self.runBt = button(ui.RunButton, runCm)
        self.onBt = button(ui.onButton, onCm)
        self.offBt = button(ui.offButton, offCm)
        self.restartPwBt = button(ui.RestartPowerButton, restartPwCm)
        self.fastRestartBt = button(ui.FastRestart, fastRestartCm)
        self.reloadBt = button(ui.ReloadButton, reloadCm)

        # Link Buttons
        self.connectBt.link.buttonLink(self.disconnectBt)
        self.connectBt.link.frameLink(self.ui.connectedFrame)
        self.disconnectBt.link.frameLink(self.ui.disconnectFrame)
        self.flashBt.link.buttonLink(self.runBt)
        self.onBt.link.buttonLink(self.offBt)

        # workaround bug
        self.ui.connectedFrame.setEnabled(False)

if __name__ == "__main__":
    # Init the UI
    MCP2200 = usbControl()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)

    MagnaRemote = RemoteApp(ui)

    mainWindow.show()
    sys.exit(app.exec_())