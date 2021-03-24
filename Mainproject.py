import sys
import sqlite3
import xml.etree.ElementTree as ET
from datetime import datetime
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
import Main
import add_product
import edit_product
import add_product2
import facture
import edit_product2


class Main_window(QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.w2 = window2()
        self.setupUi(self)
        self.tw.doubleClicked.connect(self.double_func)

        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("""create table if 
        not exists data(id integer primary key, name text, factory text, count text, 
        cost integer, package integer, date text, code integer)""")
        cur.execute("""create table if not exists fulldata(code integer primary key, name text, factory text, 
        cost integer, package integer, date text)""")
        cur.execute("""create table if not exists factures(id integer primary key, name text, summa integer, 
                    vaqti text)""")
        cur.execute("""create table if not exists history(id integer primary key, name text, factory text, count text, 
        cost integer, date text, code integer, factory_code integer)""")
        conn.commit()
        conn.close()

        self.settable()

        self.pushButton_2.clicked.connect(self.open_window2)
        self.delete_btn.clicked.connect(self.del_func)
        self.lineEdit.textChanged.connect(self.search_func)
        self.tw.clicked.connect(self.add_product)
        self.exprt.clicked.connect(self.export)
        self.pushButton_3.clicked.connect(self.open_factures)

    def open_factures(self):
        self.factures_window = facture_class()
        self.factures_window.showMaximized()

    def double_func(self):
        if len(self.lineEdit.text()) < 3:
            id = self.tw.item(self.tw.currentRow(), 0).text()
            self.window_edit2 = w_edit(id)
            self.window_edit2.show()

    def export(self):
        if self.tw.rowCount() != 0:
            file = QFileDialog.getSaveFileName(self, 'Файлларни юклаш', '', "Xml (*.xml)")[0]
            if file != "":
                conn = sqlite3.connect("data.db")
                cur = conn.cursor()
                cur.execute("""insert into factures(name, summa, vaqti) values(?, ?, ?)""",
                            [file, self.lineEdit_2.text().replace(" ", ""), datetime.now().strftime("%Y-%m-%d, %H:%M")])
                conn.commit()
                doc = ET.Element("DocumentSchema", attrib={'xmlns': 'http://tempuri.org/DocumentSchema.xsd'})
                d = ET.SubElement(doc, "Documents")
                ET.SubElement(d, "DocumentType").text = "2"
                ET.SubElement(d, "DocumentID").text = str(cur.lastrowid)
                ET.SubElement(d, "DocumentDate").text = datetime.now().strftime("%Y-%m-%d") + "T00:00:00+05:00"
                ET.SubElement(d, "DocumentNumber").text = str(cur.lastrowid)
                self.document_id = str(cur.lastrowid)
                cur.execute("""select * from data""")
                for i in cur.fetchall():
                    cur.execute("""insert into history(name, factory, count, cost, date, code, factory_code) values(?, ?, ?,
                                ?, ?, ?, ?)""", [i[1], i[2], i[3], i[4], i[6], i[7], int(self.document_id)])
                    g = ET.SubElement(doc, "DocumentDetails")
                    ET.SubElement(g, "DocumentType").text = "2"
                    ET.SubElement(g, "DocumentID").text = self.document_id
                    ET.SubElement(g, "GoodID").text = str(i[7])
                    ET.SubElement(g, "PlantName").text = i[2]
                    ET.SubElement(g, "ProductName").text = i[1]
                    ET.SubElement(g, "BasePrice").text = str(float(i[4]))
                    ET.SubElement(g, "BuyPrice").text = str(float(i[4]))
                    ET.SubElement(g, "PriceR").text = str(float(i[4]))
                    ET.SubElement(g, "PriceO").text = str(float(i[4]))
                    ET.SubElement(g, "PriceP").text = str(i[4])
                    ET.SubElement(g, "Price").text = str(i[4])
                    ET.SubElement(g, "Qty").text = str(i[3])
                    if i[6] != "":
                        ET.SubElement(g, "ExpDate").text = i[6] + "T00:00:00+05:00"
                    ET.SubElement(g, "PackageSize").text = str(i[5])
                    ET.SubElement(g, "Barcode")
                    ET.SubElement(g, "CategoryID").text = "1"
                tree = ET.ElementTree(doc)
                tree.write(file)

                cur.execute("drop table data")
                cur.execute("""create table if 
                        not exists data(id integer primary key, name text, factory text, count text, 
                        cost integer, package integer, date text, code integer)""")
                conn.commit()
                conn.close()
                self.update_table()

    def add_product(self):
        if len(self.lineEdit.text()) > 2:
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            cur.execute("""select * from data where name=? and factory=?""",
                        [self.tw.item(self.tw.currentRow(), 1).text(),
                         self.tw.item(self.tw.currentRow(), 2).text()])
            d = cur.fetchall()
            if len(d) != 0:
                self.w_error = window3(d[0])
                self.w_error.show()
            else:
                f = self.tw.item(self.tw.currentRow(), 0).text()
                self.w4 = win_add(f)
                self.w4.show()

    def keyPressEvent(self, e):
        k = e.key()
        if self.lineEdit.hasFocus() and k == Qt.Key_Down:
            if self.tw.rowCount() > 0:
                self.tw.setFocus()
                self.tw.selectRow(0)
        if self.tw.hasFocus() and k == Qt.Key_Delete:
            self.del_func()
        if self.tw.hasFocus() and k in [Qt.Key_Return, Qt.Key_Enter] and len(self.lineEdit.text()) > 2:
            self.add_product()
        if self.tw.hasFocus() and k == Qt.Key_Up:
            self.tw.clearSelection()
            self.lineEdit.setFocus()
        if k == Qt.Key_Escape:
            self.lineEdit.clear()
            self.lineEdit.setFocus()
        if k == Qt.Key_F1:
            self.open_window2()

    def search_func(self):
        if len(self.lineEdit.text()) > 2:
            self.tw.setColumnHidden(3, True)
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            text = '"%' + self.lineEdit.text() + '%"'
            text2 = '"%' + self.lineEdit.text().capitalize() + '%"'
            cur.execute(f"SELECT * FROM fulldata WHERE name LIKE {text} OR name LIKE {text2} order by name LIMIT 50")
            a = cur.fetchall()
            while self.tw.rowCount() > 0:
                self.tw.removeRow(0)
            if len(a) > 0:
                for row in range(0, len(a)):
                    b = self.tw.rowCount()
                    self.tw.insertRow(b)
                    if a[b][4] == 0:
                        q = ""
                    else:
                        q = str(a[b][4])
                    self.tw.setItem(b, 0, QTableWidgetItem(str(a[b][0])))
                    self.tw.setItem(b, 1, QTableWidgetItem(a[b][1]))
                    self.tw.setItem(b, 2, QTableWidgetItem(a[b][2]))
                    self.tw.setItem(b, 4, QTableWidgetItem(str(a[b][3])))
                    self.tw.setItem(b, 5, QTableWidgetItem(q))
                    self.tw.setItem(b, 6, QTableWidgetItem(a[b][5]))
            conn.close()
        else:
            self.tw.setColumnHidden(3, False)
            self.update_table()

    def del_func(self):
        if len(self.tw.selectedItems()) != 0 and len(self.lineEdit.text()) < 3:
            id = self.tw.item(self.tw.currentRow(), 0).text()
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            cur.execute("""delete from data where id=?""", (id,))
            conn.commit()
            conn.close()
            self.update_table()
            self.tw.setFocus()
            self.tw.selectRow(0)

    def settable(self):
        self.tw.setColumnHidden(0, True)
        self.tw.setColumnWidth(1, 380)
        self.tw.setColumnWidth(2, 300)
        self.tw.setColumnWidth(3, 150)
        self.tw.setColumnWidth(4, 150)
        self.tw.setColumnWidth(5, 120)
        self.tw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.update_table()

    def update_table(self):
        while self.tw.rowCount() > 0:
            self.tw.removeRow(0)

        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("select * from data order by name")
        a = cur.fetchall()
        conn.close()
        s = 0
        if len(a) > 0:
            for ro in range(0, len(a)):
                b = self.tw.rowCount()
                self.tw.insertRow(b)
                if a[b][5] == 0:
                    q = ""
                else:
                    q = str(a[b][5])
                self.tw.setItem(b, 0, QTableWidgetItem(str(a[b][0])))
                self.tw.setItem(b, 1, QTableWidgetItem(a[b][1]))
                self.tw.setItem(b, 2, QTableWidgetItem(a[b][2]))
                self.tw.setItem(b, 3, QTableWidgetItem(str(a[b][3])))
                self.tw.setItem(b, 4, QTableWidgetItem(str(a[b][4])))
                self.tw.setItem(b, 5, QTableWidgetItem(q))
                self.tw.setItem(b, 6, QTableWidgetItem(a[b][6]))
                s += int(a[b][3]) * int(a[b][4])
            self.lineEdit_2.setText('{:,}'.format(s).replace(',', ' '))
        else:
            self.lineEdit_2.setText("0")

    def open_window2(self):
        self.w2.show()
        date = datetime.now()
        self.w2.dateEdit.setDate(date)
        self.w2.lineEdit.setFocus()


class window3(QMainWindow, edit_product.Ui_MainWindow):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.id = id
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("""select * from data where id=?""", [id[0]])
        f = cur.fetchone()
        conn.close()
        # nomi
        self.lineEdit.setText(f[1])
        # zavodi
        self.lineEdit_2.setText(f[2])
        # narxi
        self.lineEdit_3.setText(str(f[4]))
        # qadoq
        if f[5] != 0:
            self.lineEdit_4.setText(str(f[5]))
        # muddati
        self.lineEdit_5.setText(f[6])
        # soni
        self.lineEdit_6.setText(str(f[3]))
        self.btn_ok.clicked.connect(self.btn_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)

    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Return, Qt.Key_Enter]:
            self.btn_clicked()
        elif e.key() == Qt.Key_Escape:
            self.btn_cancel_clicked()

    def btn_clicked(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("""update data set count=? where id=?""", (str(self.lineEdit_6.text()), self.id[0]))
        conn.commit()
        conn.close()
        w.update_table()
        self.close()
        w.lineEdit.setText("")

    def btn_cancel_clicked(self):
        self.close()


class window2(QMainWindow, add_product.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.pushButton_2.clicked.connect(self.set_style)
        self.pushButton.clicked.connect(self.finish_class)

    def set_style(self):
        self.lineEdit.setStyleSheet("QLineEdit{border: 2px solid #59CDF2; border-radius: 5px;} QLineEdit::focus{"
                                    "border: 1px solid blue;}")
        self.lineEdit_2.setStyleSheet("QLineEdit{border: 2px solid #59CDF2; border-radius: 5px;} QLineEdit::focus{"
                                      "border: 1px solid blue;}")
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.spin.setValue(1)
        self.spin_2.setValue(0)
        self.dateEdit.clear()
        self.close()

    def keyPressEvent(self, e):
        k = e.key()
        if k == Qt.Key_Escape:
            self.set_style()

        if self.lineEdit.hasFocus() and (k in [Qt.Key_Return, Qt.Key_Enter, Qt.Key_Down]):
            self.lineEdit_2.setFocus()
        elif self.lineEdit_2.hasFocus() and (k in [Qt.Key_Return, Qt.Key_Enter, Qt.Key_Down]):
            self.spin.setFocus()
        elif self.spin.hasFocus() and (k in [Qt.Key_Return, Qt.Key_Enter, Qt.Key_Down]):
            self.spin_2.setFocus()
        elif self.spin_2.hasFocus() and (k in [Qt.Key_Return, Qt.Key_Enter, Qt.Key_Down]):
            self.dateEdit.setFocus()
        elif self.dateEdit.hasFocus() and (k in [Qt.Key_Return, Qt.Key_Enter]):
            self.finish_class()

        if k == Qt.Key_Up and self.dateEdit.hasFocus():
            self.lineEdit_5.setFocus()
        elif k == Qt.Key_Up and self.lineEdit_5.hasFocus():
            self.spin_2.setFocus()
        elif k == Qt.Key_Up and self.spin_2.hasFocus():
            self.spin.setFocus()
        elif k == Qt.Key_Up and self.spin.hasFocus():
            self.lineEdit_2.setFocus()
        elif k == Qt.Key_Up and self.lineEdit_2.hasFocus():
            self.lineEdit.setFocus()

    def finish_class(self):
        if "" in [self.lineEdit.text(), self.lineEdit_2.text(), self.spin.text(), self.spin_2.text()]:
            if self.lineEdit.text() == "":
                self.lineEdit.setStyleSheet("QLineEdit{border: 2px solid red;}")
                self.lineEdit.setFocus()

            if self.lineEdit_2.text() == "":
                self.lineEdit_2.setStyleSheet("QLineEdit{border: 2px solid red;}")
                if self.lineEdit.text() != "":
                    self.lineEdit_2.setFocus()
        else:
            nomi = self.lineEdit.text()
            zavodi = self.lineEdit_2.text()
            soni = self.spin.value()
            narxi = self.spin_2.value()
            qadoq = "1"
            if self.dateEdit.date() != datetime.now():
                muddati = self.dateEdit.text()
            else:
                muddati = ""
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            cur.execute("""select * from fulldata where name=? and factory=?""", [nomi, zavodi])
            c = cur.fetchall()

            if len(c) != 0:
                cur.execute("""update fulldata set cost=?, date=? where name=? and factory=?""",
                            (int(narxi), muddati, nomi, zavodi))
            else:
                cur.execute("""insert into fulldata(name, factory, cost, package, date) values(?, ?, ?, ?, ?)""",
                            [nomi, zavodi,
                             int(narxi), int(qadoq), muddati])
            conn.commit()
            cur.execute("""select * from data where name=? and factory=?""",
                        [nomi, zavodi])

            d = cur.fetchall()

            if len(d) != 0:
                self.w3 = window3(d[0])
                self.w3.show()
                self.spin_2.setFocus()
                self.spin_2.selectAll()
                self.set_style()
            else:
                cur.execute("""select * from fulldata where name=?""", [nomi])
                a = cur.fetchone()
                cur.execute("""insert into data(name, factory, count, cost, package, date, code) values(?, ?, ?, ?, ?, 
                            ?, ?)""", [nomi, zavodi, int(soni), int(narxi), int(qadoq), muddati, a[0]])
            conn.commit()
            conn.close()
            w.update_table()
            self.set_style()


class win_add(QMainWindow, add_product2.Ui_MainWindow):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.t = QIntValidator()
        self.count.setValidator(self.t)
        self.cost.setValidator(self.t)

        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.btn_ok)

        self.conn = sqlite3.connect("data.db")
        self.cur = self.conn.cursor()
        self.cur.execute("select * from fulldata where code=?", [int(id)])
        self.a = self.cur.fetchone()
        self.name.setText(self.a[1])
        self.cost.setText(str(self.a[3]))
        self.count.setFocus()

    def btn_ok(self):
        if len(self.count.text()) != 0 and len(self.cost.text()) != 0:
            self.cur.execute("""insert into data(name, factory, count, cost, package, date, code) values(?, ?, ?, ?, ?, 
                                        ?, ?)""",
                             [self.a[1], self.a[2], int(self.count.text()), int(self.cost.text()), self.a[4], self.a[5],
                              self.a[0]])
            self.cur.execute("""update fulldata set cost=? where code=?""", [int(self.cost.text()), int(self.a[0])])
            self.conn.commit()
            self.count.setText("")
            self.close()
            w.update_table()
            w.lineEdit.clear()

    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Return, Qt.Key_Enter] and self.count.hasFocus():
            self.btn_ok()


