# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RemoteUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(451, 345)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connectedFrame = QtWidgets.QFrame(self.centralwidget)
        self.connectedFrame.setEnabled(True)
        self.connectedFrame.setGeometry(QtCore.QRect(0, 60, 450, 281))
        self.connectedFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.connectedFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.connectedFrame.setObjectName("connectedFrame")
        self.DebugBordButtons = QtWidgets.QGroupBox(self.connectedFrame)
        self.DebugBordButtons.setEnabled(True)
        self.DebugBordButtons.setGeometry(QtCore.QRect(-1, 60, 450, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DebugBordButtons.setFont(font)
        self.DebugBordButtons.setAlignment(QtCore.Qt.AlignCenter)
        self.DebugBordButtons.setFlat(False)
        self.DebugBordButtons.setCheckable(False)
        self.DebugBordButtons.setObjectName("DebugBordButtons")
        self.FlashButton = QtWidgets.QPushButton(self.DebugBordButtons)
        self.FlashButton.setEnabled(False)
        self.FlashButton.setGeometry(QtCore.QRect(37, 35, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.FlashButton.setFont(font)
        self.FlashButton.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.FlashButton.setObjectName("FlashButton")
        self.RunButton = QtWidgets.QPushButton(self.DebugBordButtons)
        self.RunButton.setEnabled(True)
        self.RunButton.setGeometry(QtCore.QRect(262, 35, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RunButton.setFont(font)
        self.RunButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.RunButton.setObjectName("RunButton")
        self.PowerOptions = QtWidgets.QGroupBox(self.connectedFrame)
        self.PowerOptions.setGeometry(QtCore.QRect(-1, 170, 450, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PowerOptions.setFont(font)
        self.PowerOptions.setAlignment(QtCore.Qt.AlignCenter)
        self.PowerOptions.setFlat(False)
        self.PowerOptions.setCheckable(False)
        self.PowerOptions.setObjectName("PowerOptions")
        self.RestartPowerButton = QtWidgets.QPushButton(self.PowerOptions)
        self.RestartPowerButton.setGeometry(QtCore.QRect(290, 60, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RestartPowerButton.setFont(font)
        self.RestartPowerButton.setObjectName("RestartPowerButton")
        self.DelayValue = QtWidgets.QTextEdit(self.PowerOptions)
        self.DelayValue.setGeometry(QtCore.QRect(400, 30, 30, 20))
        self.DelayValue.setAcceptDrops(True)
        self.DelayValue.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DelayValue.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DelayValue.setObjectName("DelayValue")
        self.DelaySeconds = QtWidgets.QLabel(self.PowerOptions)
        self.DelaySeconds.setGeometry(QtCore.QRect(300, 30, 78, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DelaySeconds.setFont(font)
        self.DelaySeconds.setObjectName("DelaySeconds")
        self.offButton = QtWidgets.QPushButton(self.PowerOptions)
        self.offButton.setEnabled(False)
        self.offButton.setGeometry(QtCore.QRect(33, 62, 81, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.offButton.setFont(font)
        self.offButton.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.offButton.setObjectName("offButton")
        self.onButton = QtWidgets.QPushButton(self.PowerOptions)
        self.onButton.setGeometry(QtCore.QRect(33, 17, 81, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.onButton.setFont(font)
        self.onButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.onButton.setObjectName("onButton")
        self.FastRestart = QtWidgets.QPushButton(self.PowerOptions)
        self.FastRestart.setGeometry(QtCore.QRect(177, 30, 90, 72))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.FastRestart.setFont(font)
        self.FastRestart.setObjectName("FastRestart")
        self.DisconnectButton = QtWidgets.QPushButton(self.connectedFrame)
        self.DisconnectButton.setGeometry(QtCore.QRect(150, 1, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DisconnectButton.setFont(font)
        self.DisconnectButton.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.DisconnectButton.setObjectName("DisconnectButton")
        self.disconnectFrame = QtWidgets.QFrame(self.centralwidget)
        self.disconnectFrame.setGeometry(QtCore.QRect(0, 0, 450, 61))
        self.disconnectFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.disconnectFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.disconnectFrame.setObjectName("disconnectFrame")
        self.ConnectButton = QtWidgets.QPushButton(self.disconnectFrame)
        self.ConnectButton.setGeometry(QtCore.QRect(150, 20, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ConnectButton.setFont(font)
        self.ConnectButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.ConnectButton.setObjectName("ConnectButton")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.DelayValue, self.RestartPowerButton)
        mainWindow.setTabOrder(self.RestartPowerButton, self.FastRestart)
        mainWindow.setTabOrder(self.FastRestart, self.onButton)
        mainWindow.setTabOrder(self.onButton, self.offButton)
        mainWindow.setTabOrder(self.offButton, self.FlashButton)
        mainWindow.setTabOrder(self.FlashButton, self.RunButton)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.DebugBordButtons.setTitle(_translate("mainWindow", "Debug Bord Buttons"))
        self.FlashButton.setText(_translate("mainWindow", "Flash"))
        self.RunButton.setText(_translate("mainWindow", "Run"))
        self.PowerOptions.setTitle(_translate("mainWindow", "Power Options"))
        self.RestartPowerButton.setText(_translate("mainWindow", "Restart Power"))
        self.DelaySeconds.setText(_translate("mainWindow", "Delay (s)"))
        self.offButton.setText(_translate("mainWindow", "OFF"))
        self.onButton.setText(_translate("mainWindow", "ON"))
        self.FastRestart.setText(_translate("mainWindow", "Fast\n"
"Restart"))
        self.DisconnectButton.setText(_translate("mainWindow", "Disconnect"))
        self.ConnectButton.setText(_translate("mainWindow", "Connect"))
