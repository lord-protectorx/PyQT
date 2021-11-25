import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btnClicked = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.btnClicked:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.btnClicked = True
        self.repaint()

    def draw_ellipse(self, qp):
        a = randint(15, 300)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(randint(0, 500), randint(0, 300), a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())