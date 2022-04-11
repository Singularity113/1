from math import sqrt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# root window
root = tk.Tk()

# create new windows
def create_1():
    newWindow_1 = tk.Toplevel(root)
    newWindow_1.geometry('712x200+450+300')
    newWindow_1.resizable(False, False)
    newWindow_1.title('Решение уравнений 1 степени')

    def solver1():
        a = current_value_1.get()
        b = current_value_2.get()
        if a == 0:
            messagebox.showerror("Решение уравнений 1 степени", "Коэффициент при x не может быть равен 0.")
        x = -b / a
        if x == 0:
            x = abs(x)
        text = "X: %s" % round(x,2)
        messagebox.showinfo("Решение уравнений 1 степени", text)
        
    # exit button
    exit_button = ttk.Button(newWindow_1, text='Выход', command=lambda: newWindow_1.quit())
    exit_button.pack(ipadx=2, ipady=2, fill='x',side='bottom')
    
    # spinboxs
    current_value_1 = tk.IntVar(value=0)
    spin_box_1 = ttk.Spinbox(newWindow_1, state='readonly', from_=-20, to=20,
    textvariable=current_value_1, wrap=True, width='10')

    current_value_2 = tk.IntVar(value=0)
    spin_box_2 = ttk.Spinbox(newWindow_1, state='readonly', from_=-20, to=20, 
    textvariable=current_value_2, wrap=True, width='10')

    # Button
    btn_s = ttk.Button(newWindow_1, text='Найти ответ', command=solver1)
    
    # labels
    lbl_1 = ttk.Label(newWindow_1, text=' *X + ', font=("Times New Roman", 14))
    lbl_2 = ttk.Label(newWindow_1, text=' = 0 ', font=("Times New Roman", 14))
    
    btn_s.place(relx=0.45, rely=0.65)
    lbl_1.place(relx=0.4, rely=0.1)
    lbl_2.place(relx=0.60, rely=0.1)   
    spin_box_1.place(relx=0.29, rely=0.1)
    spin_box_2.place(relx=0.48, rely=0.1)
 
def create_2():
    newWindow_2 = tk.Toplevel(root)
    newWindow_2.geometry('712x200+450+300')
    newWindow_2.resizable(False, False)
    newWindow_2.title('Решение уравнений 2 степени')

    def solver2():
        a = current_value_1.get()
        b = current_value_2.get()
        c = current_value_3.get()
        if a == 0:
            messagebox.showerror("Решение уравнений 2 степени", "Коэффициент при x в степени 2 не может быть равен 0.")
        D = b ** 2 - 4 * a * c
        if D > 0:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            text="X1: %s \n X2: %s \n" % (round(x1,2), round(x2,2))
            messagebox.showinfo("Решение уравнений 2 степени", text)
        elif D == 0:
            x = -b / (2 * a)
            text="X: %s \n" % round(x)
            messagebox.showinfo("Решение уравнений 2 степени", text)
        else:
            z1 = complex(round(-b + sqrt(abs(b ** 2 - 4 * a * c)) / (2 * a)))
            z2 = complex(round(-b - sqrt(abs(b ** 2 - 4 * a * c)) / (2 * a)))
            text="\n Z1: %s \n Z2: %s \n" % (z1, z2)
            messagebox.showinfo("Решение уравнений 2 степени", "У этого уравнения два комплексных корня:" + text)

    # exit button
    exit_button = ttk.Button(newWindow_2, text='Выход', command=lambda: newWindow_2.quit())
    exit_button.pack(ipadx=2, ipady=2, fill='x',side='bottom')

    # spinboxs
    current_value_1 = tk.IntVar(value=0)
    spin_box_1 = ttk.Spinbox(newWindow_2, state='readonly', from_=-20, to=20, 
    textvariable=current_value_1, wrap=True, width='10')

    current_value_2 = tk.IntVar(value=0)
    spin_box_2 = ttk.Spinbox(newWindow_2, state='readonly', from_=-20, to=20, 
    textvariable=current_value_2, wrap=True, width='10')

    current_value_3 = tk.IntVar(value=0)
    spin_box_3 = ttk.Spinbox(newWindow_2, state='readonly', from_=-20, to=20, 
    textvariable=current_value_3, wrap=True, width='10')

    btn_s = ttk.Button(newWindow_2, text='Найти ответ', command=solver2)
    
    # labels
    lbl_1 = ttk.Label(newWindow_2, text=' *X^2 + ', font=("Times New Roman", 14))
    lbl_2 = ttk.Label(newWindow_2, text=' *X + ', font=("Times New Roman", 14))
    lbl_3 = ttk.Label(newWindow_2, text=' = 0 ', font=("Times New Roman", 14))

    btn_s.place(relx=0.45, rely=0.65)  
    lbl_1.place(relx=0.35, rely=0.1)
    lbl_2.place(relx=0.56, rely=0.1)   
    lbl_3.place(relx=0.76, rely=0.1)
    spin_box_1.place(relx=0.23, rely=0.1)
    spin_box_2.place(relx=0.45, rely=0.1)
    spin_box_3.place(relx=0.64, rely=0.1)

