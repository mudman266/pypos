# Form implementation generated from reading ui file 'commission.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_commission_dialog(object):
    def setupUi(self, commission_dialog):
        commission_dialog.setObjectName("commission_dialog")
        commission_dialog.resize(889, 614)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        commission_dialog.setFont(font)
        self.lbl_salesperson = QtWidgets.QLabel(commission_dialog)
        self.lbl_salesperson.setGeometry(QtCore.QRect(20, 70, 431, 41))
        self.lbl_salesperson.setObjectName("lbl_salesperson")
        self.label_2 = QtWidgets.QLabel(commission_dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 881, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lbl_report_date = QtWidgets.QLabel(commission_dialog)
        self.lbl_report_date.setGeometry(QtCore.QRect(470, 60, 401, 41))
        self.lbl_report_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_report_date.setObjectName("lbl_report_date")
        self.tableWidget = QtWidgets.QTableWidget(commission_dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 130, 841, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lbl_total_retail = QtWidgets.QLabel(commission_dialog)
        self.lbl_total_retail.setGeometry(QtCore.QRect(340, 450, 501, 41))
        self.lbl_total_retail.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_total_retail.setObjectName("lbl_total_retail")
        self.lbl_total_commission = QtWidgets.QLabel(commission_dialog)
        self.lbl_total_commission.setGeometry(QtCore.QRect(330, 490, 511, 41))
        self.lbl_total_commission.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_total_commission.setObjectName("lbl_total_commission")
        self.btn_ok = QtWidgets.QPushButton(commission_dialog)
        self.btn_ok.setGeometry(QtCore.QRect(330, 540, 211, 61))
        self.btn_ok.setObjectName("btn_ok")

        self.retranslateUi(commission_dialog)
        QtCore.QMetaObject.connectSlotsByName(commission_dialog)

    def retranslateUi(self, commission_dialog):
        _translate = QtCore.QCoreApplication.translate
        commission_dialog.setWindowTitle(_translate("commission_dialog", "Commission Statement"))
        self.lbl_salesperson.setText(_translate("commission_dialog", "Salesperson:"))
        self.label_2.setText(_translate("commission_dialog", "Commission Statement"))
        self.lbl_report_date.setText(_translate("commission_dialog", "Report Date:"))
        self.lbl_total_retail.setText(_translate("commission_dialog", "Total Reatil:"))
        self.lbl_total_commission.setText(_translate("commission_dialog", "Total Commission:"))
        self.btn_ok.setText(_translate("commission_dialog", "OK"))
