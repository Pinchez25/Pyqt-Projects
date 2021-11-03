import sys

from PyQt6.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Auto convert text to proper case')
        self.resize(700, 100)

        self.lay = QVBoxLayout()
        self.setLayout(self.lay)



        self.input = QLineEdit()
        self.input.setPlaceholderText('Type Something...')
        self.input.textChanged.connect(self.auto_convert_texts)
        self.lay.addWidget(self.input)

        self.show()

    def auto_convert_texts(self, txt):
        proper_case_text = txt.title()
        self.input.setText(proper_case_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QWidget {
        font-size:20px;
    }
    """)
    win = Window()
    sys.exit(app.exec())
