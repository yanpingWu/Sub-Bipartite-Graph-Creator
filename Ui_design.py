# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\shinshi\Desktop\test\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 359)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(30, 60, 340, 230))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 229))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.next = QtWidgets.QPushButton(Form)
        self.next.setGeometry(QtCore.QRect(280, 310, 93, 28))
        self.next.setObjectName("next")
        self.quite = QtWidgets.QPushButton(Form)
        self.quite.setGeometry(QtCore.QRect(30, 310, 93, 28))
        self.quite.setObjectName("quite")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GUI"))
        self.next.setText(_translate("Form", "next"))
        self.quite.setText(_translate("Form", "quite"))
        self.label.setText(_translate("Form", "Sub-bipartite graph creator"))
