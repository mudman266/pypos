# Form implementation generated from reading ui file 'manufacturing.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_manufacturing_dialog(object):
    def setupUi(self, manufacturing_dialog):
        manufacturing_dialog.setObjectName("manufacturing_dialog")
        manufacturing_dialog.resize(400, 369)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        manufacturing_dialog.setFont(font)
        self.label = QtWidgets.QLabel(manufacturing_dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 41))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(manufacturing_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 59, 381, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_view_orders = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_view_orders.setObjectName("btn_view_orders")
        self.verticalLayout.addWidget(self.btn_view_orders)
        self.btn_assign_work = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_assign_work.setObjectName("btn_assign_work")
        self.verticalLayout.addWidget(self.btn_assign_work)
        self.btn_check_materials = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_check_materials.setObjectName("btn_check_materials")
        self.verticalLayout.addWidget(self.btn_check_materials)
        self.btn_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.verticalLayout.addWidget(self.btn_cancel)

        self.retranslateUi(manufacturing_dialog)
        QtCore.QMetaObject.connectSlotsByName(manufacturing_dialog)

    def retranslateUi(self, manufacturing_dialog):
        _translate = QtCore.QCoreApplication.translate
        manufacturing_dialog.setWindowTitle(_translate("manufacturing_dialog", "Manufacturing"))
        self.label.setText(_translate("manufacturing_dialog", "Manufacturing"))
        self.btn_view_orders.setText(_translate("manufacturing_dialog", "View Open Orders"))
        self.btn_assign_work.setText(_translate("manufacturing_dialog", "Assign Work"))
        self.btn_check_materials.setText(_translate("manufacturing_dialog", "Check Materials"))
        self.btn_cancel.setText(_translate("manufacturing_dialog", "Cancel"))
