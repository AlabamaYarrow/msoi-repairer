# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Sun Oct 16 12:23:08 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 414)
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 581, 401))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 561, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 547, 788))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setLineWidth(2)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.calc_pushButton = QtWidgets.QPushButton(self.tab)
        self.calc_pushButton.setGeometry(QtCore.QRect(200, 290, 161, 41))
        self.calc_pushButton.setObjectName("calc_pushButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 20, 371, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.c_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.c_lineEdit.setObjectName("c_lineEdit")
        self.gridLayout_2.addWidget(self.c_lineEdit, 0, 1, 1, 1)
        self.s_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.s_label.setObjectName("s_label")
        self.gridLayout_2.addWidget(self.s_label, 4, 0, 1, 1)
        self.si_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.si_lineEdit.setObjectName("si_lineEdit")
        self.gridLayout_2.addWidget(self.si_lineEdit, 5, 1, 1, 1)
        self.c_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.c_label.setObjectName("c_label")
        self.gridLayout_2.addWidget(self.c_label, 0, 0, 1, 1)
        self.to_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.to_lineEdit.setObjectName("to_lineEdit")
        self.gridLayout_2.addWidget(self.to_lineEdit, 2, 1, 1, 1)
        self.to_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.to_label.setObjectName("to_label")
        self.gridLayout_2.addWidget(self.to_label, 2, 0, 1, 1)
        self.c3_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.c3_lineEdit.setObjectName("c3_lineEdit")
        self.gridLayout_2.addWidget(self.c3_lineEdit, 0, 3, 1, 1)
        self.n_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.n_lineEdit.setObjectName("n_lineEdit")
        self.gridLayout_2.addWidget(self.n_lineEdit, 3, 1, 1, 1)
        self.s_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.s_lineEdit.setObjectName("s_lineEdit")
        self.gridLayout_2.addWidget(self.s_lineEdit, 4, 1, 1, 1)
        self.c2_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.c2_lineEdit.setObjectName("c2_lineEdit")
        self.gridLayout_2.addWidget(self.c2_lineEdit, 0, 2, 1, 1)
        self.si_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.si_label.setObjectName("si_label")
        self.gridLayout_2.addWidget(self.si_label, 5, 0, 1, 1)
        self.n_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.n_label.setObjectName("n_label")
        self.gridLayout_2.addWidget(self.n_label, 3, 0, 1, 1)
        self.tno_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.tno_label.setObjectName("tno_label")
        self.gridLayout_2.addWidget(self.tno_label, 1, 0, 1, 1)
        self.tno_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tno_lineEdit.setObjectName("tno_lineEdit")
        self.gridLayout_2.addWidget(self.tno_lineEdit, 1, 1, 1, 1)
        self.c_info_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.c_info_label.setObjectName("c_info_label")
        self.gridLayout_2.addWidget(self.c_info_label, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(100, 10, 351, 311))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.choice_label = QtWidgets.QLabel(self.tab_2)
        self.choice_label.setGeometry(QtCore.QRect(100, 340, 211, 16))
        self.choice_label.setObjectName("choice_label")
        self.choice_val_label = QtWidgets.QLabel(self.tab_2)
        self.choice_val_label.setGeometry(QtCore.QRect(320, 340, 131, 16))
        self.choice_val_label.setText("")
        self.choice_val_label.setObjectName("choice_val_label")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчет модели ремонтника"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>1. Во вкладке &quot;<span style=\" font-weight:600;\">Ввод параметров</span>&quot; заполнить форму ввода значениями параметров. Значения входных параметров приведены ниже.</p><p>2. Нажать на кнопку &quot;<span style=\" font-weight:600;\">Произвести расчет</span>&quot;. При корректном вводе откроется вкладка с результатами вычислений. Значения выходных параметров приведены ниже.</p><p><span style=\" font-weight:600;\">Входные значения:</span></p><p><span style=\" font-weight:600;\">C</span> - количество сотрудников</p><p><span style=\" font-weight:600;\">t</span><span style=\" font-weight:600; vertical-align:sub;\">Н.О.</span>-среднее время наработки на отказ одного компьютера (в часах)</p><p><span style=\" font-weight:600;\">t</span><span style=\" font-weight:600; vertical-align:sub;\">О</span>- среднее время ремонта одного компьютера (в часах)</p><p><span style=\" font-weight:600;\">N</span> - количество компьютеров</p><p><span style=\" font-weight:600;\">S</span> - потери от 1 неисправного компьютера в час (в рублях)</p><p><span style=\" font-weight:600;\">S</span><span style=\" font-weight:600; vertical-align:sub;\">i</span> - зарплата 1 сотрудника в час (в рублях)<br/></p><p><span style=\" font-weight:600;\">Выходные значения:</span></p><p><span style=\" font-weight:600;\">Q - </span>среднее число компьютеров, находящихся в очереди</p><p><span style=\" font-weight:600;\">L</span> - среднее число компьютеров в очереди на ремонт и в ремонте</p><p><span style=\" font-weight:600;\">U - </span>среднее число ремонтируемых компьютеров</p><p><span style=\" font-weight:600;\">ρ</span><span style=\" font-weight:600; vertical-align:sub;\">0</span><span style=\" font-weight:600;\"> - </span>коэффициент загрузки одного специалиста</p><p><span style=\" font-weight:600;\">n - </span>среднее количество исправных компьютеров</p><p><span style=\" font-weight:600;\">ρ</span><span style=\" font-weight:600; vertical-align:sub;\">e</span><span style=\" font-weight:600;\"> - </span>коэффициент загрузки компьютера, т.е. долz времени, в течение которого он находится в исправном состоянии</p><p><span style=\" font-weight:600;\">W - </span>среднее время нахождения компьютера в очереди на ремонт (в часах)</p><p><span style=\" font-weight:600;\">T</span><span style=\" font-weight:600; vertical-align:sub;\">Р</span> - среднее время пребывания компьютера в неисправном состоянии (в часах)</p><p><span style=\" font-weight:600;\">T</span><span style=\" font-weight:600; vertical-align:sub;\">Ц</span> - среднее время цикла компьютера (в часах)</p><p><span style=\" font-weight:600;\">ρ</span><span style=\" font-weight:600; vertical-align:sub;\">e</span><span style=\" font-weight:600;\">/ρ</span><span style=\" font-weight:600; vertical-align:sub;\">o</span> - отношение загрузки специалиствов и компьютеров</p><p><span style=\" font-weight:600;\">Y</span> - финансовые затраты (в рублях) </p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Описание работы"))
        self.calc_pushButton.setText(_translate("MainWindow", "Произвести расчет"))
        self.c_lineEdit.setText(_translate("MainWindow", "1"))
        self.s_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">S</span></p></body></html>"))
        self.si_lineEdit.setText(_translate("MainWindow", "200"))
        self.c_label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Число ремонтиков</p></body></html>"))
        self.c_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">C</span></p></body></html>"))
        self.to_lineEdit.setText(_translate("MainWindow", "8"))
        self.to_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">t</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">O</span></p></body></html>"))
        self.c3_lineEdit.setText(_translate("MainWindow", "3"))
        self.n_lineEdit.setText(_translate("MainWindow", "100"))
        self.s_lineEdit.setText(_translate("MainWindow", "350"))
        self.c2_lineEdit.setText(_translate("MainWindow", "2"))
        self.si_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">S</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">i</span></p></body></html>"))
        self.n_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">N</span></p></body></html>"))
        self.tno_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">t</span><span style=\" font-weight:600; vertical-align:sub;\">н.о.</span></p></body></html>"))
        self.tno_lineEdit.setText(_translate("MainWindow", "800"))
        self.c_info_label.setText(_translate("MainWindow", "(чел.)"))
        self.label.setText(_translate("MainWindow", "(часов)"))
        self.label_3.setText(_translate("MainWindow", "(часов)"))
        self.label_4.setText(_translate("MainWindow", "(шт.)"))
        self.label_5.setText(_translate("MainWindow", "(руб/час)"))
        self.label_6.setText(_translate("MainWindow", "(руб/час)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ввод параметров"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "C"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "P0"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Q"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "L"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "U=L-Q"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "ρ0=U/C"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "n=L-C"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "ρe=n/N"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "W"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Tp"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Tц"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "ρe/ρ0"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Y"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "B1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "B3"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.choice_label.setText(_translate("MainWindow", "Предпочтительный вариант:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Результаты"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

