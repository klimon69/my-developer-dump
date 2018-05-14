from tkinter import *
import tkinter.messagebox

root = Tk()

#==================ФУНКЦИИ==================

def calcUhod(event):
    a = int(enyry_1.get())
    b = int(enyry_2.get())
    c = a-b
    if c > 0:
        d = (c/b)*100
        if d > 0 and d <= 2:
            label_5.config(text=d)
            label_3.config(image=photo2)
        elif d > 2 and d <= 3:
            label_5.config(text=d)
            label_3.config(image=photo)
        elif d > 3:
            label_5.config(text=d)
            label_3.config(image=photo3)


    elif c < 0:
        d = abs((c / a)*100)
        if d > 0 and d <= 2:
            label_5.config(text=d)
            label_3.config(image=photo2)
        elif d > 2 and d <= 3:
            label_5.config(text=d)
            label_3.config(image=photo)
        elif d > 3:
            label_5.config(text=d)
            label_3.config(image=photo3)






label_1 = Label(root, text='Значение при 25°C')
label_2 = Label(root, text='Значение при 125°C')
enyry_1 = Entry(root)
enyry_2 = Entry(root)
label_1.grid(row=0, padx=10, sticky=E)
label_2.grid(row=1,padx=10, sticky=E)
enyry_1.grid(row=0, column=1, padx=10)
enyry_2.grid(row=1, column=1, padx=10)


#=====================================================================


button_1 = Button(root, text="Посчитать уход")
button_1.grid(columnspan=4, rowspan=2, pady=20)
button_1.bind("<Button-1>", calcUhod)

#======================================================================

photo = PhotoImage(file="images/norm.png")
photo2 = PhotoImage(file="images/good7.png")
photo3 = PhotoImage(file="images/sad2.png")
label_3 = Label(root,image=photo)
label_3.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=W+E+N+S, padx=10, pady=10)

#======================================================================

label_4 = Label(root, text='    Уход (%):')
label_4.grid(row=4, column=1, sticky=E,pady=10)

#======================================================================

label_5 = Label(root, text='    ')
label_5.grid(row=4, column = 2, sticky=W)


#======================================================================



root.mainloop()