import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import messagebox

root = tk.Tk()

root.geometry('710x235+400+100')
root.resizable(False, False)
root.title('Огнестрельное оружие')
#создание таблицы
i = 0
j = 0
n, m = 3, 12
a = [[ttk.Label(root, background='red', width=22, relief="solid", text='').grid(column=i, row=j) for j in range(m)] for i in range(n)]

lbl0 = ttk.Label(root, width=22, relief="solid", text='Mauser C96').grid(column=0, row=1)
lbl2 = ttk.Label(root, width=22, relief="solid", text='1916-1918').grid(column=1, row=1)
lbl3 = ttk.Label(root, width=22, relief="solid", text='1,25').grid(column=2, row=1)

lbl4 = ttk.Label(root, width=22, relief="solid", text='Thompson 1928A1').grid(column=0, row=2)
lbl5 = ttk.Label(root, width=22, relief="solid", text='1921').grid(column=1, row=2)
lbl6 = ttk.Label(root, width=22, relief="solid", text='4,9').grid(column=2, row=2)

lbl7 = ttk.Label(root, width=22, relief="solid", text='Colt M1911A1').grid(column=0, row=3)
lbl8 = ttk.Label(root, width=22, relief="solid", text='1911').grid(column=1, row=3)
lbl9 = ttk.Label(root, width=22, relief="solid", text='1,12').grid(column=2, row=3)

def create1():
    w1 = Toplevel(root)
    w1.geometry('450x100+400+390')
    w1.title('Добавление')
    #заполнение таблицы
    def save():

        while e1.get() == '':
            messagebox.showerror("Добавление", "Введите все значения")
        while e2.get() == '':
            messagebox.showerror("Добавление", "Введите все значения")
        while e3.get() == '':
            messagebox.showerror("Добавление", "Введите все значения")

        f = c1.get() 
        if e1.get() == '':
            lbl1 = ttk.Label(root, background='red', width=22, relief="solid", text=e1.get()).grid(column=0, row=f+1)
        else:
            lbl1 = ttk.Label(root, width=22, relief="solid", text=e1.get()).grid(column=0, row=f+1)
        if e2.get() == 0:
            lbl2 = ttk.Label(root, background='red', width=22, relief="solid", text=e2.get()).grid(column=1, row=f+1)
        else:
            lbl2 = ttk.Label(root, width=22, relief="solid", text=e2.get()).grid(column=1, row=f+1)
        if e3.get() == 0.0:
            lbl3 = ttk.Label(root, background='red', width=22, relief="solid", text=e3.get()).grid(column=2, row=f+1)
        else:
            lbl3 = ttk.Label(root, width=22, relief="solid", text=e3.get()).grid(column=2, row=f+1)

    lb = ttk.Label(w1, text='Выберите строку для добавления').grid(column=2, row=0)

    c1 = tk.IntVar(value=3)
    spin_box_1 = ttk.Spinbox(w1, state='readonly', from_=3, to=10,textvariable=c1, wrap=True, width='10').grid(column=2, row=1)

    lbl1 = ttk.Label(w1, text='Введите название').grid(column=0, row=0)

    e1 = tk.StringVar()
    en1 = ttk.Entry(w1, textvariable=e1).grid(column=1, row=0)

    lbl2 = ttk.Label(w1, text='Введите год выпуска').grid(column=0, row=1)

    e2 = tk.IntVar()
    en2 = ttk.Entry(w1, textvariable=e2).grid(column=1, row=1)

    lbl3 = ttk.Label(w1, text='Введите массу').grid(column=0, row=2)

    e3 = tk.DoubleVar()
    en3 = ttk.Entry(w1, textvariable=e3).grid(column=1, row=2)

    btn1 = ttk.Button(w1, text='Сохранить изменения', command=save).grid(column=0, row=3)