def create_3():
    newWindow_3 = tk.Toplevel(root)
    newWindow_3.geometry('712x200+450+300')
    newWindow_3.resizable(False, False)
    newWindow_3.title('Решение уравнений 3 степени')

    def solver3():
        a = current_value_1.get()
        b = current_value_2.get()
        c = current_value_3.get()
        d = current_value_4.get()
        if a == 0:
            messagebox.showerror("Решение уравнений 3 степени", "Коэффициент при x в степени 3 не может быть равен 0.")
        p = (3*a*c - b*b)/(3*a*a)
        q = (2*b*b*b - 9*a*b*c + 27*a*a*d)/(27*a*a*a)
        Q = (p/3)**3 + (q/2)**2
        alf = ((-q/2) + (Q)**(1/2))**(1/3)
        bet = ((-q/2) - (Q)**(1/2))**(1/3)
        y1 = alf + bet
        y2 = -(alf + bet)/2 + ((alf - bet)/2)*((3)**(1/3))
        y3 = -(alf + bet)/2 - ((alf - bet)/2)*((3)**(1/3))
        x1 = (y1 - (b/3*a))
        x2 = (y2 - (b/3*a))
        x3 = (y3 - (b/3*a))
        text="\n X1: %s \n X2: %s \n X3: %s \n" % (x1, x2, x3)
        messagebox.showinfo("Решение уравнений 3 степени", text)

    # exit button
    exit_button = ttk.Button(newWindow_3, text='Выход', command=lambda: newWindow_3.quit())
    exit_button.pack(ipadx=2, ipady=2, fill='x',side='bottom')

    # spinboxs
    current_value_1 = tk.IntVar(value=0)
    spin_box_1 = ttk.Spinbox(newWindow_3, state='readonly', from_=-20, to=20, 
    textvariable=current_value_1, wrap=True, width='10')

    current_value_2 = tk.IntVar(value=0)
    spin_box_2 = ttk.Spinbox(newWindow_3, state='readonly', from_=-20, to=20, 
    textvariable=current_value_2, wrap=True, width='10')

    current_value_3 = tk.IntVar(value=0)
    spin_box_3 = ttk.Spinbox(newWindow_3, state='readonly', from_=-20, to=20, 
    textvariable=current_value_3, wrap=True, width='10')

    current_value_4 = tk.IntVar(value=0)
    spin_box_4 = ttk.Spinbox(newWindow_3, state='readonly', from_=-20, to=20, 
    textvariable=current_value_4, wrap=True, width='10')
    
    # labels
    lbl_1 = ttk.Label(newWindow_3, text=' *X^3 + ', font=("Times New Roman", 14))
    lbl_2 = ttk.Label(newWindow_3, text=' *X^2 + ', font=("Times New Roman", 14))
    lbl_3 = ttk.Label(newWindow_3, text=' *X + ', font=("Times New Roman", 14))
    lbl_4 = ttk.Label(newWindow_3, text=' = 0 ', font=("Times New Roman", 14))

    btn_s = ttk.Button(newWindow_3, text='Найти ответ', command=solver3)

    btn_s.place(relx=0.45, rely=0.65)
    lbl_1.place(relx=0.22, rely=0.1)
    lbl_2.place(relx=0.43, rely=0.1)   
    lbl_3.place(relx=0.64, rely=0.1)   
    lbl_4.place(relx=0.84, rely=0.1)     
    spin_box_1.place(relx=0.1, rely=0.1)
    spin_box_2.place(relx=0.317, rely=0.1)
    spin_box_3.place(relx=0.53, rely=0.1)
    spin_box_4.place(relx=0.72, rely=0.1)

