# Form implementation generated from reading ui file 'password_entry.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(665, 510)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        Dialog.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 100, 411, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_1.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_7.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_9.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_3.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_4.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_8.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_2.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_5.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_6.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_0.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)
        self.btn_backspace = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_backspace.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_backspace.setFont(font)
        self.btn_backspace.setObjectName("btn_backspace")
        self.gridLayout.addWidget(self.btn_backspace, 3, 0, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_ok.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(28)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 3, 2, 1, 1)
        self.lbl_pass_input = QtWidgets.QLabel(Dialog)
        self.lbl_pass_input.setGeometry(QtCore.QRect(220, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.lbl_pass_input.setFont(font)
        self.lbl_pass_input.setStyleSheet("background: rgb(255, 255, 255);")
        self.lbl_pass_input.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lbl_pass_input.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.lbl_pass_input.setLineWidth(2)
        self.lbl_pass_input.setObjectName("lbl_pass_input")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Enter Passcode"))
        self.btn_1.setText(_translate("Dialog", "1"))
        self.btn_7.setText(_translate("Dialog", "7"))
        self.btn_9.setText(_translate("Dialog", "9"))
        self.btn_3.setText(_translate("Dialog", "3"))
        self.btn_4.setText(_translate("Dialog", "4"))
        self.btn_8.setText(_translate("Dialog", "8"))
        self.btn_2.setText(_translate("Dialog", "2"))
        self.btn_5.setText(_translate("Dialog", "5"))
        self.btn_6.setText(_translate("Dialog", "6"))
        self.btn_0.setText(_translate("Dialog", "0"))
        self.btn_backspace.setText(_translate("Dialog", "<-"))
        self.btn_ok.setText(_translate("Dialog", "OK"))
        self.lbl_pass_input.setText(_translate("Dialog", "Enter Password"))