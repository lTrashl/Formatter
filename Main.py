#-*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
from PyQt5.QtWidgets import QTableWidgetItem #для работы с таблицей
from usemainwindow import useMainWindow
from unittest import unitTest

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = useMainWindow()
ui.setupUi(MainWindow)
ui.SetMainActions(app)

print(sys.argv)

if len(sys.argv) > 1: #это самотестирование!
    test = unitTest()
    test.run(ui)
else:
    MainWindow.show()
    print("starting")
    code = app.exec_()
    sys.exit(code)
