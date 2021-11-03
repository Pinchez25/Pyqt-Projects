import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(400, 150, 400, 400)

        layout = QVBoxLayout(self)
        btn = QPushButton("Click to shake", self)
        btn.clicked.connect(self.doShake)
        layout.addWidget(btn)
        self.shake(self)
        self.show()

    def doShake(self):
        self.shake(self)

    @staticmethod
    def shake(target):
        # if hasattr(target, '_shake_animation'):
        #     return
        #
        #
        # target._shake_animation = anim
        # anim.finished.connect(lambda: delattr(target, '_shake_animation'))
        anim = QPropertyAnimation(target, b'pos', target)
        pos = target.pos()
        x, y = pos.x(), pos.y()

        anim.setDuration(200)
        anim.setLoopCount(9)
        anim.setKeyValueAt(0, QPoint(x, y))
        anim.setKeyValueAt(0.09, QPoint(x + 2, y - 2))
        anim.setKeyValueAt(0.18, QPoint(x + 4, y - 4))
        anim.setKeyValueAt(0.27, QPoint(x + 2, y - 6))
        anim.setKeyValueAt(0.36, QPoint(x + 0, y - 8))
        anim.setKeyValueAt(0.45, QPoint(x - 2, y - 10))
        anim.setKeyValueAt(0.54, QPoint(x - 4, y - 8))
        anim.setKeyValueAt(0.63, QPoint(x - 6, y - 6))
        anim.setKeyValueAt(0.72, QPoint(x - 8, y - 4))
        anim.setKeyValueAt(0.81, QPoint(x - 6, y - 2))
        anim.setKeyValueAt(0.90, QPoint(x - 4, y - 0))
        anim.setKeyValueAt(0.99, QPoint(x - 2, y + 2))
        anim.setEndValue(QPoint(x, y))

        anim.start(anim.DeleteWhenStopped)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec())
