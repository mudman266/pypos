# Josh Williams
# PyPOS

# Import all the windows
from FIRST import Ui_MainWindow
from begin import Ui_BeginWindow
from password_entry import Ui_Dialog
from make_sale import Ui_SaleWindow
from discount_selection import Ui_discount_check_dialog
from discount_percent_entry import Ui_discount_percent_dialog
from discount_amount_entry import Ui_discount_amount_dialog
from settle import Ui_settle_window
from customer_lookup import Ui_customer_lookup_dialog
from new_customer import Ui_new_customer_dialog
from account_search_results import Ui_select_account_dialog
from enter_amount import Ui_payment_amount_dialog
from manage_account import Ui_manage_account_dialog
from select_employee import Ui_time_clock_dialog
from manager import Ui_manager_dialog
from stock import Ui_stock_dialog
from groups import Ui_groups_dialog
from vendors import Ui_vendors_dialog
from add_item import Ui_add_item_dialog
from edit_employee import Ui_edit_employee_dialog
from edit_item import Ui_edit_item_dialog
from inventory_count import Ui_count_dialog
from payroll import Ui_payroll_dialog
from manufacturing import Ui_manufacturing_dialog
from open_orders import Ui_open_orders_dialog
from assign_work import Ui_assign_work_dialog
from check_materials import Ui_check_materials_dialog
from PyQt6 import QtWidgets as qtw
import db_manager as dbm
import mysql.connector as mc
from datetime import datetime

debugging = True

db = mc.connect(
                host="10.0.0.126",
                user="sqluser",
                password="essqueel",
                charset="utf8mb4"
            )
cursor = db.cursor()


# Each window needs its own class
class PyPOS(qtw.QMainWindow):
    # Custom initializer to build the window
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Define the windows that can be reached from here
        self.pass_window = PasswordEntry()
        self.begin_window = Begin()
        self.time_clock_window = selectEmployee()
        self.manager_window = manager()

        # Connect the buttons to methods
        self.ui.btn_begin.clicked.connect(self.show_password_entry)
        self.ui.btn_quit.clicked.connect(self.exit)
        self.ui.btn_timeclock.clicked.connect(self.time_clock)
        self.ui.btn_manager.clicked.connect(self.show_manager)

    # Methods to show each window
    def show_password_entry(self):
        self.pass_window.show()

    def show_manager(self):
        self.manager_window.show()

    def exit(self):
        exit(0)

    def time_clock(self):
        self.time_clock_window.show()