class facture_class(QMainWindow, facture.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget_2.setColumnHidden(0, True)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget_2.setColumnWidth(1, 350)
        self.tableWidget_2.setColumnWidth(2, 280)
        self.tableWidget_2.setColumnWidth(3, 150)
        self.tableWidget_2.setColumnWidth(4, 180)

        self.update_table()
        self.tableWidget.itemSelectionChanged.connect(self.print_items)
        self.btn_return.clicked.connect(self.return_facture)

    def return_facture(self):
        if len(self.tableWidget.selectedItems()) != 0:
            id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            cur.execute("drop table data")
            cur.execute("""create table if 
                                not exists data(id integer primary key, name text, factory text, count text, 
                                cost integer, package integer, date text, code integer)""")
            cur.execute("select * from history where factory_code=?", [int(id)])
            a = cur.fetchall()
            for i in a:
                cur.execute(
                    """insert into data(name, factory, count, cost, package, date, code) values(?, ?, ?, ?, ?, ?, ?)""",
                    [i[1], i[2], i[3], i[4], 1, i[5], i[6]])
            conn.commit()
            conn.close()
            self.close()
            w.update_table()

    def update_table(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("""select * from factures""")
        a = cur.fetchall()
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        if len(a) > 0:
            for i in range(0, len(a)):
                b = self.tableWidget.rowCount()
                self.tableWidget.insertRow(b)
                self.tableWidget.setItem(b, 0, QTableWidgetItem(str(a[i][0])))
                self.tableWidget.setItem(b, 1, QTableWidgetItem(a[i][1].split("/")[-1]))
                self.tableWidget.setItem(b, 2, QTableWidgetItem(str(a[i][2])))
                self.tableWidget.setItem(b, 3, QTableWidgetItem(a[i][3]))
            conn.close()

    def print_items(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("""select * from history where factory_code=?""", [int(self.tableWidget.selectedItems()[0].text())])
        a = cur.fetchall()
        while self.tableWidget_2.rowCount() > 0:
            self.tableWidget_2.removeRow(0)
        if len(a) > 0:
            for i in range(0, len(a)):
                b = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(b)
                self.tableWidget_2.setItem(b, 0, QTableWidgetItem(str(a[b][0])))
                self.tableWidget_2.setItem(b, 1, QTableWidgetItem(a[b][1]))
                self.tableWidget_2.setItem(b, 2, QTableWidgetItem(a[b][2]))
                self.tableWidget_2.setItem(b, 3, QTableWidgetItem(str(a[b][3])))
                self.tableWidget_2.setItem(b, 4, QTableWidgetItem(str(a[b][4])))
                self.tableWidget_2.setItem(b, 5, QTableWidgetItem(a[b][5]))
                conn.close()


class w_edit(QMainWindow, edit_product2.Ui_MainWindow):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.ok_btn)
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("""select * from data where id=?""", [id])
        self.a = cur.fetchone()
        conn.close()
        self.lineEdit.setText(self.a[1])
        self.lineEdit_2.setText(self.a[2])
        self.spin.setValue(int(self.a[3]))
        self.spin_2.setValue(self.a[4])
        if self.a[6] != "":
            date = datetime.strptime(self.a[6], "%Y-%m-%d")
            self.dateEdit.setDate(date)
        else:
            self.dateEdit.setDate(datetime.now())

    def keyPressEvent(self, e):
        k = e.key()
        if k in [Qt.Key_Return, Qt.Key_Enter]:
            self.ok_btn()
        elif k == Qt.Key_Escape:
            self.close()
    def ok_btn(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        if self.dateEdit.date() == datetime.now():
            date = ""
        else:
            date = self.dateEdit.text()
        cur.execute("""update data set name=?, factory=?, count=?, cost=?, date=? where id=?""", (self.lineEdit.text(),
                                                                                                  self.lineEdit_2.text(),
                                                                                                  str(
                                                                                                      self.spin.value()),
                                                                                                  self.spin_2.value(),
                                                                                                  date, self.a[0]))

        cur.execute("""update fulldata set name=?, factory=?, cost=?, date=? where code=?""", (self.lineEdit.text(),
                                                                                               self.lineEdit_2.text(),
                                                                                               self.spin_2.value(),
                                                                                               date, self.a[7]))

        conn.commit()
        conn.close()
        self.close()
        w.update_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main_window()
    w.showMaximized()
    sys.exit(app.exec_())
