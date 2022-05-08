from tkinter import * 
from tkinter import ttk   
from tkinter.ttk import Combobox 
from random import randint

i = 0
p = 1
N = 20
z = 0
array = [0]*N
for i in range(N):
    array[i] = randint(-9,9)
for i in range(N):
    if array[i] != 0:
        p = p*array[i] 
for i in range(N):
    if array[i] == 0:
        z += 1

M = [0]*N
P = [0]*N
for i in range(N):
    M[i] = randint(-9,9)
for i in range(N):
    if i % 2 == 0:
        P[i] = i*M[i]
    else:
        P[i] = 5*M[i]

window = Tk()  
window.title("Массивы")  
window.geometry('350x200+600+250')
window.resizable(False, False)

combo = Combobox(window)  
combo = ttk.Combobox(window, values=[array], state="readonly")

combo.grid(column=0, row=0)
combo.current(0) 

lbl1 = ttk.Label(window, text='Произведение ненулевых элементов:').grid(column=0, row=1)
lbl2 = ttk.Label(window, text='Количество нулевых элементов').grid(column=0, row=3)
lbl3 = ttk.Label(window, text=p).grid(column=1, row=1)
lbl4 = ttk.Label(window, text=z).grid(column=1, row=3)
lbl5 = ttk.Label(window, text='Задание 2').grid(column=0, row=5)

combo1 = Combobox(window)  
combo1 = ttk.Combobox(window, values=[M], state="readonly")
combo1.grid(column=0, row=7)
combo1.current(0)
lbl11 = ttk.Label(window, text='1 Массив').grid(column=0, row=6)
lbl12 = ttk.Label(window, text='2 Массив').grid(column=0, row=8)
combo2 = Combobox(window)  
combo2 = ttk.Combobox(window, values=[P], state="readonly")
combo2.grid(column=0, row=9)
combo2.current(0)
lbl13 = ttk.Label(window, text='Индексация начинается с нуля!').grid(column=0, row=10)
   
window.mainloop()