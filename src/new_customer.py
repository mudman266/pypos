# Form implementation generated from reading ui file 'new_customer.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_new_customer_dialog(object):
    def setupUi(self, new_customer_dialog):
        new_customer_dialog.setObjectName("new_customer_dialog")
        new_customer_dialog.resize(442, 399)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        new_customer_dialog.setFont(font)
        self.label = QtWidgets.QLabel(new_customer_dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 221, 41))
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.line_lname = QtWidgets.QLineEdit(new_customer_dialog)
        self.line_lname.setGeometry(QtCore.QRect(170, 80, 221, 31))
        self.line_lname.setObjectName("line_lname")
        self.lbl_lname = QtWidgets.QLabel(new_customer_dialog)
        self.lbl_lname.setGeometry(QtCore.QRect(20, 70, 131, 51))
        self.lbl_lname.setObjectName("lbl_lname")
        self.lbl_address = QtWidgets.QLabel(new_customer_dialog)
        self.lbl_address.setGeometry(QtCore.QRect(20, 150, 131, 51))
        self.lbl_address.setObjectName("lbl_address")
        self.lbl_fname = QtWidgets.QLabel(new_customer_dialog)
        self.lbl_fname.setGeometry(QtCore.QRect(20, 110, 141, 51))
        self.lbl_fname.setObjectName("lbl_fname")
        self.lbl_phone = QtWidgets.QLabel(new_customer_dialog)
        self.lbl_phone.setGeometry(QtCore.QRect(20, 190, 131, 51))
        self.lbl_phone.setObjectName("lbl_phone")
        self.line_phone = QtWidgets.QLineEdit(new_customer_dialog)
        self.line_phone.setGeometry(QtCore.QRect(170, 200, 221, 31))
        self.line_phone.setObjectName("line_phone")
        self.line_address = QtWidgets.QLineEdit(new_customer_dialog)
        self.line_address.setGeometry(QtCore.QRect(170, 160, 221, 31))
        self.line_address.setObjectName("line_address")
        self.line_fname = QtWidgets.QLineEdit(new_customer_dialog)
        self.line_fname.setGeometry(QtCore.QRect(170, 120, 221, 31))
        self.line_fname.setObjectName("line_fname")
        self.horizontalLayoutWidget = QtWidgets.QWidget(new_customer_dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 290, 421, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_add.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_add.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_cancel.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_cancel.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)

        self.retranslateUi(new_customer_dialog)
        QtCore.QMetaObject.connectSlotsByName(new_customer_dialog)

    def retranslateUi(self, new_customer_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_customer_dialog.setWindowTitle(_translate("new_customer_dialog", "New Cusomter"))
        self.label.setText(_translate("new_customer_dialog", "New Customer"))
        self.lbl_lname.setText(_translate("new_customer_dialog", "Last Name"))
        self.lbl_address.setText(_translate("new_customer_dialog", "Address"))
        self.lbl_fname.setText(_translate("new_customer_dialog", "First Name"))
        self.lbl_phone.setText(_translate("new_customer_dialog", "Phone"))
        self.btn_add.setText(_translate("new_customer_dialog", "Add"))
        self.btn_cancel.setText(_translate("new_customer_dialog", "Cancel"))
