import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5 import uic


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)
        self.pushButton.clicked.connect()

    def run(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
