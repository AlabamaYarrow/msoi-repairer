import sys
from math import factorial as fact, pow

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QAbstractItemView, QApplication,
                             QDialog, QTableWidgetItem, QMessageBox)

from ui_dialog import Ui_MainWindow


class UserInput:
    def __init__(self, to, tno, n, c, c2, c3, s, si):
        self.to = to
        self.tno = tno
        self.n = n
        self.c = c
        self.c2 = c2
        self.c3 = c3
        self.s = s
        self.si = si

    def is_valid(self):
        try:
            self.to = float(self.to)
            self.tno = float(self.tno)
            self.n = int(self.n)
            self.c = int(self.c)
            self.c2 = int(self.c2)
            self.c3 = int(self.c3)
            self.s = float(self.s)
            self.si = float(self.si)
            if any([self.to <= 0, self.tno <= 0, self.n <= 0, self.c <= 0,
                    self.c2 <= 0, self.c3 <= 0, self.s <= 0, self.si <= 0]):
                raise ValueError
        except ValueError:
            return False
        return True


class MainWindow(QDialog, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.input = None
        self.output = {}
        self.setupUi(self)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.calc_pushButton.clicked.connect(self.start_calculation)

    def show_error(self, *args):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Неверные входные параметры")
        msg.setInformativeText("Проверьте введенные значения")
        msg.setWindowTitle("Ошибка ввода")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def start_calculation(self):
        self.input = UserInput(
            self.to_lineEdit.text(), self.tno_lineEdit.text(),
            self.n_lineEdit.text(), self.c_lineEdit.text(),
            self.c2_lineEdit.text(), self.c3_lineEdit.text(),
            self.s_lineEdit.text(), self.si_lineEdit.text(),
        )
        if not self.input.is_valid():
            self.show_error()
        else:
            self.calculate()
        self.input = None

    def calculate(self):
        c_vals = [self.input.c, self.input.c2, self.input.c3]
        y_vals = []
        for alternative_num in range(0, len(c_vals)):
            self.output = {}
            c = c_vals[alternative_num]

            self.set_output_values(c)
            y_vals.append(self.output['y'])

            table_column = [c, self.output['p0'], self.output['q'], self.output['l'],
                            self.output['u'], self.output['ro'], self.output['n_avg'], self.output['roe'],
                            self.output['w'], self.output['tp'], self.output['tc'], self.output['roe_to_ro'],
                            round(self.output['y'], 1)]
            for i in range(0, self.tableWidget.rowCount()):
                self.tableWidget.setItem(i, alternative_num,  QTableWidgetItem(str(round(table_column[i], 5))))

        min_y = y_vals.index(min(y_vals))

        self.tableWidget.item(self.tableWidget.rowCount() - 1, min_y).setBackground(QColor(100, 150, 100))
        self.choice_val_label.setText('B' + str(min_y + 1))

        self.tabWidget.setCurrentIndex(2)

    def set_probalilities(self, c):
        psi = self.input.to / self.input.tno
        # вероятность пребывания в состоянии о
        p0 = 0
        for k in range(0, c + 1):
            p0 += (fact(self.input.n) * pow(psi, k)) \
                  / (fact(k) * fact(self.input.n - k))
        for k in range(c + 1, self.input.n + 1):
            p0 += (fact(self.input.n) * pow(psi, k)) \
                  / (pow(c, k - c) * fact(c) * fact(self.input.n - k))
        p0 = 1 / p0
        self.output['p0'] = p0

        # вероятности пребывания в состоянии отказа
        pks = []
        for k in range(1, c + 1):
            pks.append(
                (p0 * fact(self.input.n) * pow(psi, k)) /
                (fact(k) * fact(self.input.n - k))
            )
        for k in range(c + 1, self.input.n + 1):
            pks.append(
                (p0 * fact(self.input.n) * pow(psi, k)) /
                (pow(c, k - c) * fact(c) * fact(self.input.n - k))
            )
        return pks

    def set_output_values(self, c):
        pks = self.set_probalilities(c)
        q = 0
        for k in range(c, self.input.n + 1):
            q += (k - c) * pks[k - 1]
        self.output['q'] = q
        l = 0
        for k in range(1, self.input.n + 1):
            l += k * pks[k - 1]
        # неисправные компьютеры
        self.output['l'] = l
        # ремонтируемые компьютеры
        self.output['u'] = self.output['l'] - self.output['q']
        # загрузка одного специалиста
        self.output['ro'] = self.output['u'] / c
        # среднее время в ремонте (очередь + время ремонта)
        self.output['tp'] = (self.output['l'] * self.input.tno) \
                            / (self.input.n - self.output['l'])
        # среднее время нахождения в очереди на ремонт
        self.output['w'] = self.output['tp'] - self.input.to
        # среднее время цикла компьютера
        self.output['tc'] = self.output['tp'] + self.input.tno
        # коэффициент загрузки компьютера (время в исправном состоянии)
        self.output['roe'] = self.input.tno / self.output['tc']
        # среднее число исправных компьютеров
        self.output['n_avg'] = self.input.n - self.output['l']
        # режим работы (отношение исправен-ремонтируется)
        self.output['roe_to_ro'] = (c * self.input.tno) / (self.input.n * self.input.to)
        # затраты
        self.output['y'] = c * self.input.si + self.output['l'] * self.input.s


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
