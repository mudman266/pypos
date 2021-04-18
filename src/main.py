# Josh Williams
# PyPOS

from FIRST import Ui_MainWindow
from begin import Ui_BeginWindow

from PyQt6 import QtWidgets as qtw
import sys


class PyPOS(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_begin.clicked.connect(self.show_begin)
        self.w = None

    def show_begin(self, checked):
        if self.w is None:
            self.w = Begin()
            self.w.show()
        else:
            self.w.close()
            self.w = None


class Begin(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BeginWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = PyPOS()
    widget.show()

    app.exec()
