import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import *


# from PySide6.QtGui import QPixmap


class Window(QMainWindow):
    check_box = None
    tray_icon = None

    def __init__(self):
        super(Window, self).__init__()

        try:
            self.setMinimumSize(QSize(480, 80))
            self.setWindowTitle("System Tray Application")
            central_widget = QWidget(self)
            self.setCentralWidget(central_widget)

            lay = QGridLayout(self)
            central_widget.setLayout(lay)
            lay.addWidget(QLabel("Application which can minimize to tray", self), 0, 0)

            self.check_box = QCheckBox("Minimize to tray")
            lay.addWidget(self.check_box, 1, 0)
            lay.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding), 2, 0)

            self.tray_icon = QSystemTrayIcon(self)
            self.tray_icon.setIcon(QIcon('Images/cat.jpg'))

            show_action = QAction("Show", self)
            quit_action = QAction("Exit", self)
            hide_action = QAction("Hide", self)
            show_action.triggered.connect(self.show)
            hide_action.triggered.connect(self.hide)
            quit_action.triggered.connect(QApplication.instance().quit)
            tray_menu = QMenu()
            tray_menu.addAction(show_action)
            tray_menu.addAction(hide_action)
            tray_menu.addAction(quit_action)
            self.tray_icon.setContextMenu(tray_menu)
            self.tray_icon.show()

            # Override closeEvent, to intercept the window closing event
            # The window will be closed only if there is no check mark in the check box

        except Exception as e:
            print("Error " + str(e))

    def closeEvent(self, event):
        try:
            if self.check_box.isChecked():
                event.ignore()
                self.hide()
                self.tray_icon.showMessage(
                    "Tray Program",
                    "Application was minimized to Tray",
                    QIcon('Images/taipei.jpg'),
                    2000
                )
            else:
                QMessageBox.information(QMessageBox(), "Info", "Exited successfully")
                QApplication.instance().quit()
        except Exception as e:
            print("Error: " + str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
