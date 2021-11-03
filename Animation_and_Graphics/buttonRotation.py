import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer


class Rotate(QWidget):
    def __init__(self):
        super(Rotate, self).__init__()

        self.n = 10

        lay = QVBoxLayout()
        self.setLayout(lay)

        for i in range(self.n):
            btn = QPushButton()
            btn.setText(str(i))
            btn.setObjectName(f'Button {i}')
            lay.addWidget(btn)

        timer = QTimer(self)
        timer.setInterval(1000)
        timer.timeout.connect(self.updateText)
        timer.start()

        self.show()

    def updateText(self):
        for i in range(self.n):
            child = self.findChild(QPushButton, f'Button {i}')
            counter = int(child.text())
            child.setText(str(counter + 1))


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet("""
    QWidget {
        font-size: 35px;
        }
    """)
    rot = Rotate()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
