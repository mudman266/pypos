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
        self.begin_window = Begin()
        self.ui.btn_begin.clicked.connect(lambda checked: self.toggle_window(self.begin_window))

        self.setCentralWidget(self.ui)

    def toggle_window(self, window):
        if window.isVisibe():
            window.hide()
        else:
            window.show()


class Begin(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BeginWindow()
#        self.ui.setupUi(self)


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = PyPOS()
    widget.show()

    app.exec()
