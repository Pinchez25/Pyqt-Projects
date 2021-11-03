import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class Animate(QWidget):
    def __init__(self):
        super(Animate, self).__init__()
        self.baseHeight = 50
        self.extendedHeight = 300
        self.rect = QRect(600, 300, 300, self.baseHeight)
        self.setGeometry(self.rect)

        self.btn = QPushButton('Expand', self)
        self.btn.move(20, 15)
        self.btn.clicked.connect(self.resizeWindow)

    def resizeWindow(self):
        currentHeight = self.height()
        # self.btn.setText('Shrink')

        if currentHeight == self.baseHeight:
            baseHeight = self.baseHeight
            extendedHeight = self.extendedHeight
            self.btn.setText('Shrink')
        else:
            baseHeight = self.extendedHeight
            extendedHeight = self.baseHeight
            self.btn.setText('Expand')

        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(800)
        self.animation.setStartValue(QRect(600, 300, 300, baseHeight))
        self.animation.setEndValue(QRect(600, 300, 300, extendedHeight))
        self.animation.start()


if __name__ == '__main__':
    app = QApplication([])
    demo = Animate()
    demo.show()
    sys.exit(app.exec())
