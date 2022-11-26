import sqlite3
import sys
import re
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt_material import apply_stylesheet

class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('ИС для учета вычислительной техники и орг. техники')
    
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.cur.execute("""BEGIN""")  
        N = self.cur.execute("""SELECT COUNT() FROM NewProducts""").fetchone()[0]
        allrows = self.cur.execute("""SELECT * FROM NewProducts""").fetchall()
        self.cur.connection.commit()  
        assert N == len(allrows)
        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(N)
        self.tableWidget.setColumnCount(5)
        
        self.tableWidget.setHorizontalHeaderLabels(['id','Наименование','Категория','Количество','Цена'])

        self.cur.execute("""SELECT * FROM NewProducts""")
        items = self.cur.fetchall()
        for i in range(N):
            for j in range(5):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(items[i][j])))
                if j == 2:
                    cat_id = items[i][2]
                    self.db_c = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Category.db')
                    self.cur_c = self.db_c.cursor()
                    self.cur_c.execute(f"""SELECT name FROM Category WHERE id_c={cat_id}""")
                    name_c = self.cur_c.fetchone()
                    n_c = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(name_c))
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(n_c)))
        self.tableWidget.resizeColumnsToContents()

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        grid_layout.addWidget(self.tableWidget, 0, 0, N, 1)

        self.btn = QPushButton(self)
        self.btn.setText('&Показать всю таблицу')
        self.btn.setFixedWidth(220)
        grid_layout.addWidget(self.btn, 0, 1, Qt.AlignTop)
        self.btn.clicked.connect(self.update)

        self.btn_find = QPushButton(self)
        self.btn_find.setText('&Найти категорию')
        self.btn_find.setFixedWidth(220)
        grid_layout.addWidget(self.btn_find, 1, 1)
        self.btn_find.clicked.connect(self.find_cat)

        self.btn_pack = QPushButton(self)
        self.btn_pack.setText('&Добавить в корзину')
        self.btn_pack.setFixedWidth(220)
        grid_layout.addWidget(self.btn_pack, 2, 1)
        self.btn_pack.clicked.connect(self.trash)

        self.btn_see = QPushButton(self)
        self.btn_see.setText('&Просмотреть корзину')
        self.btn_see.setFixedWidth(220)
        grid_layout.addWidget(self.btn_see, 3, 1)
        self.btn_see.clicked.connect(self.look)

        self.btn_p = QPushButton(self)
        self.btn_p.setText('&Увеличить количество')
        self.btn_p.setFixedWidth(220)
        grid_layout.addWidget(self.btn_p, 4, 1)
        self.btn_p.clicked.connect(self.plus)
        self.btn_p.setEnabled(False)

        self.btn_m = QPushButton(self)
        self.btn_m.setText('&Уменьшить количество')
        self.btn_m.setFixedWidth(220)
        grid_layout.addWidget(self.btn_m, 5, 1)
        self.btn_m.clicked.connect(self.minus)
        self.btn_m.setEnabled(False)

        self.btn_dell = QPushButton(self)
        self.btn_dell.setText('&Удалить из корзины')
        self.btn_dell.setFixedWidth(220)
        grid_layout.addWidget(self.btn_dell, 6, 1)
        self.btn_dell.clicked.connect(self.dell)
        self.btn_dell.setEnabled(False)

        self.btn_sell = QPushButton(self)
        self.btn_sell.setText('&Совершить покупку')
        self.btn_sell.setFixedWidth(220)
        grid_layout.addWidget(self.btn_sell, 7, 1)
        self.btn_sell.clicked.connect(self.sell)
        self.btn_sell.setEnabled(False)

        self.db.close()

    def update(self):
        self.btn_pack.setEnabled(True)
        self.btn_find.setEnabled(True)
        self.btn_see.setEnabled(True)
        self.btn_p.setEnabled(False)
        self.btn_m.setEnabled(False)
        self.btn_dell.setEnabled(False)
        self.btn_sell.setEnabled(False)

        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.cur.execute("""BEGIN""")  
        N = self.cur.execute("""SELECT COUNT() FROM NewProducts""").fetchone()[0]
        allrows = self.cur.execute("""SELECT * FROM NewProducts""").fetchall()
        self.cur.connection.commit()  
        assert N == len(allrows)
        self.tableWidget.setRowCount(N)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setHorizontalHeaderLabels(['id','Наименование','Категория','Количество','Цена'])

        self.cur.execute("""SELECT * FROM NewProducts""")
        items = self.cur.fetchall()
        for i in range(N):
            for j in range(5):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(items[i][j])))
                if j == 2:
                    cat_id = items[i][2]
                    self.db_c = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Category.db')
                    self.cur_c = self.db_c.cursor()
                    self.cur_c.execute(f"""SELECT name FROM Category WHERE id_c={cat_id}""")
                    name_c = self.cur_c.fetchone()
                    n_c = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(name_c))
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(n_c)))
        self.tableWidget.resizeColumnsToContents()

        self.db.close()

    def find_cat(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.db_c = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Category.db')
        self.cur_c = self.db_c.cursor()
        
        value_cat = self.tableWidget.model().data(self.tableWidget.currentIndex())

        self.cur_c.execute(f"""SELECT * FROM Category WHERE name='{value_cat}'""")
        self.i_c = self.cur_c.fetchall()[0][0]

        self.cur.execute("""BEGIN""")  
        N = self.cur.execute(f"""SELECT COUNT() FROM NewProducts WHERE id_c={self.i_c}""").fetchone()[0]
        allrows = self.cur.execute(f"""SELECT * FROM NewProducts WHERE id_c={self.i_c}""").fetchall()
        self.cur.connection.commit()  
        assert N == len(allrows)
        self.tableWidget.setRowCount(N)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.clearContents()

        self.tableWidget.setHorizontalHeaderLabels(['id','Наименование','Категория','Количество','Цена'])

        self.cur.execute(f"""SELECT * FROM NewProducts WHERE id_c={self.i_c}""")
        items = self.cur.fetchall()
        for i in range(N):
            for j in range(5):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(items[i][j])))
                if j == 2:
                    cat_id = items[i][2]
                    self.cur_c.execute(f"""SELECT name FROM Category WHERE id_c='{cat_id}'""")
                    name_c = self.cur_c.fetchone()
                    n_c = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(name_c))
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(n_c)))
        self.tableWidget.resizeColumnsToContents()

        self.db.close()

    def trash(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.value_id = self.tableWidget.model().data(self.tableWidget.currentIndex())
        self.prod_name = self.cur.execute(f"""SELECT name FROM NewProducts WHERE id_prod='{self.value_id}'""").fetchone()
        self.prod_cost = self.cur.execute(f"""SELECT cost FROM NewProducts WHERE id_prod='{self.value_id}'""").fetchone()

        self.db.commit() 
        self.db.close()
        
        self.db_o = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Order.db')
        self.cur_o = self.db_o.cursor()

        self.prod_name = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(self.prod_name))
        self.prod_cost = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(self.prod_cost))

        self.cur_o.execute(f"""INSERT INTO Orders(id_prod,name,count,cost) VALUES({self.value_id},'{self.prod_name}',1,{self.prod_cost})""")
        self.db_o.commit()
        self.db_o.close()
        
    def look(self):
        self.btn_p.setEnabled(True)
        self.btn_m.setEnabled(True)
        self.btn_dell.setEnabled(True)
        self.btn_sell.setEnabled(True)
        self.btn_pack.setEnabled(False)
        self.btn_find.setEnabled(False)
        self.btn_see.setEnabled(False)

        self.db_o = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Order.db')
        self.cur_o = self.db_o.cursor()

        self.cur_o.execute("""BEGIN""")  
        N = self.cur_o.execute("""SELECT COUNT() FROM Orders""").fetchone()[0]
        allrows = self.cur_o.execute("""SELECT * FROM Orders""").fetchall()
        self.cur_o.connection.commit()  
        assert N == len(allrows)
        self.tableWidget.setRowCount(N)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setHorizontalHeaderLabels(['ID','Наименование','Количество','Цена'])

        self.total = self.cur_o.execute("""SELECT TOTAL(cost) FROM Orders""").fetchone()[0]

        self.cur_o.execute("""SELECT * FROM Orders""")
        items = self.cur_o.fetchall()
        for i in range(N):
            for j in range(4):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(items[i][j])))
        self.tableWidget.resizeColumnsToContents()

        self.db_o.close()

    def plus(self):
        self.db_o = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Order.db')
        self.cur_o = self.db_o.cursor()

        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.v_id = self.tableWidget.model().data(self.tableWidget.currentIndex())
        self.cur.execute(f"""SELECT cost FROM NewProducts WHERE id_prod={self.v_id}""")
        self.cost = self.cur.fetchall()
        self.cost = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(self.cost))
        self.cur_o.execute(f"""UPDATE Orders set count=count+1 WHERE id_prod={self.v_id}""")
        self.cur_o.execute(f"""UPDATE Orders set cost=cost+{self.cost} WHERE id_prod={self.v_id}""")
        self.db_o.commit()

        self.look()
        
        self.db.close()
        self.db_o.close()

    def minus(self):
        self.db_o = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Order.db')
        self.cur_o = self.db_o.cursor()

        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.v_id = self.tableWidget.model().data(self.tableWidget.currentIndex())
        self.cur.execute(f"""SELECT cost FROM NewProducts WHERE id_prod={self.v_id}""")
        self.cost = self.cur.fetchall()
        self.cost = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(self.cost))
        self.cur_o.execute(f"""UPDATE Orders set count=count-1 WHERE id_prod={self.v_id}""")
        self.cur_o.execute(f"""UPDATE Orders set cost=cost-{self.cost} WHERE id_prod={self.v_id}""")

        self.cur_o.execute(f"""DELETE FROM Orders WHERE count=0""")
        self.db_o.commit()

        self.look()

        self.db.close()
        self.db_o.close()

    def dell(self):
        self.db_o = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Order.db')
        self.cur_o = self.db_o.cursor()

        self.d_id = self.tableWidget.model().data(self.tableWidget.currentIndex())
        self.cur_o.execute(f"""DELETE FROM Orders WHERE id_prod={self.d_id}""")
        self.db_o.commit()

        self.db_o.close()
        self.look()
        
    def sell(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.db_o = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Order.db')
        self.cur_o = self.db_o.cursor()

        self.db_all = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\AllOrders.db')
        self.cur_all = self.db_all.cursor()

        self.cur_o.execute("""SELECT * FROM Orders""")
        items = self.cur_o.fetchall()

        self.cur_o.execute("""BEGIN""")  
        N = self.cur_o.execute("""SELECT COUNT() FROM Orders""").fetchone()[0]
        allrows = self.cur_o.execute("""SELECT * FROM Orders""").fetchall()
        self.cur_o.connection.commit()  
        assert N == len(allrows)

        self.date = datetime.datetime.today()
        self.data0 = self.date.strftime("%Y-%m-%d(%H:%M)")

        for i in range(N):
            self.cur.execute(f"""UPDATE NewProducts set count=count-{items[i][2]} WHERE id_prod={items[i][0]}""")
            self.cur_all.execute(f"""INSERT INTO AllOrders(id_prod, name, count, cost, date) VALUES({items[i][0]},'{items[i][1]}',{items[i][2]},{items[i][3]},'{self.data0}')""")
        self.db.commit()
        self.db_all.commit()

        self.cur_o.execute("""DELETE FROM Orders""")
        self.db_o.commit()

        self.look()
        self.db.close()
        self.db_all.close()
        self.db_o.close()

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('ИС для учета вычислительной техники и орг. техники')

        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.cur.execute("""BEGIN""")  
        N = self.cur.execute("""SELECT COUNT() FROM NewProducts""").fetchone()[0]
        allrows = self.cur.execute("""SELECT * FROM NewProducts""").fetchall()
        self.cur.connection.commit()  
        assert N == len(allrows)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(N)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setHorizontalHeaderLabels(['ID','Наименование','Категория','Количество','Цена'])

        self.cur.execute("""SELECT * FROM NewProducts""")
        items = self.cur.fetchall()
        for i in range(N):
            for j in range(5):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(items[i][j])))
                if j == 2:
                    cat_id = items[i][2]
                    self.db_c = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Category.db')
                    self.cur_c = self.db_c.cursor()
                    self.cur_c.execute(f"""SELECT name FROM Category WHERE id_c={cat_id}""")
                    name_c = self.cur_c.fetchone()
                    n_c = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(name_c))
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(n_c)))
        self.tableWidget.resizeColumnsToContents()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        grid_layout.addWidget(self.tableWidget, 0, 0, N, 1)

        self.lbl_add  = QLabel(self)
        self.lbl_add.setText('Добавление')
        self.lbl_add.setFixedWidth(240)
        grid_layout.addWidget(self.lbl_add, 0, 1)

        self.lbl_name = QLabel(self)
        self.lbl_name.setText('Введите наименование:')
        self.lbl_name.setFixedWidth(240)
        grid_layout.addWidget(self.lbl_name, 1, 1)

        self.e_name = QLineEdit(self)
        self.e_name.setFixedWidth(240)
        grid_layout.addWidget(self.e_name, 2, 1)

        self.lbl_category = QLabel(self)
        self.lbl_category.setText('Введите категорию:')
        self.lbl_category.setFixedWidth(240)
        grid_layout.addWidget(self.lbl_category, 3, 1)

        self.e_category = QLineEdit(self)
        self.e_category.setFixedWidth(240)
        grid_layout.addWidget(self.e_category, 4, 1)

        self.lbl_count = QLabel(self)
        self.lbl_count.setText('Введите количество:')
        self.lbl_count.setFixedWidth(240)
        grid_layout.addWidget(self.lbl_count, 5, 1)

        self.e_count = QLineEdit(self)
        self.e_count.setFixedWidth(240)
        grid_layout.addWidget(self.e_count, 6, 1)

        self.lbl_cost = QLabel(self)
        self.lbl_cost.setText('Введите цену:')
        self.lbl_cost.setFixedWidth(240)
        grid_layout.addWidget(self.lbl_cost, 7, 1)

        self.e_cost = QLineEdit(self)
        self.e_cost.setFixedWidth(240)
        grid_layout.addWidget(self.e_cost, 8, 1)

        self.btn = QPushButton('&Сохранить')
        self.btn.setFixedWidth(240)
        grid_layout.addWidget(self.btn, 9, 1)
        self.btn.clicked.connect(self.add)

        self.btn_del = QPushButton('&Удалить')
        self.btn_del.setFixedWidth(240)
        grid_layout.addWidget(self.btn_del, 10, 1)
        self.btn_del.clicked.connect(self.dl)

        self.btn_re = QPushButton('&Сохранить редактирование')
        self.btn_re.setFixedWidth(240)
        grid_layout.addWidget(self.btn_re, 11, 1)
        # self.btn_re.clicked.connect(self.rewrite)

        self.db.close()

    def update(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.cur.execute("""BEGIN""")  
        N = self.cur.execute("""SELECT COUNT() FROM NewProducts""").fetchone()[0]
        allrows = self.cur.execute("""SELECT * FROM NewProducts""").fetchall()
        self.cur.connection.commit()  
        assert N == len(allrows)
        self.tableWidget.setRowCount(N)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setHorizontalHeaderLabels(['ID','Наименование','Категория','Количество','Цена'])

        self.cur.execute("""SELECT * FROM NewProducts""")
        items = self.cur.fetchall()
        for i in range(N):
            for j in range(5):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(items[i][j])))
                if j == 2:
                    cat_id = items[i][2]
                    self.db_c = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Category.db')
                    self.cur_c = self.db_c.cursor()
                    self.cur_c.execute(f"""SELECT name FROM Category WHERE id_c={cat_id}""")
                    name_c = self.cur_c.fetchone()
                    n_c = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(name_c))
                    self.tableWidget.setItem(i,j, QTableWidgetItem(str(n_c)))
        self.tableWidget.resizeColumnsToContents()

        self.db.close()

    def add(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.db_c = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Category.db')
        self.cur_c = self.db_c.cursor()

        id_cat = self.cur_c.execute(f"""SELECT id_c FROM Category WHERE name='{self.e_category.text()}'""").fetchone()
        id_cat = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(id_cat))

        if id_cat == None:
            self.cur_c.execute(f"""INSERT INTO Category(name) VALUES('{self.e_category.text()}')""")
            self.db_c.commit()
            id_cat = self.cur_c.execute(f"""SELECT id_c FROM Category WHERE name='{self.e_category.text()}'""").fetchone()
            id_cat = re.sub("[^A-Za-z0-9-^А-Яа-я- ]", "", str(id_cat))
            self.cur.execute(f"""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('{self.e_name.text()}',{id_cat},{self.e_count.text()},{self.e_cost.text()})""")
            self.db.commit()
        else:
            self.cur.execute(f"""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('{self.e_name.text()}',{id_cat},{self.e_count.text()},{self.e_cost.text()})""")
            self.db.commit()

        self.e_name.clear()
        self.e_category.clear()
        self.e_count.clear()
        self.e_cost.clear()

        self.db_c.close()
        self.db.close()
        self.update()

    def dl(self):
        self.db = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
        self.cur = self.db.cursor()

        self.value = self.tableWidget.model().data(self.tableWidget.currentIndex())
        self.cur.execute("""DELETE FROM NewProducts WHERE id_prod=?""", self.value)
        self.db.commit()

        self.db.close()
        self.update()
#########def rewrite(self):
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(500,220)
        self.setWindowTitle('Аутентификация')

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
    apply_stylesheet(app, theme='dark_cyan.xml')
    win.show()
    # sys.__excepthook__ = sys.excepthook
    # def my_exeption_hook(exctype, value, traceback):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #     msg.setText('Введены не верные данные')
    #     msg.setWindowTitle('Ошибка!')
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     msg.exec_()
    # sys.excepthook = my_exeption_hook
    sys.exit(app.exec_())