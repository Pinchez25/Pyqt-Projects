import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.resize(1000, 500)

        names = ['Peter', 'Kelvin', 'James', 'Karen', 'Njeri', 'Faith', 'Amos', "Lydia", 'Carol', 'Jared', 'Jane',
                 'Janee', 'Jamrock']

        font = QFont('Open Sans', 12)
        lay = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setFixedHeight(50)
        self.input.setFont(font)
        self.input.editingFinished.connect(self.addEntry)
        lay.addWidget(self.input)

        self.model = QStandardItemModel()
        for i in names:
            self.model.appendRow(QStandardItem(i))
        completer = QCompleter(self.model, self)
        self.input.setCompleter(completer)

        self.console = QTextEdit()
        self.console.setFont(font)
        lay.addWidget(self.console)

        self.setLayout(lay)

    def addEntry(self):
        entryItem = self.input.text()
        self.input.clear()
        self.console.append(entryItem)

        if not self.model.findItems(entryItem):
            self.model.appendRow(QStandardItem(entryItem))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dm = Demo()
    dm.show()
    sys.exit(app.exec())
