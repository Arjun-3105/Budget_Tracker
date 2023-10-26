from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt
import os, sys


#creating window

root = Tk()
root.title('Remove detaisl')
root.configure(bg = '#234E70')
root.geometry('900x300')
#creating the main function of the entire program that executes commands
a = StringVar()
b= StringVar()
def ge():
    if (len(b.get())) == 0:
        messagebox.showinfo('Error', 'First select a item')
    if b.get() == 'MONTH':
        root.destroy()
        py = sys.executable
        os.system('%s %s' % (py,'bar.py'))
    #     try:
    #         conn = mysql.connector.connect(host='localhost',
    #                                 database='budget',
    #                                 user='root',
    #                                 password='heelo.123')
    #         mycursor =conn.cursor()
    #         mycursor.execute("Select month, sum(amount) as total from budget where month LIKE %s group by month",['%'+a.get()+'%'])
    #         pc = mycursor.fetchall()
    #         if pc:
    #             fig = plt.figure()
    #             axes = fig.add_subplot(1,1,1)
    #             axes.bar(range(len(pc)),
    #                      [pc[1] for x in pc],
    #                      tick_label = [pc[0] for x in pc] 

    #             )
    #             plt.show()
    #             # insert(pc)
    #         else:
    #             messagebox.showinfo("Oop's","Either Name is incorrect or it is not available")
    #     except Error:
    #         messagebox.showerror("Error","Something goes wrong")
    elif b.get().lower() =='type':

        root.destroy()
        py = sys.executable
        os.system('%s %s' % (py,'bar-type.py'))
        # try:
        #     conn = mysql.connector.connect(host='localhost',
        #                             database='budget',
        #                             user='root',
        #                             password='heelo.123')
        #     mycursor =conn.cursor()
        #     mycursor.execute("Select type, sum(amount) as total from budget group by typ")
        #     pc = mycursor.fetchall()
        #     if pc:
        #         fig = plt.figure()
        #         axes = fig.add_subplot(1,1,1)
        #         axes.bar(range(len(pc)),
        #                  [pc[1] for x in pc],
        #                  tick_label = [pc[0] for x in pc] 

        #         )
        #         plt.show()
        #         # insert(pc)
        #     else:
        #         messagebox.showinfo("Oop's","Either Name is incorrect or it is not available")
        # except Error:
        #     messagebox.showerror("Error","Something goes wrong")
            
find = Button(root,text="Find",width=15,bg='#234E70', fg = '#FBF8BE',font=("Courier new",10,'bold'),command = ge).place(x=300,y=148)
# en = Entry(root,textvariable=a,width=43).place(x=180,y=155)
Label(root,text = "Select to graph", bg = '#234e70', fg = '#fbf883',font=("Courier new",10,'bold')).place(x = 130,y = 100)
#creating a drop down menu box
c=ttk.Combobox(textvariable=b,values=["TYPE","MONTH"],width=40,state="readonly").place(x = 290, y = 100)
Button(root, text = 'Submit', bg = '#234e70', fg= '#fbf88e', command = ge)
root.mainloop()
plt.show()