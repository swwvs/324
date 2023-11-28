import tkinter as tk
import tkinter.messagebox
import tkinter
from tkinter import ttk
import sqlite3
from tkcalendar import Calendar
import tkinter.messagebox
class User():
    global getlogIDUser

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("User Window")
        self.window.geometry('1000x1200')
        print(getlogIDUser)
        self.buttonBack = tk.Button(self.window, text='Logout', command=self.logout)

        notebook = ttk.Notebook(self.window)
        notebook.pack()

        frame1 = tkinter.Frame(self.window, bg='grey')
        frame2 = tkinter.Frame(self.window, bg='grey')
        frame1.pack()
        frame2.pack()
        notebook.add(frame1, text='Reserve a Cart')
        notebook.add(frame2, text='View my Reservations')

        connection = sqlite3.connect("k7.db")

        resrvationTv = ttk.Treeview(frame2, columns=(1, 2, 3, 4, 5), show='headings')

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
            resrvationTv.insert(parent='', index=count, text='',
                                values=(row[0], row[1], row[2], row[3], row[4]))
            count += 1
        refreshButton = tkinter.Button(frame2, text="Refresh", width='20', command=self.refresh)
        refreshButton.pack()
        connection.close()
        connection = sqlite3.connect("k7.db")
        CartTv = ttk.Treeview(frame1, columns=(1, 2), show='headings')

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
        connection = sqlite3.connect("k7.db")
        cursor = connection.execute("SELECT CartID from Cart")
        CartIDRows = cursor.fetchall()
        allCartIdsList = [r[0] for r in CartIDRows]  # removing commas that appear at the end of the tuple ex:[323, ]

        connection.close()

        self.selected_Cart = tkinter.StringVar()
        self.combBox = ttk.Combobox(frame1, textvariable=self.selected_Cart)
        self.combBox['values'] = allCartIdsList
        self.comblabel = tkinter.Label(frame1, text='choose Cart Id:', bg='grey')
        self.comblabel.pack(side='top', ipadx=10, pady=5)
        self.combBox.pack(side='top', ipadx=10, pady=5)
        self.startcal = Calendar(frame1, date_pattern="Y-mm-DD")
        self.startcal.pack(expand='true', fill='x')

        self.startdate = tkinter.Button(frame1, text="enter start date", command=self.getStartDate)
        self.startlabel = tkinter.Label(frame1, text='date')
        self.startdate.pack()
        self.startlabel.pack(pady='20')
        self.label1 = tk.Label(frame1, text="Start time::24h 00:00")
        self.entry1 = tk.Entry(frame1, width="22")
        self.label1.pack()
        self.entry1.pack()

        self.endcal = Calendar(frame1, date_pattern="Y-mm-DD")
        self.endcal.pack(fill='x')

        self.enddate = tkinter.Button(frame1, text="enter end date", command=self.getEndDate)
        self.endlabel = tkinter.Label(frame1, text='date')
        self.enddate.pack(ipadx=10)
        self.endlabel.pack(pady='20')
        self.label2 = tk.Label(frame1, text="End time:24h 00:00")
        self.entry2 = tk.Entry(frame1, width="22")
        self.label2.pack()
        self.entry2.pack()
        self.reserveButton = tkinter.Button(frame1, text="reserve", width='15',pady='20', command=self.reserve)
        self.reserveButton.pack()


        self.buttonBack.pack()
        self.window.mainloop()

    def logout(self):
        self.window.destroy()
        self.window.destroy()
        import Signup
        Signup.Signup()

    def getStartDate(self):
        self.startlabel.config(text=f"the start date is {self.startcal.get_date()}")
        return self.startcal.get_date()

    def getEndDate(self):
        self.startcompare = self.startcal.get_date().split('-')  # to avoid choosing end date before start date
        self.endcompare = self.endcal.get_date().split('-')

        if ((self.startcompare[-3:-2] > self.endcompare[-3:-2]) or  # [-1:]  days , [-2:-1]  months , [-3:-2]  years
                (self.startcompare[-2:-1] > self.endcompare[-2:-1] and self.startcompare[-3:-2] >= self.endcompare[-3:-2]) or
                (self.startcompare[-1:] > self.endcompare[-1:] and self.startcompare[-2:-1] >= self.endcompare[-2:-1] and self.startcompare[
                                                                                                      -3:-2] >= self.endcompare[
                                                                                                                -3:-2])):
            tkinter.messagebox.showinfo('Error', "you cant choose End Date earlier than Start Date")
            return
        self.endlabel.config(text=f"the end date is {self.endcal.get_date()}")
        return self.endcal.get_date()

    def reserve(self):
        connection = sqlite3.connect("k7.db")
        reserved="true"
        connection.execute(
            f"INSERT INTO Reservations VALUES ({getlogIDUser}, {self.combBox.get()},'{self.startcal.get_date()}','{self.endcal.get_date()}','{reserved}')")
        connection.commit()

    def go_signup(self):
        self.window.destroy()
        import Signup
        Signup.Signup()

    def refresh(self):
        self.window.destroy()
        import User
        User.User()