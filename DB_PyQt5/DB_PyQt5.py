import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Продавец')
    
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\products.db')
        self.cur = self.db.cursor()

        self.cur.execute("""BEGIN""")  
        N = self.cur.execute("""SELECT COUNT() FROM products""").fetchone()[0]
        allrows = self.cur.execute("""SELECT * FROM products""").fetchall()
        self.cur.connection.commit()  
        assert N == len(allrows)
        self.tableWidget = QTableWidget()
        QTableWidget.resizeColumnsToContents(self.tableWidget)
        QTableWidget.resizeRowsToContents(self.tableWidget)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(N)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setHorizontalHeaderLabels(['Наименование','Категория','Количество','Цена'])

        self.cur.execute("""SELECT * FROM products""")
        items = self.cur.fetchall()
        row = 0
        col = 0
        for row in range(N):
            for col in range(4):
                self.tableWidget.setItem(row,col, QTableWidgetItem(str(items[row][col])))

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        grid_layout.addWidget(self.tableWidget, 0, 0)

        self.btn = QPushButton(self)
        self.btn.setText('&Обновить')
        grid_layout.addWidget(self.btn, 0, 1, Qt.AlignTop)
        self.btn.clicked.connect(self.update)

        self.lbl_name1 = QLabel(self)
        self.lbl_name1.setText('Введите наименование продукта для добавления в корзину')
        grid_layout.addWidget(self.lbl_name1, 1, 0)

        self.e_name = QLineEdit(self)
        grid_layout.addWidget(self.e_name, 2, 0)

        self.btn_pack = QPushButton(self)
        self.btn_pack.setText('&Добавить в корзину')
        grid_layout.addWidget(self.btn_pack, 3, 0)

        self.btn_sell = QPushButton(self)
        self.btn_sell.setText('&Совершить покупку')
        grid_layout.addWidget(self.btn_sell, 4, 0)

        self.lbl_category = QLabel(self)
        self.lbl_category.setText('Поиск по категории')
        grid_layout.addWidget(self.lbl_category, 1, 1)

        self.lbl_find = QLabel(self)
        self.lbl_find.setText('Введите категорию')
        grid_layout.addWidget(self.lbl_find, 2, 1)

        self.e_find = QLineEdit(self)
        grid_layout.addWidget(self.e_find, 3, 1)

        self.btn_find = QPushButton(self)
        self.btn_find.setText('&Найти')
        grid_layout.addWidget(self.btn_find, 4, 1)
        self.btn_find.clicked.connect(self.find_cat)

        self.db.close()

    def update(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\products.db')
        self.cur = self.db.cursor()

        self.cur.execute("""BEGIN""")  
        N = self.cur.execute("""SELECT COUNT() FROM products""").fetchone()[0]
        allrows = self.cur.execute("""SELECT * FROM products""").fetchall()
        self.cur.connection.commit()  
        assert N == len(allrows)
        self.tableWidget.setRowCount(N)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setHorizontalHeaderLabels(['Наименование','Категория','Количество','Цена'])

        self.cur.execute("""SELECT * FROM products""")
        items = self.cur.fetchall()
        row = 0
        col = 0
        for row in range(N):
            for col in range(4):
                self.tableWidget.setItem(row,col, QTableWidgetItem(str(items[row][col])))

        self.db.close()

    def find_cat(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\products.db')
        self.cur = self.db.cursor()

        value_cat = [self.e_find.text()]

        self.cur.execute("""BEGIN""")  
        N = self.cur.execute("""SELECT COUNT() FROM products WHERE category=?""", value_cat).fetchone()[0]
        allrows = self.cur.execute("""SELECT * FROM products WHERE category=?""", value_cat).fetchall()
        self.cur.connection.commit()  
        assert N == len(allrows)
        self.tableWidget.setRowCount(N)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.clearContents()

        self.tableWidget.setHorizontalHeaderLabels(['Наименование','Категория','Количество','Цена'])

        self.cur.execute("""SELECT * FROM products WHERE category=?""", value_cat)
        items = self.cur.fetchall()
        row = 0
        col = 0
        for row in range(N):
            for col in range(4):
                self.tableWidget.setItem(row,col, QTableWidgetItem(str(items[row][col])))

        self.e_find.clear()

        self.db.close()

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Кладовщик')
        self.setFixedSize(500,500)

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.lbl_add  = QLabel(self)
        self.lbl_add.setText('Добавление')
        grid_layout.addWidget(self.lbl_add, 0, 0)

        self.lbl_name = QLabel(self)
        self.lbl_name.setText('Введите наименование:')
        grid_layout.addWidget(self.lbl_name, 1, 0, 1, 1)

        self.e_name = QLineEdit(self)
        grid_layout.addWidget(self.e_name, 1, 1, 1, 1)

        self.lbl_category = QLabel(self)
        self.lbl_category.setText('Введите категорию:')
        grid_layout.addWidget(self.lbl_category, 2, 0, 1, 1)

        self.e_category = QLineEdit(self)
        grid_layout.addWidget(self.e_category, 2, 1, 1, 1)

        self.lbl_count = QLabel(self)
        self.lbl_count.setText('Введите количество:')
        grid_layout.addWidget(self.lbl_count, 3, 0, 1, 1)

        self.e_count = QLineEdit(self)
        grid_layout.addWidget(self.e_count, 3, 1, 1, 1)

        self.lbl_cost = QLabel(self)
        self.lbl_cost.setText('Введите цену:')
        grid_layout.addWidget(self.lbl_cost, 4, 0, 1, 1)

        self.e_cost = QLineEdit(self)
        grid_layout.addWidget(self.e_cost, 4, 1, 1, 1)

        self.btn = QPushButton('Сохранить')
        grid_layout.addWidget(self.btn, 5, 0, 1, 2)
        self.btn.clicked.connect(self.add)

        self.lbl_del  = QLabel(self)
        self.lbl_del.setText('Удаление')
        grid_layout.addWidget(self.lbl_del, 6, 0)

        self.lbl_del = QLabel(self)
        self.lbl_del.setText('Введите наименование:')
        grid_layout.addWidget(self.lbl_del, 7, 0, 1, 1)

        self.e_del = QLineEdit(self)
        grid_layout.addWidget(self.e_del, 7, 1, 1, 1)

        self.btn_del = QPushButton('Удалить')
        grid_layout.addWidget(self.btn_del, 8, 0, 1, 2)
        self.btn_del.clicked.connect(self.dl)

    def add(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\products.db')
        self.cur = self.db.cursor()

        values = [(self.e_name.text(), self.e_category.text(), self.e_count.text(), self.e_cost.text())]

        self.cur.executemany("""INSERT INTO products VALUES(?,?,?,?);""", values)
        self.db.commit()

        self.e_name.clear()
        self.e_category.clear()
        self.e_count.clear()
        self.e_cost.clear()

        self.db.close()

    def dl(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\products.db')
        self.cur = self.db.cursor()

        value = [self.e_del.text()]
        self.cur.execute("""DELETE FROM products WHERE name=?""", value)
        self.db.commit()

        self.e_del.clear()

        self.db.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(500,200)
        self.setWindowTitle('Аунтификация')

        self.lbl_name = QLabel(self)
        self.lbl_name.setText('Логин:')
        self.lbl_name.move(120,10)
        self.lbl_name.show()

        self.e_name = QLineEdit(self)
        self.e_name.move(190,5)
        self.e_name.show()

        self.lbl_pass = QLabel(self)
        self.lbl_pass.setText('Пароль:')
        self.lbl_pass.move(120,40)
        self.lbl_pass.show()

        self.e_pass = QLineEdit(self)
        self.e_pass.setEchoMode(QLineEdit.Password)
        self.e_pass.move(190,35)
        self.e_pass.show()

        self.btn = QPushButton(self)
        self.btn.setText('&Войти')
        self.btn.move(210,165)
        self.btn.show()
        self.btn.clicked.connect(self.auntific)

    def auntific(self):
        if self.e_name.text() == '01' and self.e_pass.text() == '01':
            self.w1 = Window1()
            self.w1.showMaximized()
            win.close()
        elif self.e_name.text() == '02' and self.e_pass.text() == '02':
            self.w1 = Window1()
            self.w1.showMaximized()
            self.w2 = Window2()
            self.w2.show()
            win.close()
        else: 
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText('Введены не верные логин/пароль')
            self.msg.setInformativeText('Попытайтесь снова')
            self.msg.setWindowTitle('Ошибка!')
            self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.msg.exec_()
            self.e_name.clear()
            self.e_pass.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())