from tkinter import *
import os, sys
import mysql.connector

global py
py = sys.executable


#connecting to the database:
try: 
    conn = mysql.connector.connect(host='localhost',
                                            database='budget',
                                            user='root',
                                            password='heelo.123')
except:
    print('error')

# creating the window
root = Tk()
root.title('BUDGET TRACKER')
root.config(bg = '#234E70')
root.geometry('1080x720')
#creating and linking the database


label = Label(root, text = 'BUDGET TRACKER', font  = ('Arial', 50), bg = '#234E70', fg = '#FBF8BE')
label.pack()

def add():
    # root.destroy()
    global py
    os.system('%s %s' % (py, 'add.py'))
    
    

def remove():
    
    # global py
    root.destroy()
    os.system('%s %s' % (py, 'remove.py'))
    

    

def display():
    # root.destroy()
    global py
    os.system('%s %s' % (py, 'show.py'))

def analysis():
    global py
    os.system('%s %s' % (py,'analysis.py'))
    
    

#creating buttons
button_frame = Frame(root, bg = '#234E70')
button_frame.pack()

button_add = Button(button_frame, text = 'Add Expense', bg = '#234E70', fg = '#FBF8BE', font = ('arial', 20), command = add)
button_display = Button(button_frame, text = 'Display', bg = '#234E70', fg = '#FBF8BE', font = ('arial', 20), command = display)
button_mark = Button(root, text='Analysis', bg = '#234E70',fg= '#FBF8BE',font = ('arial', 20), command = analysis)
button_remove = Button(button_frame, text = 'Remove expense', bg = '#234E70', fg = '#FBF8BE', font = ('arial', 20), command = remove)
button_quit = Button(button_frame, text = 'QUIT', bg = '#234E70', fg = '#FBF8BE', font = ('arial', 20), command = root.quit)


button_add.pack(pady =20)
button_display.pack(pady =20 )
button_mark.pack(pady=20)
button_remove.pack(pady=20)
button_quit.pack(pady=20)



root.mainloop()