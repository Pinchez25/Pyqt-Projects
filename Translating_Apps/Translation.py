import sys

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton(self)
        self.btn.setText(self.tr("Click Me"))
        self.btn.move(100, 250)

        self.btn2 = QPushButton(self)
        self.btn2.setText(self.tr("Click Me Too"))
        self.btn2.move(300, 250)

        self.setWindowTitle(self.tr("Translating Qt Files"))
        self.setGeometry(200, 200, 500, 500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    languages = ['English', 'Swahili']


    lang, test = QInputDialog.getItem(None, 'Select Language', "Language", languages)
    translator = QTranslator(app)
    if lang == 'Swahili':+
        translator.load("sw_ke.qm")

    if lang != "English":
        app.installTranslator(translator)

    win = Window()

    sys.exit(app.exec_())
