# Form implementation generated from reading ui file 'FIRST.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 390, 420, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_timeclock = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_timeclock.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_timeclock.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_timeclock.setFont(font)
        self.btn_timeclock.setObjectName("btn_timeclock")
        self.gridLayout.addWidget(self.btn_timeclock, 0, 2, 1, 1)
        self.btn_begin = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_begin.sizePolicy().hasHeightForWidth())
        self.btn_begin.setSizePolicy(sizePolicy)
        self.btn_begin.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_begin.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_begin.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_begin.setFont(font)
        self.btn_begin.setObjectName("btn_begin")
        self.gridLayout.addWidget(self.btn_begin, 0, 1, 1, 1)
        self.btn_quit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_quit.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_quit.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        self.btn_quit.setFont(font)
        self.btn_quit.setObjectName("btn_quit")
        self.gridLayout.addWidget(self.btn_quit, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Begin"))
        self.btn_timeclock.setText(_translate("MainWindow", "Time\n"
"Clock"))
        self.btn_begin.setText(_translate("MainWindow", "Begin"))
        self.btn_quit.setText(_translate("MainWindow", "Quit"))
