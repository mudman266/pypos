# Form implementation generated from reading ui file 'receipt.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_receipt(object):
    def setupUi(self, receipt):
        receipt.setObjectName("receipt")
        receipt.resize(401, 506)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        receipt.setFont(font)
        self.label = QtWidgets.QLabel(receipt)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 41))
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(receipt)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 401, 41))
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(receipt)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 401, 31))
        self.label_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.items_table = QtWidgets.QTableWidget(receipt)
        self.items_table.setGeometry(QtCore.QRect(5, 120, 391, 192))
        self.items_table.setObjectName("items_table")
        self.items_table.setColumnCount(0)
        self.items_table.setRowCount(0)
        self.lbl_tax = QtWidgets.QLabel(receipt)
        self.lbl_tax.setGeometry(QtCore.QRect(130, 350, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        self.lbl_tax.setFont(font)
        self.lbl_tax.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.lbl_tax.setObjectName("lbl_tax")
        self.lbl_total_amt = QtWidgets.QLabel(receipt)
        self.lbl_total_amt.setGeometry(QtCore.QRect(280, 380, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        self.lbl_total_amt.setFont(font)
        self.lbl_total_amt.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.lbl_total_amt.setObjectName("lbl_total_amt")
        self.lbl_tax_amt = QtWidgets.QLabel(receipt)
        self.lbl_tax_amt.setGeometry(QtCore.QRect(280, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        self.lbl_tax_amt.setFont(font)
        self.lbl_tax_amt.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.lbl_tax_amt.setObjectName("lbl_tax_amt")
        self.lbl_subtotal = QtWidgets.QLabel(receipt)
        self.lbl_subtotal.setGeometry(QtCore.QRect(130, 320, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        self.lbl_subtotal.setFont(font)
        self.lbl_subtotal.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.lbl_subtotal.setObjectName("lbl_subtotal")
        self.lbl_subtotal_amt = QtWidgets.QLabel(receipt)
        self.lbl_subtotal_amt.setGeometry(QtCore.QRect(280, 320, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        self.lbl_subtotal_amt.setFont(font)
        self.lbl_subtotal_amt.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.lbl_subtotal_amt.setObjectName("lbl_subtotal_amt")
        self.lbl_total = QtWidgets.QLabel(receipt)
        self.lbl_total.setGeometry(QtCore.QRect(130, 380, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        self.lbl_total.setFont(font)
        self.lbl_total.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.lbl_total.setObjectName("lbl_total")
        self.btn_done = QtWidgets.QPushButton(receipt)
        self.btn_done.setGeometry(QtCore.QRect(110, 430, 161, 61))
        self.btn_done.setObjectName("btn_done")

        self.retranslateUi(receipt)
        QtCore.QMetaObject.connectSlotsByName(receipt)

    def retranslateUi(self, receipt):
        _translate = QtCore.QCoreApplication.translate
        receipt.setWindowTitle(_translate("receipt", "Customer Receipt"))
        self.label.setText(_translate("receipt", "Larry\'s Sartorial Shoppe"))
        self.label_2.setText(_translate("receipt", "Register: 1"))
        self.label_3.setText(_translate("receipt", "Date:"))
        self.lbl_tax.setText(_translate("receipt", "Tax:"))
        self.lbl_total_amt.setText(_translate("receipt", "0.00"))
        self.lbl_tax_amt.setText(_translate("receipt", "0.00"))
        self.lbl_subtotal.setText(_translate("receipt", "Subtotal:"))
        self.lbl_subtotal_amt.setText(_translate("receipt", "0.00"))
        self.lbl_total.setText(_translate("receipt", "Total:"))
        self.btn_done.setText(_translate("receipt", "Done"))
