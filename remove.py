from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

#creating window

root = Tk()
root.title('Remove')
root.configure(bg = '#234E70')
root.geometry('400x200')
#creating the main function of the entire program that executes commands
a = StringVar()

def ent():

    if len(a.get()) ==0:
        messagebox.showinfo("Error","Please Enter A Valid Id")
    else:
        d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
        if d:
            try:
                conn = mysql.connector.connect(host='localhost',
                                    database='budget',
                                    user='root',
                                    password='heelo.123')
                myCursor = conn.cursor()
                myCursor.execute("Delete from budget where ID = %s",[a.get()])
                conn.commit()
                myCursor.close()
                conn.close()
                messagebox.showinfo("Confirm","User Removed Successfully")
                a.set("")
            except:
                messagebox.showerror("Error","Something goes wrong")
Label(root,text = "Task Id: ",bg='#234E70',fg='#FBF8BE',font=('Courier new', 15, 'bold')).place(x = 5,y = 40)
Entry(root,textvariable = a,width = 37).place(x = 160,y = 44)
Button(root,text='Remove',bg = '#234E70', fg = '#FBF8BE', width=15, font=('arial', 10),command = ent).place(x=200, y = 90)

root.mainloop()