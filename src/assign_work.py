# Form implementation generated from reading ui file 'assign_work.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_assign_work_dialog(object):
    def setupUi(self, assign_work_dialog):
        assign_work_dialog.setObjectName("assign_work_dialog")
        assign_work_dialog.resize(590, 506)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        assign_work_dialog.setFont(font)
        self.label = QtWidgets.QLabel(assign_work_dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 571, 61))
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(assign_work_dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 70, 571, 192))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(assign_work_dialog)
        self.tableView_2.setGeometry(QtCore.QRect(10, 280, 571, 91))
        self.tableView_2.setObjectName("tableView_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(assign_work_dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 380, 571, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_assign = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_assign.sizePolicy().hasHeightForWidth())
        self.btn_assign.setSizePolicy(sizePolicy)
        self.btn_assign.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_assign.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_assign.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_assign.setFont(font)
        self.btn_assign.setObjectName("btn_assign")
        self.horizontalLayout.addWidget(self.btn_assign)
        self.btn_unassign = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btn_unassign.sizePolicy().hasHeightForWidth())
        self.btn_unassign.setSizePolicy(sizePolicy)
        self.btn_unassign.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_unassign.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_unassign.setBaseSize(QtCore.QSize(12, 2))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.btn_unassign.setFont(font)
        self.btn_unassign.setObjectName("btn_unassign")
        self.horizontalLayout.addWidget(self.btn_unassign)
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

        self.retranslateUi(assign_work_dialog)
        QtCore.QMetaObject.connectSlotsByName(assign_work_dialog)

    def retranslateUi(self, assign_work_dialog):
        _translate = QtCore.QCoreApplication.translate
        assign_work_dialog.setWindowTitle(_translate("assign_work_dialog", "Assign Word"))
        self.label.setText(_translate("assign_work_dialog", "Assign Work"))
        self.btn_assign.setText(_translate("assign_work_dialog", "Assign"))
        self.btn_unassign.setText(_translate("assign_work_dialog", "Unassign"))
        self.btn_cancel.setText(_translate("assign_work_dialog", "Cancel"))