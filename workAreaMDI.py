import sys

from PyQt6.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.resize(800, 800)

        workSpace = QMdiArea(self)
        workSpace.resize(self.rect().width(), self.rect().height())
        print(self.width(), ":", self.height())

        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(lambda date: print(date.getDate()))
        workSpace.addSubWindow(self.calendar)

        self.btn = QPushButton('My Button')
        self.btn.clicked.connect(lambda: print("Button is clicked"))
        workSpace.addSubWindow(self.btn)

        textEditor = QTextEdit()
        workSpace.addSubWindow(textEditor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
