# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(622, 501)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 100, 451, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LabelZhuhe = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.LabelZhuhe.setFont(font)
        self.LabelZhuhe.setObjectName("LabelZhuhe")
        self.gridLayout.addWidget(self.LabelZhuhe, 2, 0, 1, 1)
        self.LabelValue = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.LabelValue.setFont(font)
        self.LabelValue.setObjectName("LabelValue")
        self.gridLayout.addWidget(self.LabelValue, 3, 0, 1, 1)
        self.number = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.number.setFont(font)
        self.number.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number.setText("")
        self.number.setAlignment(QtCore.Qt.AlignCenter)
        self.number.setReadOnly(True)
        self.number.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.number.setObjectName("number")
        self.gridLayout.addWidget(self.number, 2, 2, 1, 1)
        self.maxvalue = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.maxvalue.setFont(font)
        self.maxvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.maxvalue.setReadOnly(True)
        self.maxvalue.setObjectName("maxvalue")
        self.gridLayout.addWidget(self.maxvalue, 3, 2, 1, 1)
        self.LabelWay = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.LabelWay.setFont(font)
        self.LabelWay.setObjectName("LabelWay")
        self.gridLayout.addWidget(self.LabelWay, 1, 0, 1, 1)
        self.way = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.way.setFont(font)
        self.way.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.way.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.way.setText("")
        self.way.setAlignment(QtCore.Qt.AlignCenter)
        self.way.setReadOnly(True)
        self.way.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.way.setObjectName("way")
        self.gridLayout.addWidget(self.way, 1, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 370, 451, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonQ = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonQ.setFont(font)
        self.pushButtonQ.setCheckable(True)
        self.pushButtonQ.setAutoExclusive(True)
        self.pushButtonQ.setObjectName("pushButtonQ")
        self.horizontalLayout.addWidget(self.pushButtonQ)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButtonD = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonD.setFont(font)
        self.pushButtonD.setCheckable(True)
        self.pushButtonD.setAutoExclusive(True)
        self.pushButtonD.setObjectName("pushButtonD")
        self.horizontalLayout.addWidget(self.pushButtonD)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 20, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.pushButtonQ.clicked.connect(Form.calculate_q)
        self.pushButtonD.clicked.connect(Form.calculate_d)
        self.pushButton.clicked.connect(Form.clear_all)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "????????????????????????Wu Dingwei"))
        self.LabelZhuhe.setText(_translate("Form", "??????-???????????????"))
        self.LabelValue.setText(_translate("Form", "??????-???????????????"))
        self.number.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.LabelWay.setText(_translate("Form", "     ???????????????"))
        self.way.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButtonQ.setText(_translate("Form", "?????????"))
        self.pushButton.setText(_translate("Form", "??????"))
        self.pushButtonD.setText(_translate("Form", "????????????"))
        self.label.setText(_translate("Form", "??????????????????"))

