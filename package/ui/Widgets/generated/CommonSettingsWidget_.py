# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\PycharmProjects\Project2023\package\ui\Widgets\ui\CommonSettingsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(153, 183)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.inputName = QtWidgets.QLineEdit(Form)
        self.inputName.setObjectName("inputName")
        self.horizontalLayout.addWidget(self.inputName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.button_color = QtWidgets.QPushButton(Form)
        self.button_color.setStyleSheet("backound-color : white")
        self.button_color.setText("")
        self.button_color.setCheckable(False)
        self.button_color.setDefault(False)
        self.button_color.setObjectName("button_color")
        self.horizontalLayout_2.addWidget(self.button_color)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.inputOpacity = QtWidgets.QLineEdit(Form)
        self.inputOpacity.setObjectName("inputOpacity")
        self.horizontalLayout_5.addWidget(self.inputOpacity)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.inputTBounds = QtWidgets.QLineEdit(Form)
        self.inputTBounds.setObjectName("inputTBounds")
        self.horizontalLayout_3.addWidget(self.inputTBounds)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.inputVBounds = QtWidgets.QLineEdit(Form)
        self.inputVBounds.setObjectName("inputVBounds")
        self.horizontalLayout_4.addWidget(self.inputVBounds)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Object settings:"))
        self.label.setText(_translate("Form", "Name:"))
        self.label_2.setText(_translate("Form", "Color:"))
        self.label_6.setText(_translate("Form", "Opacity:"))
        self.label_3.setText(_translate("Form", "t bounds:"))
        self.label_5.setText(_translate("Form", "v bounds:"))