def create_4():
    newWindow_4 = tk.Toplevel(root)
    newWindow_4.geometry('712x200+450+300')
    newWindow_4.resizable(False, False)
    newWindow_4.title('Решение уравнений 4 степени')

    def solver4():
        a = current_value_1.get()
        b = current_value_2.get()
        c = current_value_3.get()
        d = current_value_4.get()
        e = current_value_5.get()
        if a == 0:
            messagebox.showerror("Решение уравнений 4 степени", "Коэффициент при x в степени 4 не может быть равен 0.")
        alf = -(3*b*b/8*a*a) + c/a
        bet = (b**3/8*a**3) - (b*c/2*a**2) + d/a
        gam = -(3*b**4/256*a**4) + (b**2*c/16*a**3) - (b*d/4*a**2) + (e/a)
        if bet == 0:
            x1 = -(b/4*a) + ((-alf + (alf**2-4*gam)**(1/2))/2)**(1/2)
            x2 = -(b/4*a) + ((-alf - (alf**2-4*gam)**(1/2))/2)**(1/2)
            x3 = -(b/4*a) - ((-alf + (alf**2-4*gam)**(1/2))/2)**(1/2)
            x4 = -(b/4*a) - ((-alf - (alf**2-4*gam)**(1/2))/2)**(1/2)
            text="\n X1: %s \n X2: %s \n X3: %s \n X4: %s \n" % (x1, x2, x3, x4)
            messagebox.showinfo("Решение уравнений 4 степени", text)
        else:
            P = -alf**2/12 - gam
            Q = -alf**3/108 + alf*gam/3 - bet**2/8
            R = -Q/2 +- (Q**2/4 + P**3/27)**(1/2)
            U = R**(1/3)
            if U == 0:
                y = -(5/6)*alf + U - Q**(1/3)
            else:
                y = -(5/6)*alf + U + -P/3*U
            W = (alf + 2*y)**(1/2)
            x1 = -b/4*a + ( W + (-(3*alf + 2*y + 2*bet/W))**(1/2))/2
            x2 = -b/4*a + ( W - (-(3*alf + 2*y + 2*bet/W))**(1/2))/2
            x3 = -b/4*a + ( -W + (-(3*alf + 2*y - 2*bet/W))**(1/2))/2
            x4 = -b/4*a + ( -W - (-(3*alf + 2*y - 2*bet/W))**(1/2))/2
            text="\n X1: %s \n X2: %s \n X3: %s \n X4: %s \n" % (x1, x2, x3, x4)
            messagebox.showinfo("Решение уравнений 4 степени", text)

    # exit button
    exit_button = ttk.Button(newWindow_4, text='Выход', command=lambda: newWindow_4.quit())
    exit_button.pack(ipadx=2, ipady=2, fill='x',side='bottom')

    # spinboxs
    current_value_1 = tk.IntVar(value=0)
    spin_box_1 = ttk.Spinbox(newWindow_4, state='readonly', from_=-20, to=20, 
    textvariable=current_value_1, wrap=True, width='7')

    current_value_2 = tk.IntVar(value=0)
    spin_box_2 = ttk.Spinbox(newWindow_4, state='readonly', from_=-20, to=20, 
    textvariable=current_value_2, wrap=True, width='7')

    current_value_3 = tk.IntVar(value=0)
    spin_box_3 = ttk.Spinbox(newWindow_4, state='readonly', from_=-20, to=20, 
    textvariable=current_value_3, wrap=True, width='7')

    current_value_4 = tk.IntVar(value=0)
    spin_box_4 = ttk.Spinbox(newWindow_4, state='readonly', from_=-20, to=20, 
    textvariable=current_value_4, wrap=True, width='7')

    current_value_5 = tk.IntVar(value=0)
    spin_box_5 = ttk.Spinbox(newWindow_4, state='readonly', from_=-20, to=20, 
    textvariable=current_value_5, wrap=True, width='7')   
    
    # labels
    lbl_1 = ttk.Label(newWindow_4, text=' *X^4 + ', font=("Times New Roman", 14))
    lbl_2 = ttk.Label(newWindow_4, text=' *X^3 + ', font=("Times New Roman", 14))
    lbl_3 = ttk.Label(newWindow_4, text=' *X^2 + ', font=("Times New Roman", 14))
    lbl_4 = ttk.Label(newWindow_4, text=' *X + ', font=("Times New Roman", 14))
    lbl_5 = ttk.Label(newWindow_4, text=' = 0 ', font=("Times New Roman", 14))

    btn_s = ttk.Button(newWindow_4, text='Найти ответ', command=solver4)

    btn_s.place(relx=0.45, rely=0.65)
    lbl_1.place(relx=0.16, rely=0.1)
    lbl_2.place(relx=0.35, rely=0.1)   
    lbl_3.place(relx=0.54, rely=0.1)   
    lbl_4.place(relx=0.73, rely=0.1)
    lbl_5.place(relx=0.9, rely=0.1)   
    spin_box_1.place(relx=0.07, rely=0.1)
    spin_box_2.place(relx=0.26, rely=0.1)
    spin_box_3.place(relx=0.45, rely=0.1)
    spin_box_4.place(relx=0.64, rely=0.1)
    spin_box_5.place(relx=0.81, rely=0.1)      
   
root.geometry('712x200+450+300')
root.resizable(False, False)
root.title('Решение уравнений') 

# exit button
exit_button = ttk.Button(root, text='Выход', command=lambda: root.quit())
exit_button.pack(ipadx=2, ipady=2, fill='x',side='bottom')

# buttons
btn_1 = ttk.Button(root, text='Решение уравнений 1 степени', command=create_1)
btn_1.place(relx=0, rely=0)

btn_2 = ttk.Button(root, text='Решение уравнений 2 степени', command=create_2)
btn_2.place(relx=0.25, rely=0)

btn_3 = ttk.Button(root, text='Решение уравнений 3 степени', command=create_3)
btn_3.place(relx=0.5, rely=0)

btn_4 = ttk.Button(root, text='Решение уравнений 4 степени', command=create_4)
btn_4.place(relx=0.75, rely=0)

root.mainloop()