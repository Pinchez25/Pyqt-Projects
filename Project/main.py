import sys
import os
from os import path
import pymysql
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUiType



def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
FORM_CLASS,_ = loadUiType(resource_path('UI_Files/mainwindow.ui'))


class Window(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(Window, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)

        #loadUi('UI_Files/mainwindow.ui',self)

        self.populateTable1()
        self.navigate()
        self.handleButtons()

        self.show()

    def handleButtons(self):
        self.btnSearch.clicked.connect(self.searchTable)
        self.btnRefresh.clicked.connect(self.populateTable1)
        self.btnCheck.clicked.connect(self.Level)
        self.btnAdd.clicked.connect(self.add)
        self.btnDelete.clicked.connect(self.delete)

    def populateTable1(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', database='parts')

            cur = conn.cursor()
            sql = "select * from parts_table"
            cur.execute(sql)
            result = cur.fetchall()
            self.table.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.table.insertRow(row_number)
                for column, data in enumerate(row_data):
                    self.table.setItem(row_number, column, QTableWidgetItem(str(data)))

            cur2 = conn.cursor()
            cur3 = conn.cursor()

            parts_number = "SELECT COUNT(Distinct partName) FROM parts_table"
            ref_nbr = "select count(Distinct Reference) from parts_table"

            cur2.execute(parts_number)
            cur3.execute(ref_nbr)
            result2 = cur2.fetchone()
            result3 = cur3.fetchone()
            self.lblParts.setText(str(result2[0]))
            self.lblRef.setText(str(result3[0]))

            cur4 = conn.cursor()
            cur5 = conn.cursor()
            cur6 = conn.cursor()
            cur7 = conn.cursor()

            min_holes = "SELECT min(NumberOfHoles) from parts_table"
            max_holes = "SELECT max(NumberOfHoles) from parts_table"
            cur4.execute(min_holes)
            cur5.execute(max_holes)
            result_min_hole = cur4.fetchone()
            result_max_hole = cur5.fetchone()

            ref_min_hole = f"Select Reference from parts_table where NumberOfHoles = {result_min_hole[0]}"
            ref_max_hole = f"Select Reference from parts_table where NumberOfHoles = {result_max_hole[0]}"
            cur6.execute(ref_min_hole)
            cur7.execute(ref_max_hole)

            r1 = cur6.fetchone()[0]
            r2 = cur7.fetchone()[0]

            self.lblMaxHoles.setText(str(result_max_hole[0]))
            self.lblMinHoles.setText(str(result_min_hole[0]))
            self.lblMinHoles2.setText(r1)
            self.lblMaxHoles2.setText(r2)

            conn.close()

        except Exception as e:
            print("Error: " + str(e))

    def searchTable(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', database='parts')
            cur = conn.cursor()
            number = int(self.count_filter.text())
            sql = f"SELECT * FROM parts_table WHERE Count<={number}"
            cur.execute(sql)
            result = cur.fetchall()
            self.table.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.table.insertRow(row_number)
                for column, data in enumerate(row_data):
                    self.table.setItem(row_number, column, QTableWidgetItem(str(data)))
            conn.close()
        except Exception as e:
            print("Error: " + str(e))

    def Level(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', database='parts')

            cur = conn.cursor()
            sql = "select Reference, PartName, Count from parts_table order by Count ASC LIMIT 3"
            cur.execute(sql)
            result = cur.fetchall()
            self.table2.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.table2.insertRow(row_number)
                for column, data in enumerate(row_data):
                    self.table2.setItem(row_number, column, QTableWidgetItem(str(data)))

            conn.close()
        except Exception as e:
            print("Error: " + str(e))

    def navigate(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', database='parts')
            cur = conn.cursor()
            sql = "SELECT * from parts_table"
            cur.execute(sql)

            result = cur.fetchone()
            self.lblId.setText(str(result[0]))
            self.txtPart.setText(str(result[2]))
            self.txtRef.setText(str(result[1]))
            self.txtMin.setText(str(result[3]))
            self.txtMax.setText(str(result[4]))
            self.txtHoles.setText(str(result[5]))
            self.txtMaxDiam.setText(str(result[7]))
            self.txtMinDiam.setText(str(result[6]))
            self.txtCount.setValue(int(result[8]))

            conn.close()

        except Exception as e:
            print("Error: " + str(e))

    def add(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', database='parts')
            cur = conn.cursor()

            part_name = self.txtPart.text()
            reference_ = self.txtRef.text()
            min_area = self.txtMin.text()
            max_area = self.txtMax.text()
            number_of_holes = self.txtHoles.text()
            max_diameter = self.txtMaxDiam.text()
            min_diameter = self.txtMinDiam.text()
            count = str(self.txtCount.value())

            row = (reference_, part_name, min_area, max_area, number_of_holes, min_diameter, max_diameter, count)
            query = "Insert into parts_table (Reference, PartName, MinArea, MaxArea, NumberOfHoles, MinDiameter, " \
                    "MaxDiameter, Count) Values (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query, row)

            conn.commit()

            if query:
                print("Inserted successfully!")
            else:
                conn.rollback()
            conn.close()
        except Exception as e:
            print("Error: " + str(e.args))

    def delete(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', database='parts')
            cur = conn.cursor()

            id_ = self.lblId.text()

            query = "DELETE FROM parts_table WHERE ID = %s"
            cur.execute(query, id_)
            conn.commit()

            if query:
                print("Deleted successfully!")

            conn.close()
        except Exception as e:
            print("Error: " + str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec())
