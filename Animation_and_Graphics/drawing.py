import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Draw(QWidget):
    def __init__(self):
        super(Draw, self).__init__()

        self.circle = QRect(0, 0, 50, 50)

        # move the center of the circle to the specified position
        self.circle.moveCenter(QPoint(self.width() // 2, self.circle.height() // 2))
        print(self.circle.bottom())
        print(self.circle.top())

        self.step = QPoint(2, 5)
        self.y_direction = 1

        print(self.width())

        self.painter = QPainter(self)
        self.painter.setPen(QColor('brown'))
        self.painter.setBrush(QColor('pink'))

        timer = QTimer(self)
        timer.setInterval(10)
        timer.timeout.connect(self.update_position)
        timer.start()

        self.show()

    def drawCircle(self):
        self.painter.drawEllipse(self.circle)

    def drawLine(self):
        self.painter.drawLine(QPoint(0, 0), QPoint(200, 400))

    def paintEvent(self, e):
        self.drawCircle()
        # self.drawLine()

    def update_position(self):
        if self.circle.bottom() > self.height() and self.y_direction == 1:
            self.y_direction = -1
        if self.circle.top() < 0 and self.y_direction == -1:
            self.y_direction = 1

        self.circle.translate(QPoint(self.step * self.y_direction))
        self.update()


if __name__ == '__main__':
    app = QApplication([])
    win = Draw()
    sys.exit(app.exec())
