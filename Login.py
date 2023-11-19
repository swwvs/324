import tkinter as tk
import re
import hashlib
import csv
import sqlite3
import tkinter.messagebox
class Login:
    def __init__(self):
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
        self.window.mainloop()

    def validateLogin(self):
        global getlogID

        password = self.logpassentry.get()
        passhash = hashlib.sha256(password.encode()).hexdigest()

        getlogID = self.logidentry.get()
        connection = sqlite3.connect("k6.db")
        adminIdmatch = connection.execute(
            "select ID from KSU where LENGTH(ID) >9").fetchall()  # returns all admins wich ids length > 9
        passmatch = connection.execute(
            f"SELECT count() FROM KSU WHERE PASSWORD = '{passhash}'").fetchone()  # returns 1 if stu pass found OR 0 IF NOT FOUND
        adminpassmatch = connection.execute(
            f"SELECT count() FROM KSU WHERE PASSWORD = '{passhash}' and ID ={self.logidentry.get()} and LENGTH(ID) >9").fetchone()  # returns 1 if admin pass found OR 0 IF NOT FOUND
        print(adminpassmatch[0])

        row = [x[0] for x in adminIdmatch]  # check id is more than if true he is admin

        for x in row:
            # print("typ x: ", type(x), "type gt", type(getlogID))
            if int(getlogID) == int(x):
                if adminpassmatch[0] == 1:
                    self.window.destroy()
                    import Admin
                    Admin.Admin()
            else:
                print("Not Admin")

        idPat = re.compile("^[0-9]{9}$")
        if not re.search(idPat, getlogID):
            tk.messagebox.showinfo('Error', "ID must contain exactly 9 Numbers")
            return

        if passmatch[0] == 0:
            tk.messagebox.showinfo('Error', "wrong pass")
            return
        self.window.destroy()
        import User
        User.User()
        connection.close()
    def go_signup(self):
        self.window.destroy()
        import Signup
        Signup.Signup()
