from __future__ import annotations
import sys
from remote_UI import Ui_mainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ctypes import*
import time
import configparser

on = 1
off = 0

class iniReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("remote.ini")
    
    def readSeconds(self):
        return int(self.config["DEFAULT"]["Seconds"])

    def writeSeconds(self, seconds: str):
        if(seconds != self.config["DEFAULT"]["Seconds"]):
            self.config["DEFAULT"]["Seconds"] = seconds
            with open("remote.ini", "w") as configfile:
                self.config.write(configfile)

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

    def flash_mode(self):
        self.__pinStatus &= ~self.__ECU_pins
        self.__write()

    def run_mode(self):
        self.__pinStatus |= self.__ECU_pins
        self.__write()

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
    def __init__(self, bt):
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
        self.bt.link.powerOffBt.cm.execute()
        MCP2200.flash_mode()
        time.sleep(1)
        self.bt.link.powerOnBt.cm.execute()

        self.operation.swapColors()
        self.operation.swapButtonActivation()

class runCm(commands):
    def execute(self):
        self.bt.link.powerOffBt.cm.execute()
        MCP2200.run_mode()
        time.sleep(1)
        self.bt.link.powerOnBt.cm.execute()

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
        self.bt.link.powerOffBt.cm.execute()
        time.sleep(self.bt.link.uiTextBox.seconds)
        self.bt.link.powerOnBt.cm.execute()

class fastRestartCm(commands):
    def execute(self):
        self.bt.link.powerOffBt.cm.execute()
        time.sleep(1)
        self.bt.link.powerOnBt.cm.execute()
    
class iniSaveCm(commands):
    def execute(self):
        try:
            self.bt.seconds = int(self.bt.uiTextEdit.toPlainText())
            self.bt.iniR.writeSeconds(str(self.bt.seconds))

        except ValueError:
            pass

class linkType:
    __buttonLinked = False
    def __init__(self, bt: button):
        self.__bt = bt

    """ Also link viseversa """
    def buttonLink(self, bt: button):
        if(self.__buttonLinked == False):
            self.__buttonLinked = True
            self.lButton = bt
            bt.link.buttonLink(self.__bt)

    """ Link of a frame """
    def frameLink(self, frame: QtWidgets.QFrame):
        self.lFrame = frame

    """ Link for powerbuttons """
    def powerLink(self, powerOnBt: button, powerOffBt: button):
        self.powerOnBt = powerOnBt
        self.powerOffBt = powerOffBt

    """ TextBox Link """
    def textBoxLink(self, uiTextBox: editBox):
        self.uiTextBox = uiTextBox

class button:
    def __init__(self, uiButton: QtWidgets.QPushButton, cm: commands):
        self.uiButton = uiButton
        self.cm = cm(self)
        self.uiButton.clicked.connect(self.cm.execute)
        self.link = linkType(self)

class editBox:
    def __init__(self, uiTextEdit: QtWidgets.QTextEdit, cm: commands):
        self.uiTextEdit = uiTextEdit
        self.cm = cm(self)
        self.iniR = iniReader()
        self.seconds = self.iniR.readSeconds()
        self.uiTextEdit.setPlainText(str(self.seconds))
        self.uiTextEdit.textChanged.connect(self.cm.execute)

class RemoteApp:
    def __init__(self, ui: Ui_mainWindow):
        """ Assigned Buttons """
        self.ui = ui
        self.connectBt = button(ui.ConnectButton, connectCm)
        self.disconnectBt = button(ui.DisconnectButton, disconnectCm)
        self.flashBt = button(ui.FlashButton, flashCm)
        self.runBt = button(ui.RunButton, runCm)
        self.onBt = button(ui.onButton, onCm)
        self.offBt = button(ui.offButton, offCm)
        self.restartPwBt = button(ui.RestartPowerButton, restartPwCm)
        self.fastRestartBt = button(ui.FastRestart, fastRestartCm)
        self.uiEditBox = editBox(ui.DelayValue, iniSaveCm)

        """ Link Buttons """
        self.connectBt.link.buttonLink(self.disconnectBt)
        self.connectBt.link.frameLink(self.ui.connectedFrame)
        self.disconnectBt.link.frameLink(self.ui.disconnectFrame)
        self.flashBt.link.buttonLink(self.runBt)
        self.onBt.link.buttonLink(self.offBt)

        """ Power button link """
        self.flashBt.link.powerLink(self.onBt, self.offBt)
        self.runBt.link.powerLink(self.onBt, self.offBt)
        self.restartPwBt.link.powerLink(self.onBt, self.offBt)
        self.fastRestartBt.link.powerLink(self.onBt, self.offBt)

        """ EditBox link """
        self.restartPwBt.link.textBoxLink(self.uiEditBox)

        """ workaround bug """
        self.ui.connectedFrame.setEnabled(False)

if __name__ == "__main__":
    """ Init the UI """
    MCP2200 = usbControl()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)

    MagnaRemote = RemoteApp(ui)

    mainWindow.show()
    sys.exit(app.exec_())