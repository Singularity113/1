import sqlite3

db_prod = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\NewProducts.db')
cur_p = db_prod.cursor()
cur_p.execute("""CREATE TABLE NewProducts(
    id_prod INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(80),
    id_c INTEGER NOT NULL,
    count INTEGER NOT NULL,
    cost INTEGER NOT NULL,
    FOREIGN KEY(id_C) REFERENCES Category(id_c)
)""")
db_prod.commit()

db_category = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Category.db')
cur_c = db_category.cursor()
cur_c.execute("""CREATE TABLE Category(
    id_c INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40)
)""")
db_category.commit()

db_order = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\Order.db')
cur_o = db_order.cursor()
cur_o.execute("""CREATE TABLE Orders(
    id_o INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(80),
    count INTEGER NOT NULL,
    cost INTEGER NOT NULL,
    date TEXT 
)""")
db_order.commit()

db_all = sqlite3.connect(r'C:\Users\Dungeon Master\Desktop\DB_PyQt5\AllOrders.db')
cur_all = db_all.cursor()
cur_all.execute("""CREATE TABLE AllOrders(
    id_o INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(80),
    count INTEGER NOT NULL,
    cost INTEGER NOT NULL,
    date TEXT 
)""")
db_all.commit()

cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('DEXP Atlas H341 [Intel Celeron N4020, 2x1.1 ГГц, 4 ГБ DDR4, SSD 240 ГБ, без ОС]',1,10,11000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('DEXP Aquilon O280 [Intel Celeron N4120, 4x1.1 ГГц, 8 ГБ DDR4, SSD 128 ГБ, Windows 10 Pro]',1,20,15000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('ZET Gaming NEO M064 [Intel Core i5-12400F, 6x2.5 ГГц, 16 ГБ DDR4, GeForce RTX 3050, SSD 512 ГБ, без ОС]',1,15,70000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('13.3" Irbis NB77 черный [HD (1366x768), TN+film, Intel Atom Z3735F, ядра: 4 х 1.33 ГГц, RAM 2 ГБ, eMMC 32 ГБ, Intel HD Graphics , Windows 10 Home Single Language]',2,30,15000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('11.6" Lenovo IdeaPad 1 11ADA05 серебристый [HD (1366x768), TN+film, AMD Athlon Silver 3050e, ядра: 2 х 1.4 ГГц, RAM 4 ГБ, SSD 128 ГБ, AMD Radeon Graphics , без ОС]',2,25,22000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('14" Acer Spin 1 SP114-31-C1SJ серебристый [Full HD (1920x1080), TN+film, Intel Celeron N4500, ядра: 2 х 1.1 ГГц, RAM 4 ГБ, SSD 256 ГБ, Intel UHD Graphics , Windows 10 Home Single Language]',2,13,36000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('HIPER KG201 Demure [мембранная, клавиш - 87, USB, черная]',3,50,800)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('Defender Assault GK-350L [мембранная, клавиш - 104, USB, серебристая]',3,35,1000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('Qumo Omicron K32 [мембранная, клавиш - 104, USB, белая]',3,20,1500)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('20.7" HP 21-b0034ur [463J4EA] [Intel Celeron J4025, 2x2 ГГц, TN + film, Full HD (1920x1080), 4 ГБ DDR4, SSD 128 ГБ, без ОС]',4,12,32000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('23.8" MSI PRO AP241 11M-642XRU [9S6-AE0312-642] [Intel Pentium Gold G6405, 2x4.1 ГГц, IPS, Full HD (1920x1080), 8 ГБ DDR4, SSD 256 ГБ, без ОС]',4,8,37000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('21.5" ASUS A5200WFAK-WA015M [90PT02K4-M04770] [Intel Core i3-10110U, 2x2.1 ГГц, IPS, Full HD (1920x1080), 8 ГБ DDR4, SSD 256 ГБ, без ОС]',4,5,45000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('Pantum P2207 [черно-белая печать, A4, 1200x1200 dpi, ч/б - 20 стр/мин (A4), USB]',5,34,8600)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('HP Laser 107a [черно-белая печать, A4, 1200x1200 dpi, ч/б - 20 стр/мин (A4), USB 2.0]',5,23,13000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('Hiper Cinema A6 черный [LCD, 800x480, 1800:1, 2500 лм, 1 кг]',6,24,7500)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('ViewSonic PA503X белый [DLP, 1024x768, 3D, 22000:1, 3600 лм, 27 дБ, 2.12 кг]',6,5,60000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('Mercusys MW306R [3x100 Мбит/с, 4 (802.11n), Wi-Fi 300 Мбит/с, IPv6]',7,23,1000)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('Mercusys AC10 [2x100 Мбит/с, 5 (802.11ac), 4 (802.11n), Wi-Fi 1167 Мбит/с, IPv6]',7,54,1300)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('FinePower Standard 518B-UPS черный [для ИБП, розетки - 5, 10 А, 2400 Вт, кабель - 1.8 м]',8,70,450)""")
cur_p.execute("""INSERT INTO NewProducts(name, id_c, count, cost) VALUES('Power Cube SPG-B-0.5M-BLACK черный [розетки - 5, 10 А, 2200 Вт, кабель - 0.5 м]',8,25,500)""")
db_prod.commit()


cur_c.execute("""INSERT INTO Category(name) VALUES('ПК')""")
cur_c.execute("""INSERT INTO Category(name) VALUES('Ноутбук')""")
cur_c.execute("""INSERT INTO Category(name) VALUES('Переферия')""")
cur_c.execute("""INSERT INTO Category(name) VALUES('Моноблок')""")
cur_c.execute("""INSERT INTO Category(name) VALUES('Принтер')""")
cur_c.execute("""INSERT INTO Category(name) VALUES('Проектор')""")
cur_c.execute("""INSERT INTO Category(name) VALUES('Wi-Fi роутер')""")
cur_c.execute("""INSERT INTO Category(name) VALUES('Сетевой фильтр')""")
db_category.commit()