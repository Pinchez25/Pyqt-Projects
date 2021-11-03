"""
 Creating a bouncing effect
"""
import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Bouncing(QWidget):
    def __init__(self):
        super(Bouncing, self).__init__()
        self.resize(1000, 600)
        self.color = QColor('red')

        self.rect_circle = QRect(0, 0, 50, 50)
        self.rect_circle.moveCenter(QPoint(self.width() // 2, self.rect_circle.height() // 2))

        self.step = QPoint(0, 5)
        self.y_direction = 1

        timer = QTimer(self)
        timer.setInterval(10)
        timer.timeout.connect(self.update_position)
        timer.start()

        self.show()

    def paintEvent(self, event):
        bounce = QPainter(self)
        bounce.setPen(QColor('black'))
        bounce.setBrush(QColor('red'))
        bounce.drawEllipse(self.rect_circle)

    def update_position(self):
        if self.rect_circle.bottom() > self.height() and self.y_direction == 1:
            self.y_direction = -1
        if self.rect_circle.top() < 0 and self.y_direction == -1:
            self.y_direction = 1

        self.rect_circle.translate(QPoint(self.step * self.y_direction))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ball = Bouncing()
    sys.exit(app.exec())
