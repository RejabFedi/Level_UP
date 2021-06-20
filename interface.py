# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget


class Inteface(QWidget):
    def __init__(self):
        QWidget.__init__(self)


if __name__ == "__main__":
    app = QApplication([])
    window = Inteface()
    window.show()
    sys.exit(app.exec_())
