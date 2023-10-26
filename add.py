import mysql.connector
from tkinter import *
from tkinter import messagebox
from mysql.connector import Error
import os, sys
from tkinter import ttk
global py
py = sys.executable

#inintiating  the tkinter screen
root = Tk()
root.title('BUDGET TRACKER')
root.config(bg = '#234E70')
root.geometry('500x600')

a =StringVar()
b =StringVar()
c =StringVar()
d=StringVar()
e = IntVar()

def b_q():
            if len(b.get()) == 0 or len(c.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                g = 'ongoing'
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='budget',
                                         user='root',
                                         password='heelo.123')
                    myCursor = conn.cursor()
                    myCursor.execute("Insert into budget(ID,name,amount,type,month) values (%s,%s,%s,%s,%s)",[a.get(),b.get(),e.get(),d.get(),c.get()])
                    conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another expense?")
                    if ask:
                        root.destroy()
                        os.system('%s %s' % (py, 'add-copy.py'))
                    else:
                        root.destroy()
                except Error:
                    
                    messagebox.showerror("Error","Check The Details")

#creating labels and input field

Label( text='BUDGET DETAILS:',bg='#234E70',fg='#FBF8BE',font=('Courier new', 20, 'bold')).place(x=150, y=70)
Label( text='').pack()
Label( text='ID(unique)',bg='#234E70',fg='#FBF8BE', font=('Courier new', 10, 'bold')).place(x=60, y=180)
Entry( textvariable=a, width=30).place(x=170, y=180)
Label(text='NAME:',bg='#234E70',fg='#FBF8BE', font=('Courier new', 10, 'bold')).place(x=60, y=230)
Entry( textvariable=b, width=30).place(x=170, y=232)
Label(text='MONTH:',bg='#234E70',fg='#FBF8BE', font=('Courier new', 10, 'bold')).place(x=60, y=280)
Entry(textvariable=c, width=30).place(x=170, y=300)
l=ttk.Combobox(textvariable=d,values=["Food","Housing","Travel", "Debt and loan",'entertainment', 'Misscellaneous'],width=40,state="readonly").place(x = 170, y = 320)

Label(text='AMOUNT: ',bg='#234E70',fg='#FBF8BE', font=('Courier new', 10, 'bold')).place(x=60, y=380)
Entry(textvariable=e, width=30).place(x=170, y=380)
Button(text="Submit",command = b_q).place(x=245, y=420)




root.mainloop()

