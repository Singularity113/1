import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()

# create new windows
def create_1():
    newWindow_1 = tk.Toplevel(root)
    newWindow_1.geometry('712x400+400+200')
    newWindow_1.resizable(False, False)
    newWindow_1.title('Решение уравнений 1 степени')

    # exit button
    exit_button = ttk.Button(newWindow_1, text='Exit', command=lambda: newWindow_1.quit())
    exit_button.pack(ipadx=2, ipady=2, fill='x',side='bottom')
    
    # spinboxs
    current_value_1 = tk.IntVar(value=0)
    spin_box_1 = ttk.Spinbox(newWindow_1, state='readonly', from_=-20, to=20, 
    textvariable=current_value_1, wrap=True, width='10')

    current_value_2 = tk.IntVar(value=0)
    spin_box_2 = ttk.Spinbox(newWindow_1, state='readonly', from_=-20, to=20, 
    textvariable=current_value_2, wrap=True, width='10')

    # Button
    btn_s = ttk.Button(newWindow_1, text='Найти ответ')
    
    # labels
    lbl_1 = ttk.Label(newWindow_1, text=' *X + ', font=("Times New Roman", 14))
    lbl_2 = ttk.Label(newWindow_1, text=' = 0 ', font=("Times New Roman", 14))
    
    btn_s.place(relx=0.45, rely=0.5)
    lbl_1.place(relx=0.4, rely=0.1)
    lbl_2.place(relx=0.60, rely=0.1)   
    spin_box_1.place(relx=0.29, rely=0.1)
    spin_box_2.place(relx=0.48, rely=0.1)
 
def create_2():
    newWindow_2 = tk.Toplevel(root)
    newWindow_2.geometry('712x400+400+200')
    newWindow_2.resizable(False, False)
    newWindow_2.title('Решение уравнений 2 степени')

    # exit button
    exit_button = ttk.Button(newWindow_2, text='Exit', command=lambda: newWindow_2.quit())
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
    
    # labels
    lbl_1 = ttk.Label(newWindow_2, text=' *X^2 + ', font=("Times New Roman", 14))
    lbl_2 = ttk.Label(newWindow_2, text=' *X + ', font=("Times New Roman", 14))
    lbl_3 = ttk.Label(newWindow_2, text=' = 0 ', font=("Times New Roman", 14))

    btn_s = ttk.Button(newWindow_2, text='Найти ответ')

    btn_s.place(relx=0.45, rely=0.5)  
    lbl_1.place(relx=0.35, rely=0.1)
    lbl_2.place(relx=0.56, rely=0.1)   
    lbl_3.place(relx=0.76, rely=0.1)
    spin_box_1.place(relx=0.23, rely=0.1)
    spin_box_2.place(relx=0.45, rely=0.1)
    spin_box_3.place(relx=0.64, rely=0.1)

def create_3():
    newWindow_3 = tk.Toplevel(root)
    newWindow_3.geometry('712x400+400+200')
    newWindow_3.resizable(False, False)
    newWindow_3.title('Решение уравнений 3 степени')

    # exit button
    exit_button = ttk.Button(newWindow_3, text='Exit', command=lambda: newWindow_3.quit())
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

    btn_s = ttk.Button(newWindow_3, text='Найти ответ')

    btn_s.place(relx=0.45, rely=0.5)
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
    newWindow_4.geometry('712x400+400+200')
    newWindow_4.resizable(False, False)
    newWindow_4.title('Решение уравнений 4 степени')

    # exit button
    exit_button = ttk.Button(newWindow_4, text='Exit', command=lambda: newWindow_4.quit())
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

    btn_s = ttk.Button(newWindow_4, text='Найти ответ')

    btn_s.place(relx=0.45, rely=0.5)
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
   
root.geometry('712x400+400+200')
root.resizable(False, False)
root.title('Решение уравнений') 

# exit button
exit_button = ttk.Button(root, text='Exit', command=lambda: root.quit())
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