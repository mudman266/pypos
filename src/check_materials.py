# Form implementation generated from reading ui file 'check_materials.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_check_materials_dialog(object):
    def setupUi(self, check_materials_dialog):
        check_materials_dialog.setObjectName("check_materials_dialog")
        check_materials_dialog.resize(400, 371)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        check_materials_dialog.setFont(font)
        self.label = QtWidgets.QLabel(check_materials_dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 51))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(check_materials_dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 40, 381, 192))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(check_materials_dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 250, 381, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy)
        self.btn_ok.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_ok.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_ok.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)

        self.retranslateUi(check_materials_dialog)
        QtCore.QMetaObject.connectSlotsByName(check_materials_dialog)

    def retranslateUi(self, check_materials_dialog):
        _translate = QtCore.QCoreApplication.translate
        check_materials_dialog.setWindowTitle(_translate("check_materials_dialog", "Check Materials"))
        self.label.setText(_translate("check_materials_dialog", "Check Materials"))
        self.btn_ok.setText(_translate("check_materials_dialog", "OK"))
