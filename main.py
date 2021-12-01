from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import random
import sys


class Main(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.pressvent)
        self.do_paint = False
        self.x = 0
        self.y = 0

    def pressvent(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)
        self.do_paint = True
        self.update()

    def drawing(self, qp):
        R = 255
        G = 255
        B = 0
        qp.setBrush(QColor(R, G, B))

        r = random.randint(10, self.geometry().width() // 2)
        qp.drawEllipse(self.x - r // 2, self.y - r // 2, r, r)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()


app = QApplication([])
main = Main()
main.show()
sys.exit(app.exec_())
