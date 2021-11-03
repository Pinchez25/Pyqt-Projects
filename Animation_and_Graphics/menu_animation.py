import sys

from PyQt6.QtWidgets import *

from PyQt6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Animating Context Menu")
        self.resize(500, 500)

        self.context_ = QMenu(self)
        self.context_.addAction("Menu 1")
        self.context_.addAction("Menu 2")
        self.context_.addAction("Menu 3")
        self.context_.addAction("Menu 4")
        self.context_.addAction("Menu 5")
        self.context_.addAction("Menu 6")

        self.anim = QPropertyAnimation(self.context_, b'geometry', self)
        self.anim.setEasingCurve(QEasingCurve.Type.Linear)
        self.anim.setDuration(1000)

        self.show()

    def contextMenuEvent(self, event):
        pos = event.globalPos()
        size = self.context_.sizeHint()
        x, y, w, h = pos.x(), pos.y(), size.width(), size.height()
        self.anim.setStartValue(QRect(x, y, 0, 0))
        self.anim.setEndValue(QRect(x, y, w, h))
        self.anim.start()
        self.context_.exec(pos)
        # print(pos.x(), pos.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec())
