# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'landing.ui'
#
# Created: Sat Oct 31 22:41:11 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1189, 765)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"    background-image: url(:/prefix/Pictures/launcher.jpg);\n"
"}\n"
"QGroupBox{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 63 24pt \"Ubuntu\";\n"
"}\n"
"QPushButton{\n"
"    color: rgb(0,0,0);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 611, 71))
        self.label.setStyleSheet(_fromUtf8("font: 75 36pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(880, 370, 251, 211))
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.module1 = QtGui.QPushButton(self.groupBox)
        self.module1.setGeometry(QtCore.QRect(20, 70, 201, 41))
        self.module1.setObjectName(_fromUtf8("module1"))
        self.module2 = QtGui.QPushButton(self.groupBox)
        self.module2.setGeometry(QtCore.QRect(20, 120, 201, 41))
        self.module2.setObjectName(_fromUtf8("module2"))
        self.module3 = QtGui.QPushButton(self.groupBox)
        self.module3.setGeometry(QtCore.QRect(20, 170, 201, 41))
        self.module3.setObjectName(_fromUtf8("module3"))
        self.logout = QtGui.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1060, 710, 111, 41))
        self.logout.setObjectName(_fromUtf8("logout"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Welcome User", None))
        self.groupBox.setTitle(_translate("MainWindow", "Choose Mode", None))
        self.module1.setText(_translate("MainWindow", "Geuss Word", None))
        self.module2.setText(_translate("MainWindow", "Guess Meaning", None))
        self.module3.setText(_translate("MainWindow", "Form Word", None))
        self.logout.setText(_translate("MainWindow", "Logout", None))

import rs1

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

