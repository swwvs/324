
import tkinter
from tkinter import ttk
import traceback
import sqlite3
connection = sqlite3.connect("k7.db")
connection.execute('''CREATE TABLE IF NOT EXISTS KSU(
            FName TEXT NOT NULL,
            LName TEXT NOT NULL,
            ID INT PRIMARY KEY NOT NULL,
            Password VARCHAR NOT NULL,
            Email VARCHAR NOT NULL,
            Phone INT NOT NULL,
            PType TEXT NOT NULL);''')
connection.execute('''CREATE TABLE IF NOT EXISTS Cart(
            CartID INT PRIMARY KEY NOT NULL,
            CartCollege TEXT NOT NULL);''')
connection.execute('''CREATE TABLE IF NOT EXISTS Reservations(
                ID INT NOT NULL,
                CartID INT NOT NULL,
                Start_Date DATE NOT NULL,
                End_Date DATE NOT NULL,
                reserved VARCHAR NULL,
                FOREIGN KEY(ID) REFERENCES KSU(ID),
                FOREIGN KEY(CartID) REFERENCES Cart(CartID));''')
connection.commit()
connection.close()

if __name__ == '__main__':    # if imported from another file it will not execute

    print("i am runnning DB ")
    connection = sqlite3.connect("k7.db")

    dbView = tkinter.Tk()
    notebook = ttk.Notebook(dbView)
    notebook.pack()

    frame1 = tkinter.Frame(dbView, bg='grey')

    frame1.pack()

    notebook.add(frame1, text='KSU')


    ksuTv = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6,7), show='headings')

    ksuTv.heading(1, text="FName")
    ksuTv.heading(2, text="LName")
    ksuTv.heading(3, text="ID INT")
    ksuTv.heading(4, text="Password")
    ksuTv.heading(5, text="Email")
    ksuTv.heading(6, text="Phone")
    ksuTv.heading(7, text="PType")

    ksuTv.column(1, anchor='center')
    ksuTv.column(2, anchor='center')
    ksuTv.column(3, anchor='center')
    ksuTv.column(4, anchor='center')
    ksuTv.column(5, anchor='center')
    ksuTv.column(6, anchor='center')
    ksuTv.column(7, anchor='center')


    cursor = connection.execute("SELECT * from KSU")
    count = 0

    ksuTv.pack(anchor='n')

    for row in cursor:
        ksuTv.insert(parent='', index=count, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        count += 1
    connection.close()

    connection = sqlite3.connect("k7.db")
    frame2 = tkinter.Frame(dbView, bg='grey')
    frame2.pack()
    notebook.add(frame2, text='Carts')
    CartTv = ttk.Treeview(frame2, columns=(1, 2), show='headings')

    CartTv.heading(1, text="CartID")
    CartTv.heading(2, text="CartCollege")

    CartTv.column(1, anchor='center')
    CartTv.column(2, anchor='center')

    cursor = connection.execute("SELECT * from Cart")
    count = 0

    CartTv.pack(anchor='n')

    for row in cursor:
        CartTv.insert(parent='', index=count, text='', values=(row[0], row[1]))
        count += 1
    connection.close()
    connection.close()
    frame3 = tkinter.Frame(dbView, bg='grey')
    frame3.pack()
    notebook.add(frame3, text='Reservations')
    connection = sqlite3.connect("k7.db")

    resrvationTv = ttk.Treeview(frame3, columns=(1, 2, 3, 4, 5), show='headings')

    resrvationTv.heading(1, text="ID")
    resrvationTv.heading(2, text="CartID")
    resrvationTv.heading(3, text="Start_Date")
    resrvationTv.heading(4, text="End_Date")
    resrvationTv.heading(5, text="reserved")

    resrvationTv.column(1, anchor='center')
    resrvationTv.column(2, anchor='center')
    resrvationTv.column(3, anchor='center')
    resrvationTv.column(4, anchor='center')
    resrvationTv.column(5, anchor='center')

    cursor = connection.execute("SELECT * from Reservations")
    count = 0

    resrvationTv.pack(anchor='n')

    for row in cursor:
        resrvationTv.insert(parent='', index=count, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        count += 1

    connection.close()
    dbView.mainloop()
