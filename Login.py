import tkinter as tk
import re
import hashlib
import csv
import sqlite3
from tkcalendar import Calendar
import logging
import tkinter.messagebox

class Login:
    global getlogID
    def __init__(self):
        global getlogID
        global logidentry, logpassentry
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry('400x400')
        self.buttonBack = tk.Button(self.window, text='Sign up', command=self.go_signup)
        self.loglabel1 = tk.Label(self.window, text="ID:")
        self.logidentry = tk.Entry(self.window, width='20')
        self.loglabel1.grid(column='0', row='0', padx=10, pady=10)
        self.logidentry.grid(column='1', row='0', padx=10, pady=10)
        self.loglabel2 = tk.Label(self.window, text="Password:")
        self.logpassentry = tk.Entry(self.window, width="20")
        self.loglabel2.grid(column='0', row='1', padx=10, pady=10)
        self.logpassentry.grid(column='1', row='1', padx=10, pady=10)

        self.loginButon = tk.Button(self.window, text="login", width='5', command=self.validateLogin, bg='gray')
        self.loginButon.grid(columnspan=2, row=2, sticky='ew')
        getlogID = self.logidentry.get()
        self.window.mainloop()

    def validateLogin(self):
        global getlogID

        password = self.logpassentry.get()
        passhash = hashlib.sha256(password.encode()).hexdigest()

        getlogID = self.logidentry.get()
        getlogID2=getlogID
        connection = sqlite3.connect("k7.db")
        passmatch = connection.execute(
            f"SELECT count() FROM KSU WHERE PASSWORD = '{passhash}'").fetchone()  # returns 1 if  pass found OR 0 IF NOT FOUND
        adminpassmatch = connection.execute(
            f"SELECT count() FROM KSU WHERE PASSWORD = '{passhash}' and ID ={getlogID} and LENGTH(ID) <6").fetchone()  # returns 1 if admin pass found OR 0 IF NOT FOUND

        #adminpassmatch[0] why?   =The COUNT() function returns the number of rows that matches a specified criterion.    adminpassmatch=(1,)
        if adminpassmatch[0] == 1:
                self.window.destroy()
                import Admin
                Admin.Admin()
        else:
            print("Not Admin")

        idPat = re.compile("^[0-9]{10}$")
        idPat6 = re.compile("^[0-9]{6}$")
        if not (re.search(idPat, getlogID) or re.search(idPat6, getlogID)):
            if adminpassmatch[0] != 1:
             tk.messagebox.showinfo('Error', "ID must contain exactly 10  or 6 Numbers")
             return

        if passmatch[0] == 0:
            tk.messagebox.showinfo('Error', "wrong pass")
            return
        if adminpassmatch[0] != 1:
            self.window.destroy()
            import User
            User.getlogIDUser = getlogID2
            User.User()


        connection.close()
    def go_signup(self):
        self.window.destroy()
        import Signup
        Signup.Signup()

