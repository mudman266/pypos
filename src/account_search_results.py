# Form implementation generated from reading ui file 'account_search_results.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_select_account_dialog(object):
    def setupUi(self, select_account_dialog):
        select_account_dialog.setObjectName("select_account_dialog")
        select_account_dialog.resize(660, 591)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        select_account_dialog.setFont(font)
        self.label = QtWidgets.QLabel(select_account_dialog)
        self.label.setGeometry(QtCore.QRect(230, 0, 181, 71))
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(select_account_dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 80, 521, 361))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(select_account_dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 480, 641, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_select = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_select.sizePolicy().hasHeightForWidth())
        self.btn_select.setSizePolicy(sizePolicy)
        self.btn_select.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_select.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_select.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_select.setFont(font)
        self.btn_select.setObjectName("btn_select")
        self.horizontalLayout.addWidget(self.btn_select)
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
        self.verticalLayoutWidget = QtWidgets.QWidget(select_account_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(550, 80, 102, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_up = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_up.sizePolicy().hasHeightForWidth())
        self.btn_up.setSizePolicy(sizePolicy)
        self.btn_up.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_up.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_up.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_up.setFont(font)
        self.btn_up.setObjectName("btn_up")
        self.verticalLayout.addWidget(self.btn_up)
        self.btn_down = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_down.sizePolicy().hasHeightForWidth())
        self.btn_down.setSizePolicy(sizePolicy)
        self.btn_down.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_down.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_down.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_down.setFont(font)
        self.btn_down.setObjectName("btn_down")
        self.verticalLayout.addWidget(self.btn_down)

        self.retranslateUi(select_account_dialog)
        QtCore.QMetaObject.connectSlotsByName(select_account_dialog)

    def retranslateUi(self, select_account_dialog):
        _translate = QtCore.QCoreApplication.translate
        select_account_dialog.setWindowTitle(_translate("select_account_dialog", "Search Results"))
        self.label.setText(_translate("select_account_dialog", "Search Results"))
        self.btn_select.setText(_translate("select_account_dialog", "Select"))
        self.btn_cancel.setText(_translate("select_account_dialog", "Cancel"))
        self.btn_up.setText(_translate("select_account_dialog", "Up"))
        self.btn_down.setText(_translate("select_account_dialog", "Down"))
