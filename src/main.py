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

        # Connect the buttons to methods
        self.ui.btn_begin.clicked.connect(self.show_password_entry)
        self.ui.btn_quit.clicked.connect(self.exit)

    # Methods to show each window
    def show_password_entry(self):
        self.pass_window.show()

    def exit(self):
        exit(0)


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

        # Create windows that can be reached from here
        self.discount_check_window = discountCheck()

        # Link the buttons to methods
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_discount_check.clicked.connect(self.discount_check)

    def exit(self):
        self.close()

    def discount_check(self):
        self.discount_check_window.show()


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


class discount_amount(qtw.QDialog):
    def __init__(self):
        super().__init__()

        # Setup the UI
        self.ui = Ui_discount_amount_dialog()
        self.ui.setupUi(self)

        # Link buttons to methods


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = PyPOS()
    widget.show()

    app.exec()
