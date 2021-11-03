import sys

import san as san
from PyQt6.QtWidgets import *
# from PyQt6.Qt import QStandardItemModel,QStandardItem
from PyQt6.QtGui import QFont, QColor, QStandardItemModel, QStandardItem


class StandardItem(QStandardItem):
    def __init__(self, text="", font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super(StandardItem, self).__init__()

        fnt = QFont('Open sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(text)


class AppDemo(QMainWindow):
    def __init__(self):
        super(AppDemo, self).__init__()
        self.setWindowTitle("World country Diagram")
        self.resize(500, 700)

        treeView = QTreeView()
        treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        america = StandardItem("America", 16, set_bold=True)

        california = StandardItem('California', 14)
        america.appendRow(california)

        oakland = StandardItem("Oakland", 12, color=QColor(155, 0, 0))
        sanfransisco = StandardItem('San Fransisco', 12, color=QColor(155, 0, 0))
        sanjose = StandardItem('San Jose', 12, color=QColor(155, 0, 0))

        # california.appendRow(oakland)
        # california.appendRow(sanfransisco)
        # california.appendRow(sanjose)
        california.appendRows([oakland, sanfransisco, sanjose])

        texas = StandardItem('Texas', 14)
        america.appendRow(texas)

        austin = StandardItem('Austin', 12, color=QColor(155, 0, 0))
        houston = StandardItem('Houston', 12, color=QColor(155, 0, 0))
        dallas = StandardItem('dallas', 12, color=QColor(155, 0, 0))

        # texas.appendRow(austin)
        # texas.appendRow(houston)
        # texas.appendRow(dallas)
        texas.appendRows([austin, houston, dallas])

        canada = StandardItem('Canada', 16, set_bold=True)

        alberta = StandardItem('Alberta', 14, color=QColor("Green"))
        bc = StandardItem('British Columbia', 14, color=QColor("Green"))
        ontario = StandardItem('Ontario', 14, color=QColor("Green"))
        canada.appendRows([alberta, bc, ontario])

        # rootNode.appendRow(america)
        # rootNode.appendRow(canada)
        rootNode.appendRows([america, canada])

        treeView.setModel(treeModel)
        treeView.expandAll()
        treeView.doubleClicked.connect(self.getValue)

        self.setCentralWidget(treeView)

    @staticmethod
    def getValue(val):
        print(val.data())
        print(val.row())
        print(val.column())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
