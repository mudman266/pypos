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

from PyQt6 import QtWidgets as qtw

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

        # Connect the buttons to methods
        self.ui.btn_begin.clicked.connect(self.show_password_entry)
        self.ui.btn_quit.clicked.connect(self.exit)
        self.ui.btn_timeclock.clicked.connect(self.time_clock)

    # Methods to show each window
    def show_password_entry(self):
        self.pass_window.show()

    def exit(self):
        exit(0)

    def time_clock(self):
        self.time_clock_window.show()


class PasswordEntry(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Define windows that can be reached from here
        self.sale_window = makeSale()

        # Connect the buttons to methods
        self.ui.btn_ok.clicked.connect(self.load_sale_window)

    def exit(self):
        self.close()

    def load_sale_window(self):
        self.close()
        self.sale_window.show()


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

        # Create windows that can be reached from here
        self.discount_percent_entry = discount_percent()
        self.discount_amount_entry = discount_amount()

        # Link buttons to methods
        self.ui.btn_percent.clicked.connect(self.show_discount_percent_entry)
        self.ui.btn_amount.clicked.connect(self.show_discount_amount_entry)

    # Methods
    def show_discount_percent_entry(self):
        self.close()
        self.discount_percent_entry.show()

    def show_discount_amount_entry(self):
        self.close()
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
        self.ui.btn_new_customer.clicked.connect(self.new_customer)

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
        makeSale.exit(self.makeSale)


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


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = PyPOS()
    widget.show()

    app.exec()
