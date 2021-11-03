import sys

from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *


class StandardItem(QStandardItem):
    def __init__(self, txt="", image_path="", font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super(StandardItem, self).__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

        if image_path:
            image = QImage(image_path)
            self.setData(image, Qt.ItemDataRole.DecorationRole)


class AppDemo(QMainWindow):
    def __init__(self):
        super(AppDemo, self).__init__()
        self.resize(1200, 1200)

        treeView = QTreeView()
        treeView.setHeaderHidden(True)
        treeView.header().setStretchLastSection(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        photos = StandardItem('My Photos', '', set_bold=True)

        whitney = StandardItem('Taipei', 'Images/taipei.jpg', 14)
        cat = StandardItem('Cat', 'Images/cat.jpg', 16)

        photos.appendRows([whitney, cat])

        rootNode.appendRow(photos)
        treeView.setModel(treeModel)
        treeView.expandAll()

        self.setCentralWidget(treeView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec())
