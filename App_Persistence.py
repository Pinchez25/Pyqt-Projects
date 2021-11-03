import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()

        self.settings = QSettings('MyApp', 'App1')

        try:
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
        except:
            pass

    def closeEvent(self, e):
        self.settings.setValue('window size', self.size())
        self.settings.setValue('window position', self.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('windowsvista')
    win = MyApp()
    win.show()
    sys.exit(app.exec())
