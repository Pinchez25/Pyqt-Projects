import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.resize(400, 400)

        lay = QVBoxLayout()
        btn = QPushButton("Fade")
        lay.addWidget(btn)
        self.setLayout(lay)

        self.anim = QPropertyAnimation(self, b'windowOpacity')
        self.anim.setDuration(3000)
        self.animate()
        self.show()

    def animate(self):
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()
        self.anim.finished.connect(self.close)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec())
