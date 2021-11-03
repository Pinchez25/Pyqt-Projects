import sys

from PyQt6.QtWidgets import *
# from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Accordion(QWidget):
    def __init__(self,title=""):
        super(Accordion, self).__init__()

        self.btn = QToolButton(text=title, checkable=True,checked=False)
        self.btn.setStyleSheet("QToolButton {border:none;}")
        self.btn.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )
        self.btn.setArrowType(Qt.RightArrow)
        lay = QVBoxLayout(self)
        lay.addWidget(self.btn)
        self.setLayout(lay)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Accordion()
    win.show()
    sys.exit(app.exec())