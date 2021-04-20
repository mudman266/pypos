# Josh Williams
# PyPOS

# Import all the windows
from FIRST import Ui_MainWindow
from begin import Ui_BeginWindow
from password_entry import Ui_Dialog
from make_sale import Ui_SaleWindow

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
        self.ui = Ui_SaleWindow()
        self.ui.setupUi(self)
        self.ui.btn_cancel.clicked.connect(self.exit)

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = PyPOS()
    widget.show()

    app.exec()
