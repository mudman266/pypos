# Form implementation generated from reading ui file 'bottoms.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 772)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 0, 641, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 620, 1081, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.btn_discount = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_discount.sizePolicy().hasHeightForWidth())
        self.btn_discount.setSizePolicy(sizePolicy)
        self.btn_discount.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_discount.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_discount.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_discount.setFont(font)
        self.btn_discount.setObjectName("btn_discount")
        self.horizontalLayout.addWidget(self.btn_discount)
        self.btn_settle = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_settle.sizePolicy().hasHeightForWidth())
        self.btn_settle.setSizePolicy(sizePolicy)
        self.btn_settle.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_settle.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_settle.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_settle.setFont(font)
        self.btn_settle.setObjectName("btn_settle")
        self.horizontalLayout.addWidget(self.btn_settle)
        self.btn_cust_lookup = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_cust_lookup.sizePolicy().hasHeightForWidth())
        self.btn_cust_lookup.setSizePolicy(sizePolicy)
        self.btn_cust_lookup.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_cust_lookup.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_cust_lookup.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_cust_lookup.setFont(font)
        self.btn_cust_lookup.setObjectName("btn_cust_lookup")
        self.horizontalLayout.addWidget(self.btn_cust_lookup)
        self.btn_manage_acct = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_manage_acct.sizePolicy().hasHeightForWidth())
        self.btn_manage_acct.setSizePolicy(sizePolicy)
        self.btn_manage_acct.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_manage_acct.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_manage_acct.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(17)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_manage_acct.setFont(font)
        self.btn_manage_acct.setObjectName("btn_manage_acct")
        self.horizontalLayout.addWidget(self.btn_manage_acct)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 121, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_tops = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(16)
        self.btn_tops.setFont(font)
        self.btn_tops.setObjectName("btn_tops")
        self.verticalLayout.addWidget(self.btn_tops)
        self.btn_bottoms = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(16)
        self.btn_bottoms.setFont(font)
        self.btn_bottoms.setObjectName("btn_bottoms")
        self.verticalLayout.addWidget(self.btn_bottoms)
        self.btn_ties = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(16)
        self.btn_ties.setFont(font)
        self.btn_ties.setObjectName("btn_ties")
        self.verticalLayout.addWidget(self.btn_ties)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_discount.setText(_translate("MainWindow", "Discount"))
        self.btn_settle.setText(_translate("MainWindow", "Settle"))
        self.btn_cust_lookup.setText(_translate("MainWindow", "Customer\n"
"Lookup"))
        self.btn_manage_acct.setText(_translate("MainWindow", "Manage\n"
"Account"))
        self.btn_tops.setText(_translate("MainWindow", "Tops"))
        self.btn_bottoms.setText(_translate("MainWindow", "Bottoms"))
        self.btn_ties.setText(_translate("MainWindow", "Ties"))
