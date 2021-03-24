# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 701)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/01/icon.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(45, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(45, 40))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 2px solid #59CDF2;\n"
"border-right: 0px;\n"
"}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/01/search_icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(28, 28))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(305, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(305, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("\n"
"QLineEdit{\n"
"background-color: white;\n"
"border: 2px solid #59CDF2;\n"
"border-left: 0px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(50000, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 2px solid #59CDF2;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tw = QtWidgets.QTableWidget(self.centralwidget)
        self.tw.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tw.setFont(font)
        self.tw.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tw.setAutoFillBackground(False)
        self.tw.setStyleSheet("::item:selected { color:white; background:#01a9b4;  }\n"
"\n"
"\n"
"")
        self.tw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw.setAlternatingRowColors(False)
        self.tw.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tw.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw.setRowCount(0)
        self.tw.setObjectName("tw")
        self.tw.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(6, item)
        self.tw.horizontalHeader().setVisible(True)
        self.tw.horizontalHeader().setCascadingSectionResizes(False)
        self.tw.horizontalHeader().setDefaultSectionSize(150)
        self.tw.horizontalHeader().setHighlightSections(True)
        self.tw.horizontalHeader().setMinimumSectionSize(0)
        self.tw.horizontalHeader().setSortIndicatorShown(False)
        self.tw.horizontalHeader().setStretchLastSection(True)
        self.tw.verticalHeader().setVisible(True)
        self.tw.verticalHeader().setCascadingSectionResizes(False)
        self.tw.verticalHeader().setDefaultSectionSize(35)
        self.tw.verticalHeader().setHighlightSections(True)
        self.tw.verticalHeader().setMinimumSectionSize(24)
        self.verticalLayout.addWidget(self.tw)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: #4CAF50;\n"
"border-radius: 8px;\n"
"  color: white;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(0, 170, 0);\n"
"border: 1px solid black;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #4CAF50;\n"
"border: 1px solid #626262;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/01/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setMinimumSize(QtCore.QSize(161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.delete_btn.setFont(font)
        self.delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 66, 70);\n"
"border-radius: 8px;\n"
"  color: black;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color:  rgb(255, 36, 41);\n"
"border: 1px solid black;\n"
"}\n"
"QPushButton::pressed{\n"
"\n"
"background-color: rgb(255, 66, 70);\n"
"border: 1px solid #626262;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/01/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.delete_btn.setIcon(icon3)
        self.delete_btn.setIconSize(QtCore.QSize(24, 24))
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_2.addWidget(self.delete_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(62, 204, 255);\n"
"border-radius: 8px;\n"
"  color: white;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: #00b7c2;\n"
"border: 1px solid black;\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(62, 204, 255);\n"
"border: 1px solid #626262;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/01/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.exprt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exprt.sizePolicy().hasHeightForWidth())
        self.exprt.setSizePolicy(sizePolicy)
        self.exprt.setMinimumSize(QtCore.QSize(120, 40))
        self.exprt.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exprt.setFont(font)
        self.exprt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exprt.setStyleSheet("QPushButton{\n"
"  background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #4CAF50;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: #38ff7d;\n"
"  color: white;\n"
"\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/01/xml.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exprt.setIcon(icon5)
        self.exprt.setIconSize(QtCore.QSize(24, 24))
        self.exprt.setObjectName("exprt")
        self.horizontalLayout_2.addWidget(self.exprt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Faktura yaratish"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Қўшиш учун"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        item = self.tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номи"))
        item = self.tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Заводи"))
        item = self.tw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Сони"))
        item = self.tw.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Нархи"))
        item = self.tw.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Қадоқ"))
        item = self.tw.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Муддати"))
        self.pushButton_2.setText(_translate("MainWindow", "Янги махсулот"))
        self.delete_btn.setText(_translate("MainWindow", "Ўчириш"))
        self.pushButton_3.setText(_translate("MainWindow", "   Фактуралар"))
        self.exprt.setText(_translate("MainWindow", "Экспорт"))
import Icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
