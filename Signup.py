import tkinter as tk
import re
import hashlib
import csv
import sqlite3
from tkcalendar import Calendar
import logging
import tkinter.messagebox
class Signup:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sign up")

        # to position the window in the center
        self.buttonBack = tk.Button(self.window, text='Login', command=self.go_Login)
        self.buttonBack.grid(column=2, row=6, columnspan=2, sticky='ew')
        self.label1 = tk.Label(self.window, text="First Name:")
        self.entry1 = tk.Entry(self.window, width="22")
        self.label1.grid(column=0, row=0, pady=10)
        self.entry1.grid(column=1, row=0, padx=10)
        self.label2 = tk.Label(self.window, text="Last Name:")
        self.entry2 = tk.Entry(self.window, width="22")
        self.label2.grid(column=2, row=0, pady=10)
        self.entry2.grid(column=3, row=0, padx=10)
        self.label3 = tk.Label(self.window, text=" ID:")
        self.idEntry = tk.Entry(self.window, width="20")
        self.label3.grid(column=0, row=1, pady=10)
        self.idEntry.grid(column=1, row=1, padx=10)

        self.label4 = tk.Label(self.window, text="Password:")
        self.passEntry = tk.Entry(self.window, width='20')
        self.label4.grid(column=2, row=1, pady=10)
        self.passEntry.grid(column=3, row=1, padx=10)

        self.emailLabel = tk.Label(self.window, text="Email:")
        self.emailEntry = tk.Entry(self.window, width="24")
        self.emailLabel.grid(column=0, row=2, pady=10)
        self.emailEntry.grid(column=1, row=2, padx=10)

        self.label6 = tk.Label(self.window, text="Phone Number:")
        self.phoneEntry = tk.Entry(self.window, width="20")
        self.label6.grid(column=2, row=2, pady=10)
        self.phoneEntry.grid(column=3, row=2, padx=10)
        self.team_label = tk.Label(self.window, text="type:")
        self.team_label.grid(row=5, column=0)
        type_var = tk.StringVar()
        self.team_radio_a = tk.Radiobutton(self.window, text="Student", value="Student", variable=type_var)
        self.team_radio_a.grid(row=5, column=1)
        self.team_radio_b = tk.Radiobutton(self.window, text="Faculty", value="Faculty", variable=type_var)
        self.team_radio_b.grid(row=5, column=2)
        self.team_radio_c = tk.Radiobutton(self.window, text="Employee", value="Employee", variable=type_var)
        self.team_radio_c.grid(row=5, column=3)
        self.type9 = type_var
        self.button1 = tk.Button(self.window, text="Enter", command=self.action, bg='gray')
        self.button1.grid(row='6', column='0', columnspan=2, sticky='ew')


        self.window.mainloop()

    def go_Login(self):
        self.window.destroy()
        import Login
        Login.Login()

    def action(self):
            password = self.passEntry.get()
            passhash = hashlib.sha256(password.encode()).hexdigest()
            global id
            fname = self.entry1.get()
            lname = self.entry2.get()
            id = self.idEntry.get()
            phone = self.phoneEntry.get()
            email = self.emailEntry.get()
            typeo =self.type9.get()

            connection = sqlite3.connect("k7.db")
            checkHaveAcc = connection.execute(f"select count() from KSU WHERE ID = {self.idEntry.get()} ").fetchone()
            print(checkHaveAcc[0])
            if checkHaveAcc[0] == 1:
                    tk.messagebox.showinfo('Error', 'You already have Account')

            passPat = re.compile("^[a-zA-Z0-9]{6,}$")
            idPat = re.compile("^[0-9]{10}$")
            emailVld = re.compile("^([a-zA-Z0-9\._-]+)(@student\.ksu\.edu\.sa)$")
            phoneVld = re.compile("^(05)[0-9]{8}$")

            if not re.search(passPat, password):
                    tk.messagebox.showinfo('Error', "Wrong input Password should have at least 6 or more digits ")
                    return

            if not re.search(idPat, id):
                    tk.messagebox.showinfo('Error', "ID must contain exactly 10 Numbers")
                    return

            if not re.search(emailVld, email):
                    tk.messagebox.showinfo('Error', "wrong email")
                    return

            if not re.search(phoneVld, phone):
                    tk.messagebox.showinfo('Error', "wrong phone")
                    return

            connection.execute(f"INSERT INTO KSU VALUES('{fname}','{lname}',{id},'{passhash}','{email}',{phone},'{typeo}')")
            print("Data added")
            connection.commit()
            connection.close()
Signup()

