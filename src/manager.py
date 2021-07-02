# Form implementation generated from reading ui file 'manager.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_manager_dialog(object):
    def setupUi(self, manager_dialog):
        manager_dialog.setObjectName("manager_dialog")
        manager_dialog.resize(504, 381)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        manager_dialog.setFont(font)
        self.label = QtWidgets.QLabel(manager_dialog)
        self.label.setGeometry(QtCore.QRect(170, 0, 151, 61))
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(manager_dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 59, 481, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_stock = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_stock.sizePolicy().hasHeightForWidth())
        self.btn_stock.setSizePolicy(sizePolicy)
        self.btn_stock.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_stock.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_stock.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_stock.setFont(font)
        self.btn_stock.setObjectName("btn_stock")
        self.gridLayout.addWidget(self.btn_stock, 1, 1, 1, 1)
        self.btn_eod = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_eod.sizePolicy().hasHeightForWidth())
        self.btn_eod.setSizePolicy(sizePolicy)
        self.btn_eod.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_eod.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_eod.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_eod.setFont(font)
        self.btn_eod.setObjectName("btn_eod")
        self.gridLayout.addWidget(self.btn_eod, 1, 2, 1, 1)
        self.btn_deposit = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_deposit.sizePolicy().hasHeightForWidth())
        self.btn_deposit.setSizePolicy(sizePolicy)
        self.btn_deposit.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_deposit.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_deposit.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_deposit.setFont(font)
        self.btn_deposit.setObjectName("btn_deposit")
        self.gridLayout.addWidget(self.btn_deposit, 0, 0, 1, 1)
        self.btn_manufacturin = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_manufacturin.sizePolicy().hasHeightForWidth())
        self.btn_manufacturin.setSizePolicy(sizePolicy)
        self.btn_manufacturin.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_manufacturin.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_manufacturin.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_manufacturin.setFont(font)
        self.btn_manufacturin.setObjectName("btn_manufacturin")
        self.gridLayout.addWidget(self.btn_manufacturin, 0, 1, 1, 1)
        self.btn_payroll = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_payroll.sizePolicy().hasHeightForWidth())
        self.btn_payroll.setSizePolicy(sizePolicy)
        self.btn_payroll.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_payroll.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_payroll.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_payroll.setFont(font)
        self.btn_payroll.setObjectName("btn_payroll")
        self.gridLayout.addWidget(self.btn_payroll, 0, 2, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.gridLayoutWidget)
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
        self.gridLayout.addWidget(self.btn_cancel, 1, 0, 1, 1)
        self.btn_employees = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_employees.sizePolicy().hasHeightForWidth())
        self.btn_employees.setSizePolicy(sizePolicy)
        self.btn_employees.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_employees.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_employees.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_employees.setFont(font)
        self.btn_employees.setObjectName("btn_employees")
        self.gridLayout.addWidget(self.btn_employees, 0, 3, 1, 1)

        self.retranslateUi(manager_dialog)
        QtCore.QMetaObject.connectSlotsByName(manager_dialog)

    def retranslateUi(self, manager_dialog):
        _translate = QtCore.QCoreApplication.translate
        manager_dialog.setWindowTitle(_translate("manager_dialog", "Manager"))
        self.label.setText(_translate("manager_dialog", "Manager"))
        self.btn_stock.setText(_translate("manager_dialog", "Stock"))
        self.btn_eod.setText(_translate("manager_dialog", "End\n"
"Of\n"
"Day"))
        self.btn_deposit.setText(_translate("manager_dialog", "Deposit"))
        self.btn_manufacturin.setText(_translate("manager_dialog", "Manufacturing"))
        self.btn_payroll.setText(_translate("manager_dialog", "Payroll"))
        self.btn_cancel.setText(_translate("manager_dialog", "Cancel"))
        self.btn_employees.setText(_translate("manager_dialog", "Employees"))
