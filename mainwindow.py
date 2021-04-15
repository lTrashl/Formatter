# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogMain(object):
    def setupUi(self, DialogMain):
        DialogMain.setObjectName("DialogMain")
        DialogMain.resize(900, 666)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogMain.sizePolicy().hasHeightForWidth())
        DialogMain.setSizePolicy(sizePolicy)
        DialogMain.setMinimumSize(QtCore.QSize(900, 666))
        DialogMain.setMaximumSize(QtCore.QSize(900, 666))
        self.pushButtonSaveFile = QtWidgets.QPushButton(DialogMain)
        self.pushButtonSaveFile.setGeometry(QtCore.QRect(800, 380, 101, 23))
        self.pushButtonSaveFile.setObjectName("pushButtonSaveFile")
        self.pushButtonOpenFile = QtWidgets.QPushButton(DialogMain)
        self.pushButtonOpenFile.setGeometry(QtCore.QRect(340, 380, 120, 23))
        self.pushButtonOpenFile.setObjectName("pushButtonOpenFile")
        self.pushButtonC = QtWidgets.QPushButton(DialogMain)
        self.pushButtonC.setGeometry(QtCore.QRect(10, 420, 120, 23))
        self.pushButtonC.setObjectName("pushButtonC")
        self.pushButtonPascal = QtWidgets.QPushButton(DialogMain)
        self.pushButtonPascal.setGeometry(QtCore.QRect(10, 450, 120, 23))
        self.pushButtonPascal.setObjectName("pushButtonPascal")
        self.plainTextEditSource = QtWidgets.QPlainTextEdit(DialogMain)
        self.plainTextEditSource.setGeometry(QtCore.QRect(0, 20, 461, 361))
        self.plainTextEditSource.setObjectName("plainTextEditSource")
        self.plainTextEditTarget = QtWidgets.QPlainTextEdit(DialogMain)
        self.plainTextEditTarget.setGeometry(QtCore.QRect(470, 20, 431, 361))
        self.plainTextEditTarget.setObjectName("plainTextEditTarget")
        self.plainTextEditDescription = QtWidgets.QPlainTextEdit(DialogMain)
        self.plainTextEditDescription.setGeometry(QtCore.QRect(140, 410, 321, 251))
        self.plainTextEditDescription.setObjectName("plainTextEditDescription")
        self.label = QtWidgets.QLabel(DialogMain)
        self.label.setGeometry(QtCore.QRect(140, 390, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogMain)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogMain)
        self.label_3.setGeometry(QtCore.QRect(470, 0, 191, 16))
        self.label_3.setObjectName("label_3")
        self.pushButtonFormat = QtWidgets.QPushButton(DialogMain)
        self.pushButtonFormat.setGeometry(QtCore.QRect(10, 500, 121, 23))
        self.pushButtonFormat.setObjectName("pushButtonFormat")

        self.retranslateUi(DialogMain)
        QtCore.QMetaObject.connectSlotsByName(DialogMain)

    def retranslateUi(self, DialogMain):
        _translate = QtCore.QCoreApplication.translate
        DialogMain.setWindowTitle(_translate("DialogMain", "Simple Text  Formatter"))
        self.pushButtonSaveFile.setText(_translate("DialogMain", "Сохранить"))
        self.pushButtonOpenFile.setText(_translate("DialogMain", "Загрузить"))
        self.pushButtonC.setText(_translate("DialogMain", "Это С"))
        self.pushButtonPascal.setText(_translate("DialogMain", "Это Pascal"))
        self.label.setText(_translate("DialogMain", "Правила форматирования"))
        self.label_2.setText(_translate("DialogMain", "Исходный текст"))
        self.label_3.setText(_translate("DialogMain", "Форматрированный текст"))
        self.pushButtonFormat.setText(_translate("DialogMain", "Форматировать!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogMain = QtWidgets.QDialog()
    ui = Ui_DialogMain()
    ui.setupUi(DialogMain)
    DialogMain.show()
    sys.exit(app.exec_())

