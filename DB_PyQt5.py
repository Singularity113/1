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

        grid_layout.addWidget(self.tableWidget, 0, 0, N, 1)

        self.btn = QPushButton(self)
        self.btn.setText('&Обновить')
        self.btn.setFixedWidth(300)
        self.btn.setStyleSheet('background-color: DeepSkyBlue')
        grid_layout.addWidget(self.btn, 0, 1, Qt.AlignTop)
        self.btn.clicked.connect(self.update)

        self.lbl_name1 = QLabel(self)
        self.lbl_name1.setText('Добавление в корзину')
        self.lbl_name1.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_name1, 5, 1)

        self.lbl_name = QLabel(self)
        self.lbl_name.setText('Введите наименование продукта:')
        self.lbl_name.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_name, 6, 1)

        self.e_name = QLineEdit(self)
        self.e_name.setFixedWidth(300)
        grid_layout.addWidget(self.e_name, 7, 1)

        self.btn_pack = QPushButton(self)
        self.btn_pack.setText('&Добавить в корзину')
        self.btn_pack.setFixedWidth(300)
        grid_layout.addWidget(self.btn_pack, 8, 1)

        self.btn_sell = QPushButton(self)
        self.btn_sell.setText('&Совершить покупку')
        self.btn_sell.setFixedWidth(300)
        grid_layout.addWidget(self.btn_sell, 9, 1)

        self.lbl_category = QLabel(self)
        self.lbl_category.setText('Поиск по категории')
        self.lbl_category.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_category, 1, 1)

        self.lbl_find = QLabel(self)
        self.lbl_find.setText('Введите категорию')
        self.lbl_find.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_find, 2, 1)

        self.e_find = QLineEdit(self)
        self.e_find.setFixedWidth(300)
        grid_layout.addWidget(self.e_find, 3, 1)

        self.btn_find = QPushButton(self)
        self.btn_find.setText('&Найти')
        self.btn_find.setFixedWidth(300)
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

        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\products.db')
        self.cur = self.db.cursor()

        self.cur.execute("""BEGIN""")  
        N = self.cur.execute("""SELECT COUNT() FROM products""").fetchone()[0]
        allrows = self.cur.execute("""SELECT * FROM products""").fetchall()
        self.cur.connection.commit()  
        assert N == len(allrows)
        self.tableWidget = QTableWidget()
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

        grid_layout.addWidget(self.tableWidget, 0, 0, N, 1)

        self.lbl_add  = QLabel(self)
        self.lbl_add.setText('Добавление')
        self.lbl_add.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_add, 0, 1)

        self.lbl_name = QLabel(self)
        self.lbl_name.setText('Введите наименование:')
        self.lbl_name.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_name, 1, 1)

        self.e_name = QLineEdit(self)
        self.e_name.setFixedWidth(300)
        grid_layout.addWidget(self.e_name, 2, 1)

        self.lbl_category = QLabel(self)
        self.lbl_category.setText('Введите категорию:')
        self.lbl_category.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_category, 3, 1)

        self.e_category = QLineEdit(self)
        self.e_category.setFixedWidth(300)
        grid_layout.addWidget(self.e_category, 4, 1)

        self.lbl_count = QLabel(self)
        self.lbl_count.setText('Введите количество:')
        self.lbl_count.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_count, 5, 1)

        self.e_count = QLineEdit(self)
        self.e_count.setFixedWidth(300)
        grid_layout.addWidget(self.e_count, 6, 1)

        self.lbl_cost = QLabel(self)
        self.lbl_cost.setText('Введите цену:')
        self.lbl_cost.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_cost, 7, 1)

        self.e_cost = QLineEdit(self)
        self.e_cost.setFixedWidth(300)
        grid_layout.addWidget(self.e_cost, 8, 1)

        self.btn = QPushButton('Сохранить')
        self.btn.setFixedWidth(300)
        grid_layout.addWidget(self.btn, 9, 1)
        self.btn.clicked.connect(self.add)

        self.lbl_del1  = QLabel(self)
        self.lbl_del1.setText('Удаление')
        self.lbl_del1.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_del1, 10, 1)

        self.lbl_del  = QLabel(self)
        self.lbl_del.setText('Введите наименование:')
        self.lbl_del.setFixedWidth(300)
        grid_layout.addWidget(self.lbl_del, 11, 1)

        self.e_del = QLineEdit(self)
        self.e_del.setFixedWidth(300)
        grid_layout.addWidget(self.e_del, 12, 1)

        self.btn_del = QPushButton('Удалить')
        self.btn_del.setFixedWidth(300)
        grid_layout.addWidget(self.btn_del, 13, 1)
        self.btn_del.clicked.connect(self.dl)

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
        self.update()

    def dl(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\products.db')
        self.cur = self.db.cursor()

        value = [self.e_del.text()]
        self.cur.execute("""DELETE FROM products WHERE name=?""", value)
        self.db.commit()

        self.e_del.clear()

        self.db.close()
        self.update()

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
            self.w2 = Window2()
            self.w2.showMaximized()
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