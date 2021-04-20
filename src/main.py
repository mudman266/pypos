# Josh Williams
# PyPOS

from FIRST import Ui_MainWindow
from begin import Ui_BeginWindow

from PyQt6 import QtWidgets as qtw
import sys


class PyPOS(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_begin.clicked.connect(self.show_begin)
        self.begin_window = Begin()

    def show_begin(self, checked):
        self.begin_window.show()


class Begin(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_BeginWindow()
        self.ui2.setupUi(self)
        self.ui2.btn_sale_2.clicked.connect(self.exit)

    def exit(self, checked):
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = PyPOS()
    widget.show()

    app.exec()
