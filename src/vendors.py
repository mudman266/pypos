# Form implementation generated from reading ui file 'vendors.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_vendors_dialog(object):
    def setupUi(self, vendors_dialog):
        vendors_dialog.setObjectName("vendors_dialog")
        vendors_dialog.resize(395, 417)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        vendors_dialog.setFont(font)
        self.label = QtWidgets.QLabel(vendors_dialog)
        self.label.setGeometry(QtCore.QRect(115, 29, 151, 31))
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(vendors_dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(15, 299, 361, 102))
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
        self.btn_edit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.btn_edit.setSizePolicy(sizePolicy)
        self.btn_edit.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_edit.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_edit.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_edit.setFont(font)
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
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
        self.tableView = QtWidgets.QTableView(vendors_dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 70, 371, 211))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(vendors_dialog)
        QtCore.QMetaObject.connectSlotsByName(vendors_dialog)

    def retranslateUi(self, vendors_dialog):
        _translate = QtCore.QCoreApplication.translate
        vendors_dialog.setWindowTitle(_translate("vendors_dialog", "Vendors"))
        self.label.setText(_translate("vendors_dialog", "Vendors"))
        self.btn_add.setText(_translate("vendors_dialog", "Add"))
        self.btn_edit.setText(_translate("vendors_dialog", "Edit"))
        self.btn_cancel.setText(_translate("vendors_dialog", "Cancel"))
