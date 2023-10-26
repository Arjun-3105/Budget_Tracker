from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt

#creating window

try:
    conn = mysql.connector.connect(host='localhost',
                            database='budget',
                            user='root',
                            password='heelo.123')
    mycursor =conn.cursor()
    mycursor.execute("Select month, sum(amount) as total from budget group by month")
    pc = mycursor.fetchall()
    a = [a[0] for a in pc]
    print(a)

    if pc:
        fig = plt.figure()
        axes = fig.add_subplot(1,1,1)
        axes.bar(range(len(pc)),
                    [x[1] for x in pc],
                    tick_label = [x[0] for x in pc] 

        )
        plt.show()
    else:
        messagebox.showinfo("Oop's","Either Name is incorrect or it is not available")
except Error:
     messagebox.showerror("Error","Something goes wrong")