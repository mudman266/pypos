# Form implementation generated from reading ui file 'employee_setup.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_employee_setup(object):
    def setupUi(self, employee_setup):
        employee_setup.setObjectName("employee_setup")
        employee_setup.resize(756, 733)
        self.verticalLayoutWidget = QtWidgets.QWidget(employee_setup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 109, 231, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbl_employees = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tbl_employees.setColumnCount(2)
        self.tbl_employees.setObjectName("tbl_employees")
        self.tbl_employees.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_employees)
        self.label = QtWidgets.QLabel(employee_setup)
        self.label.setGeometry(QtCore.QRect(10, 10, 741, 31))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(employee_setup)
        self.formLayoutWidget.setGeometry(QtCore.QRect(260, 110, 461, 411))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_fname = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_fname.setFont(font)
        self.lbl_fname.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lbl_fname.setObjectName("lbl_fname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_fname)
        self.txt_fname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.txt_fname.setFont(font)
        self.txt_fname.setObjectName("txt_fname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_fname)
        self.lbl_lname = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_lname.setFont(font)
        self.lbl_lname.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lbl_lname.setObjectName("lbl_lname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_lname)
        self.txt_lname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.txt_lname.setFont(font)
        self.txt_lname.setObjectName("txt_lname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_lname)
        self.lbl_disp_name = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_disp_name.setFont(font)
        self.lbl_disp_name.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lbl_disp_name.setObjectName("lbl_disp_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_disp_name)
        self.txt_disp_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.txt_disp_name.setFont(font)
        self.txt_disp_name.setObjectName("txt_disp_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_disp_name)
        self.lbl_job_class = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_job_class.setFont(font)
        self.lbl_job_class.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lbl_job_class.setObjectName("lbl_job_class")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_job_class)
        self.txt_job_class = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.txt_job_class.setFont(font)
        self.txt_job_class.setObjectName("txt_job_class")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_job_class)
        self.lbl_active = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_active.setFont(font)
        self.lbl_active.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lbl_active.setObjectName("lbl_active")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_active)
        self.chk_active = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chk_active.setFont(font)
        self.chk_active.setText("")
        self.chk_active.setObjectName("chk_active")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.chk_active)
        self.lbl_pass_code = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_pass_code.setFont(font)
        self.lbl_pass_code.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lbl_pass_code.setObjectName("lbl_pass_code")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_pass_code)
        self.txt_passcode = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.txt_passcode.setFont(font)
        self.txt_passcode.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txt_passcode.setObjectName("txt_passcode")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_passcode)
        self.lbl_social = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_social.setFont(font)
        self.lbl_social.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lbl_social.setObjectName("lbl_social")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_social)
        self.txt_social = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.txt_social.setFont(font)
        self.txt_social.setObjectName("txt_social")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_social)
        self.lbl_salaried = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_salaried.setFont(font)
        self.lbl_salaried.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lbl_salaried.setObjectName("lbl_salaried")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_salaried)
        self.chk_salaried = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chk_salaried.setFont(font)
        self.chk_salaried.setText("")
        self.chk_salaried.setObjectName("chk_salaried")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.chk_salaried)
        self.lbl_pay_rate = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_pay_rate.setFont(font)
        self.lbl_pay_rate.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lbl_pay_rate.setObjectName("lbl_pay_rate")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_pay_rate)
        self.txt_pay_rate = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.txt_pay_rate.setFont(font)
        self.txt_pay_rate.setObjectName("txt_pay_rate")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_pay_rate)
        self.btn_cancel = QtWidgets.QPushButton(employee_setup)
        self.btn_cancel.setGeometry(QtCore.QRect(530, 610, 100, 100))
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
        self.btn_ok = QtWidgets.QPushButton(employee_setup)
        self.btn_ok.setGeometry(QtCore.QRect(310, 610, 100, 100))
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

        self.retranslateUi(employee_setup)
        QtCore.QMetaObject.connectSlotsByName(employee_setup)

    def retranslateUi(self, employee_setup):
        _translate = QtCore.QCoreApplication.translate
        employee_setup.setWindowTitle(_translate("employee_setup", "Dialog"))
        self.label.setText(_translate("employee_setup", "Employee Setup"))
        self.lbl_fname.setText(_translate("employee_setup", "First Name"))
        self.lbl_lname.setText(_translate("employee_setup", "Last Name"))
        self.lbl_disp_name.setText(_translate("employee_setup", "Display Name"))
        self.lbl_job_class.setText(_translate("employee_setup", "Job Class"))
        self.lbl_active.setText(_translate("employee_setup", "Active"))
        self.lbl_pass_code.setText(_translate("employee_setup", "Passcode"))
        self.lbl_social.setText(_translate("employee_setup", "Social Security #"))
        self.lbl_salaried.setText(_translate("employee_setup", "Salaried"))
        self.lbl_pay_rate.setText(_translate("employee_setup", "Pay Rate"))
        self.btn_cancel.setText(_translate("employee_setup", "Cancel"))
        self.btn_ok.setText(_translate("employee_setup", "OK"))