class PasswordEntry(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.password = ""

        # Define windows that can be reached from here
        self.sale_window = makeSale()

        # Connect the buttons to methods
        self.ui.btn_ok.clicked.connect(self.try_login)
        self.ui.btn_1.clicked.connect(self.btn_1)
        self.ui.btn_2.clicked.connect(self.btn_2)
        self.ui.btn_3.clicked.connect(self.btn_3)
        self.ui.btn_4.clicked.connect(self.btn_4)
        self.ui.btn_5.clicked.connect(self.btn_5)
        self.ui.btn_6.clicked.connect(self.btn_6)
        self.ui.btn_7.clicked.connect(self.btn_7)
        self.ui.btn_8.clicked.connect(self.btn_8)
        self.ui.btn_9.clicked.connect(self.btn_9)
        self.ui.btn_0.clicked.connect(self.btn_0)
        self.ui.btn_backspace.clicked.connect(self.btn_backspace)

    def exit(self):
        self.close()

    def try_login(self):
        cursor.execute("SELECT ID, first_name FROM dbs1709505.employee WHERE passcode='{}'".format(self.password))

        # Debugging - print the password entered and the employee ID it links to.
        if debugging:
            print("password is: {}".format(self.password))
            for row in cursor:
                print("Employee ID: {}".format(row[0]))

        # Verify password is good
        if cursor.rowcount < 1:
            print("Failure")
            self.ui.lbl_pass_input.setText("Invalid Password")
            self.password = ""
        else:
            print("Success")
            # self.ui.lbl_pass_input.setText(cursor.rowcount())

    def load_sale_window(self):
        self.close()
        self.sale_window.show()

    def btn_1(self):
        self.button_press("1")

    def btn_2(self):
        self.button_press("2")

    def btn_3(self):
        self.button_press("3")

    def btn_4(self):
        self.button_press("4")

    def btn_5(self):
        self.button_press("5")

    def btn_6(self):
        self.button_press("6")

    def btn_7(self):
        self.button_press("7")

    def btn_8(self):
        self.button_press("8")

    def btn_9(self):
        self.button_press("9")

    def btn_0(self):
        self.button_press("0")

    def btn_backspace(self):
        l = len(self.password)
        self.password = self.password[:l-1]
        cur_text = self.ui.lbl_pass_input.text()
        l2 = len(cur_text)
        cur_text = ""
        for i in range(l2 - 1):
            cur_text += "*"
        self.ui.lbl_pass_input.setText(cur_text)

    def button_press(self, pressed):
        self.password = self.password + pressed
        cur_text = self.ui.lbl_pass_input.text()
        if cur_text == "Enter Password" or cur_text == "Invalid Password":
            self.ui.lbl_pass_input.setText("*")
        else:
            self.ui.lbl_pass_input.setText(cur_text + "*")


class Begin(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_BeginWindow()
        self.ui2.setupUi(self)
        self.ui2.btn_sale_2.clicked.connect(self.exit)

    def exit(self):
        self.close()


class makeSale(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_SaleWindow()
        self.ui.setupUi(self)

        # Link the buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_discount_check.clicked.connect(self.discount_check)
        self.ui.btn_discount_item.clicked.connect(self.discount_item)
        self.ui.btn_settle.clicked.connect(self.settle_window)
        self.ui.btn_cust_lookup.clicked.connect(self.customer_lookup)
        self.ui.btn_manage_acct.clicked.connect(self.manage_account)

    def exit(self):
        self.close()

    def discount_check(self):
        self.discount_check_window = discountCheck()
        self.discount_check_window.show()

    def discount_item(self):
        self.discount_item_window = discountCheck()
        self.discount_item_window.show()

    def settle_window(self):
        self.settle_window = settle()
        self.settle_window.show()

    def customer_lookup(self):
        self.customer_lookup_window = customerLookup()
        self.customer_lookup_window.show()

    def manage_account(self):
        self.manage_account_window = manageAccount()
        self.manage_account_window.show()


class discountCheck(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the ui
        self.ui = Ui_discount_check_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_percent.clicked.connect(self.show_discount_percent_entry)
        self.ui.btn_amount.clicked.connect(self.show_discount_amount_entry)

    # Methods
    def show_discount_percent_entry(self):
        self.close()
        self.discount_percent_entry = discount_percent()
        self.discount_percent_entry.show()

    def show_discount_amount_entry(self):
        self.close()
        self.discount_amount_entry = discount_amount()
        self.discount_amount_entry.show()


class discount_percent(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_discount_percent_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_ok.clicked.connect(self.exit)

    # Methods
    def exit(self):
        self.close()


class discount_amount(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_discount_amount_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_ok.clicked.connect(self.exit)

    # Methods
    def exit(self):
        self.close()

    def new_customer(self):
        self.close()
        self.new_customer_window = newCustomer()
        self.new_customer_window.show()


class settle(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_settle_window()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_discount_check.clicked.connect(self.discount_check)
        self.ui.btn_discount_item.clicked.connect(self.discount_check)
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_finalize.clicked.connect(self.finalize)

    def exit(self):
        self.close()

    def discount_check(self):
        self.discount_type = discountCheck()
        self.discount_type.show()

    def finalize(self):
        self.close()
        # Close the sale window
        # TODO: Fix this to close the sale window instead of the entire program
        # makeSale.exit(self.makeSale)


class customerLookup(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_customer_lookup_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_new_customer.clicked.connect(self.new_customer)

    def exit(self):
        self.close()

    def search_customer(self):
        self.close()
        self.search_reults = search_customer_results()
        self.search_reults.show()

    def new_customer(self):
        self.close()
        self.new_customer_window = newCustomer()
        self.new_customer_window.show()


class search_customer_results(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_select_account_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_select.clicked.connect(self.select_customer)
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def select_customer(self):
        self.close()
        # TODO: Return customer record to the make sale screen


class newCustomer(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_new_customer_dialog()
        self.ui.setupUi(self)

        # Connect buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class manageAccount(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_manage_account_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_payment.clicked.connect(self.make_payment)

    def exit(self):
        self.close()

    def make_payment(self):
        self.close()
        self.make_payment_screen = makePayment()
        self.make_payment_screen.show()


class makePayment(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_payment_amount_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_ok.clicked.connect(self.exit)

    def exit(self):
        self.close()


class selectEmployee(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI

        # Each name needs to go on a button
        #
        # cursor.execute("SELECT first_name FROM dbs1709505.employee")
        # for row in cursor:
        #     print(row[0])

        self.ui = Ui_time_clock_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_emp_1.clicked.connect(self.exit)
        self.ui.btn_emp_2.clicked.connect(self.exit)
        self.ui.btn_emp_3.clicked.connect(self.exit)
        self.ui.btn_emp_4.clicked.connect(self.exit)
        self.ui.btn_emp_5.clicked.connect(self.exit)
        self.ui.btn_emp_6.clicked.connect(self.exit)
        self.ui.btn_emp_7.clicked.connect(self.exit)
        self.ui.btn_emp_8.clicked.connect(self.exit)
        self.ui.btn_emp_9.clicked.connect(self.exit)
        self.ui.btn_emp_10.clicked.connect(self.exit)
        self.ui.btn_emp_11.clicked.connect(self.exit)

    def exit(self):
        self.close()
    # TODO: Create method to login/logout emp


class manager(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_manager_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_stock.clicked.connect(self.stock)
        self.ui.btn_edit_groups.clicked.connect(self.groups)
        self.ui.btn_edit_employee.clicked.connect(self.edit_employee)
        self.ui.btn_deposit.clicked.connect(self.deposit)
        self.ui.btn_payroll.clicked.connect(self.payroll)
        self.ui.btn_manufacturin.clicked.connect(self.manufacturing)

    def exit(self):
        self.close()

    def stock(self):
        self.close()
        self.stock_window = stock()
        self.stock_window.show()

    def groups(self):
        self.close()
        self.groups_window = groups()
        self.groups_window.show()

    def edit_employee(self):
        self.close()
        self.emp_window = edit_employee()
        self.emp_window.show()

    def deposit(self):
        self.close()
        self.window = makePayment()
        self.window.show()

    def payroll(self):
        self.close()
        self.window = payroll()
        self.window.show()

    def manufacturing(self):
        self.close()
        self.window = manufacturing()
        self.window.show()


class stock(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_stock_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_add_edit_vendo.clicked.connect(self.edit_vendor)
        # self.ui.btn_edit_item.clicked.connect(self.edit_item)
        self.ui.btn_add_item.clicked.connect(self.add_item)
        self.ui.btn_edit_item.clicked.connect(self.edit_item)
        self.ui.btn_perform_count.clicked.connect(self.inventory_count)

    def exit(self):
        self.close()

    def edit_vendor(self):
        self.close()
        self.vendor_screen = vendors()
        self.vendor_screen.show()

    def add_item(self):
        self.close()
        self.item_window = addItem()
        self.item_window.show()

    def edit_item(self):
        self.close()
        self.edit_item_window = editItem()
        self.edit_item_window.show()

    def inventory_count(self):
        self.close()
        self.window = inventoryCount()
        self.window.show()


class groups(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_groups_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class vendors(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_vendors_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class addItem(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_add_item_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class edit_employee(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_edit_employee_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class editItem(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_edit_item_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class inventoryCount(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_count_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class payroll(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_payroll_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class manufacturing(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_manufacturing_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_view_orders.clicked.connect(self.open_orders)
        self.ui.btn_assign_work.clicked.connect(self.assign_work)
        self.ui.btn_check_materials.clicked.connect(self.check_materials)

    def exit(self):
        self.close()

    def open_orders(self):
        self.close()
        self.window = openOrders()
        self.window.show()

    def assign_work(self):
        self.close()
        self.window = assignWork()
        self.window.show()

    def check_materials(self):
        self.close()
        self.window = checkMaterials()
        self.window.show()


class openOrders(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_open_orders_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_ok.clicked.connect(self.exit)

    def exit(self):
        self.close()


class assignWork(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_assign_work_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


class checkMaterials(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_check_materials_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods
        self.ui.btn_ok.clicked.connect(self.exit)

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = PyPOS()
    widget.show()

    app.exec()