def create2():
    w1 = Toplevel(root)
    w1.geometry('300x100+500+390')
    w1.title('Удаление')
    #создание пустых ячеек
    def delete():
        f = c1.get()
        lbl1 = ttk.Label(root, background='red', width=22, relief="solid", text='').grid(column=0, row=f+1)
        lbl2 = ttk.Label(root, background='red', width=22, relief="solid", text='').grid(column=1, row=f+1)
        lbl3 = ttk.Label(root, background='red', width=22, relief="solid", text='').grid(column=2, row=f+1)
    
    l1 = ttk.Label(w1, text='Выберите строку для удаления').grid(column=0, row=0)

    c1 = tk.IntVar(value=0)
    spin_box_1 = ttk.Spinbox(w1, state='readonly', from_=0, to=10,textvariable=c1, wrap=True, width='10').grid(column=1, row=0)

    b1 = ttk.Button(w1, text='Удалить', command=delete).grid(column=0, row=1)

def create3():
    w1 = Toplevel(root)
    w1.geometry('450x100+400+390')
    w1.title('Изменение')
    #заполнение др содержимым
    def re():

        while e1.get() == '':
            messagebox.showerror("Изменение", "Введите все значения")
        while e2.get() == '':
            messagebox.showerror("Изменение", "Введите все значения")
        while e3.get() == '':
            messagebox.showerror("Изменение", "Введите все значения")

        f = c1.get() 
        if e1.get() == '':
            lbl1 = ttk.Label(root, background='red', width=22, relief="solid", text=e1.get()).grid(column=0, row=f+1)
        else:
            lbl1 = ttk.Label(root, width=22, relief="solid", text=e1.get()).grid(column=0, row=f+1)
        if e2.get() == 0:
            lbl2 = ttk.Label(root, background='red', width=22, relief="solid", text=e2.get()).grid(column=1, row=f+1)
        else:
            lbl2 = ttk.Label(root, width=22, relief="solid", text=e2.get()).grid(column=1, row=f+1)
        if e3.get() == 0.0:
            lbl3 = ttk.Label(root, background='red', width=22, relief="solid", text=e3.get()).grid(column=2, row=f+1)
        else:
            lbl3 = ttk.Label(root, width=22, relief="solid", text=e3.get()).grid(column=2, row=f+1)
    
    lb = ttk.Label(w1, text='Выберите строку для изменения').grid(column=2, row=0)

    c1 = tk.IntVar(value=0)
    spin_box_1 = ttk.Spinbox(w1, state='readonly', from_=0, to=10,textvariable=c1, wrap=True, width='10').grid(column=2, row=1)

    lbl1 = ttk.Label(w1, text='Введите название').grid(column=0, row=0)

    e1 = tk.StringVar()
    en1 = ttk.Entry(w1, textvariable=e1).grid(column=1, row=0)

    lbl2 = ttk.Label(w1, text='Введите год выпуска').grid(column=0, row=1)

    e2 = tk.IntVar()
    en2 = ttk.Entry(w1, textvariable=e2).grid(column=1, row=1)

    lbl3 = ttk.Label(w1, text='Введите массу').grid(column=0, row=2)

    e3 = tk.DoubleVar()
    en3 = ttk.Entry(w1, textvariable=e3).grid(column=1, row=2)

    btn1 = ttk.Button(w1, text='Сохранить изменения', command=re).grid(column=0, row=3)

l1 = ttk.Label(root, width=22, relief="solid", text='Наименование модели').grid(column=0, row=0)
l2 = ttk.Label(root, width=22, relief="solid", text='Год выпуска').grid(column=1, row=0)
l3 = ttk.Label(root, width=22, relief="solid", text='Масса(кг)').grid(column=2, row=0)

btn0 = ttk.Button(root, text='Добавить запись', command=create1).grid(column=3, row=0)
btn1 = ttk.Button(root, text='Удалить запись', command=create2).grid(column=4, row=0)
btn2 = ttk.Button(root, text='Изменить запись', command=create3).grid(column=5, row=0)     

root.mainloop()