import tkinter as tk
import tkinter.messagebox
import tkinter
from tkinter import ttk
import sqlite3
from tkcalendar import Calendar
import tkinter.messagebox
import logging
logging.basicConfig(filename="Transactions.log", filemode="a",format='%(levelname)s - %(asctime)s - %(name)s  - %(message)s', level=logging.DEBUG)
class User():
    global getlogIDUser
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("User Window")
        self.window.geometry('1080x1080')
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

        resrvationTv = ttk.Treeview(frame2,columns=(1, 2, 3, 4, 5,6,7,8), show='headings', height=20)

        resrvationTv.heading(1, text="ID")
        resrvationTv.heading(2, text="CartID")
        resrvationTv.heading(3, text="CartCollege")
        resrvationTv.heading(4, text="Start_Date")
        resrvationTv.heading(5, text="End_Date")
        resrvationTv.heading(6, text="reserved")
        resrvationTv.heading(7, text="Start_Time")
        resrvationTv.heading(8, text="End_Time")

        resrvationTv.column(1, anchor='center')
        resrvationTv.column(2, anchor='center')
        resrvationTv.column(3, anchor='center')
        resrvationTv.column(4, anchor='center')
        resrvationTv.column(5, anchor='center')
        resrvationTv.column(6, anchor='center')
        resrvationTv.column(7, anchor='center')
        resrvationTv.column(8, anchor='center')

        cursor = connection.execute("SELECT * from Reservations")
        count = 0

        resrvationTv.pack(anchor='n')

        for row in cursor:
            resrvationTv.insert(parent='', index=count, text='',
                                values=(row[0], row[1], row[2], row[3], row[4],row[5], row[6], row[7]))
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
        self.cartid=self.selected_Cart
        self.startcal = Calendar(frame1, date_pattern="Y-mm-DD")
        self.startcal.pack(expand='true', fill='x')

        self.startdate = tkinter.Button(frame1, text="enter start date", command=self.getStartDate)
        self.startlabel = tkinter.Label(frame1, text='date')
        self.startdate.pack()
        self.startlabel.pack(pady='20')
        self.label1 = tk.Label(frame1, text="Start time : 24h 00:00")
        self.label1.pack()
        self.Shour_label = ttk.Label(frame1, text="Hour:")
        self.Shour_label.pack()
        self.Shour_combobox = ttk.Combobox(frame1, values=list(range(24)))
        self.Shour_combobox.pack()

        # Minute selection
        self.Sminute_label = ttk.Label(frame1, text="Minute:")
        self.Sminute_label.pack()
        self.Sminute_combobox = ttk.Combobox(frame1, values=list(range(60)))
        self.Sminute_combobox.pack()

        self.endcal = Calendar(frame1, date_pattern="Y-mm-DD")
        self.endcal.pack(fill='x')

        self.enddate = tkinter.Button(frame1, text="enter end date", command=self.getEndDate)
        self.endlabel = tkinter.Label(frame1, text='date')
        self.enddate.pack(ipadx=10)
        self.endlabel.pack(pady='20')
        self.label2 = tk.Label(frame1, text="End time : 24h 00:00")
        self.label2.pack()
        self.Ehour_label = ttk.Label(frame1, text="Hour:")
        self.Ehour_label.pack()
        self.Ehour_combobox = ttk.Combobox(frame1, values=list(range(24)))

        self.Ehour_combobox.pack()

        # Minute selection
        self.Eminute_label = ttk.Label(frame1, text="Minute:")
        self.Eminute_label.pack()
        self.Eminute_combobox = ttk.Combobox(frame1, values=list(range(60)))
        self.Eminute_combobox.pack()
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
        Shour = self.Shour_combobox.get()
        Sminute = self.Sminute_combobox.get()
        Ehour = self.Ehour_combobox.get()
        Eminute = self.Eminute_combobox.get()

        Shourint = int(Shour)
        if Shourint < 10:
            Shour="0"+Shour

        Sminuteint = int(Sminute)
        if Sminuteint < 10:
            Sminute = "0" + Sminute

        Ehourint = int(Ehour)
        if Ehourint < 10:
            Ehour="0"+Ehour

        Eminuteint = int(Eminute)
        if Eminuteint < 10:
            Eminute = "0" + Eminute

        Starttime=f"{Shour}:{Sminute}"
        Endtime=f"{Ehour}:{Eminute}"
        print(Starttime)
        connection = sqlite3.connect("k7.db")
        c = connection.cursor()
        x = c.execute(f"SELECT PType FROM KSU WHERE ID = {int(getlogIDUser)}").fetchone()
        type = x[0]
        z = c.execute(f"SELECT CartCollege FROM Cart WHERE CartID = {self.cartid.get()}").fetchone()
        CartCollege = z[0]
        # type[0] why?   = function returns   type=(student,)
        # values=["Student", "Employee", "Faculty"]

        reserved="true"
        connection.execute(
            f"INSERT INTO Reservations VALUES('{int(getlogIDUser)}','{self.combBox.get()}','{CartCollege}','{self.startcal.get_date()}','{self.endcal.get_date()}','{reserved}','{Starttime}','{Endtime}')")
        logging.info(f"Transaction info =(Log ID: {int(getlogIDUser)},CartCollege: {CartCollege},Cart ID: {self.combBox.get()},Start Date: {self.startcal.get_date()},End Date: {self.endcal.get_date()},Start time:{Starttime},End time:{Endtime})")
        connection.commit()

    def go_signup(self):
        self.window.destroy()
        import Signup
        Signup.Signup()

    def difTime(self):
       Shour= self.Shour_combobox
       Sminute=self.Sminute_combobox
       startTime=Shour*60+Sminute
       Ehour = self.Ehour_combobox
       Eminute = self.Eminute_combobox
       endTime = Ehour * 60 + Eminute
       if (endTime<startTime):
        tkinter.messagebox.showinfo('Error', "you cant choose End Time earlier than Start Time")
       dif=endTime- startTime
       return dif
    def refresh(self):
        self.window.destroy()
        import User
        User.User()

