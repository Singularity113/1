import tkinter as Tkinter
import winsound

counter = -1

running = False

def counter_label(label):

    def count():

        if running:

            global counter

            if counter==-1:           

                display="Starting..."

            else:

                display=str(counter)

            label['text']=display   

            label.after(1000, count)

            counter += 1

    count()     

def Start(label):

    winsound.PlaySound("SystemExit", winsound.SND_LOOP)

    global running

    running=True

    counter_label(label)

    start['state']='disabled'

    stop['state']='normal'

    reset['state']='normal'

def Stop():

    winsound.PlaySound("SystemQuestion", winsound.SND_LOOP)

    global running

    start['state']='normal'

    stop['state']='disabled'

    reset['state']='normal'

    running = False

def Reset(label):

    global counter

    counter=-1

    if running==False:     

        reset['state']='disabled'

        label['text']='Welcome!'

    else:               

        label['text']='Starting...'

root = Tkinter.Tk()

root.title("Stopwatch")

# Исправление размера окна.

root.minsize(width=300, height=150)
root.resizable(False,False)

label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")

label.pack()

start = Tkinter.Button(root, text='Start',
width=30, command=lambda:Start(label))

stop = Tkinter.Button(root, text='Stop',
width=30, state='disabled', command=Stop)

reset = Tkinter.Button(root, text='Reset',
width=30, state='disabled', command=lambda:Reset(label))

start.pack()
stop.pack()
reset.pack()
root.mainloop()