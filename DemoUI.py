# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DemoUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1142, 773)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/ico.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QLabel#gra_org {\n"
"    border-style: solid;            /* 边框风格 */\n"
"    border-width: 2px;               /* 边框宽度 */\n"
"    border-color:rgb(0, 0, 0);        /* 边框颜色 */\n"
"}\n"
"QLabel#gra_wm {\n"
"    border-style: solid;            /* 边框风格 */\n"
"    border-width: 2px;               /* 边框宽度 */\n"
"    border-color:rgb(0, 0, 0);        /* 边框颜色 */\n"
"}\n"
"QLabel#gra_gen {\n"
"    border-style: solid;            /* 边框风格 */\n"
"    border-width: 2px;               /* 边框宽度 */\n"
"    border-color:rgb(0, 0, 0);        /* 边框颜色 */\n"
"}\n"
"QLabel#gra_ana {\n"
"    border-style: solid;            /* 边框风格 */\n"
"    border-width: 2px;               /* 边框宽度 */\n"
"    border-color:rgb(0, 0, 0);        /* 边框颜色 */\n"
"}\n"
"\n"
"QLabel#gra_org_2 {\n"
"    border-style: solid;            /* 边框风格 */\n"
"    border-width: 2px;               /* 边框宽度 */\n"
"    border-color:rgb(0, 0, 0);        /* 边框颜色 */\n"
"}\n"
"\n"
"QLabel#gra_gen_2 {\n"
"    border-style: solid;            /* 边框风格 */\n"
"    border-width: 2px;               /* 边框宽度 */\n"
"    border-color:rgb(0, 0, 0);        /* 边框颜色 */\n"
"}\n"
"QLabel#gra_ana_2 {\n"
"    border-style: solid;            /* 边框风格 */\n"
"    border-width: 2px;               /* 边框宽度 */\n"
"    border-color:rgb(0, 0, 0);        /* 边框颜色 */\n"
"}\n"
"QTextEdit {\n"
"    border-style: solid;            /* 边框风格 */\n"
"    border-width: 2px;               /* 边框宽度 */\n"
"    border-color:rgb(0, 0, 0);        /* 边框颜色 */\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_org = QtWidgets.QPushButton(Form)
        self.btn_org.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_org.setFont(font)
        self.btn_org.setObjectName("btn_org")
        self.horizontalLayout.addWidget(self.btn_org)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(658, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_org_2 = QtWidgets.QPushButton(Form)
        self.btn_org_2.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_org_2.setFont(font)
        self.btn_org_2.setObjectName("btn_org_2")
        self.horizontalLayout.addWidget(self.btn_org_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 4)
        self.horizontalLayout.setStretch(4, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget = Label(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(728, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setProperty("value", 30)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AI魔法消除小工具离线版V1.1（by zhaoyun007 from 52pojie.cn）"))
        self.btn_org.setText(_translate("Form", "选取图片"))
        self.pushButton.setText(_translate("Form", "打赏我"))
        self.btn_org_2.setText(_translate("Form", "涂抹完毕，点我转换"))
        self.label.setText(_translate("Form", "画笔大小"))

from label import Label

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

