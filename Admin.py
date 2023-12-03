import tkinter as tk
import re
import hashlib
import csv
import sqlite3
from tkcalendar import Calendar
import logging
import tkinter.messagebox
class Admin:
   def __init__(self):
      self.window = tk.Tk()
      self.window.title("Admin")
      self.window.geometry('500x500')
      self.label1 = tk.Label(self.window, text="cart plate number:")
      self.entry1 = tk.Entry(self.window, width="22")
      self.label1.grid(column=0, row=0, pady=10)
      self.entry1.grid(column=1, row=0, padx=10)
      self.label2 = tk.Label(self.window, text="college Name:")
      self.entry2 = tk.Entry(self.window, width="22")
      self.label2.grid(column=2, row=0, pady=10)
      self.entry2.grid(column=3, row=0, padx=10)
      self.buttonBack = tk.Button(self.window, text='Logout', command=self.logout)
      self.buttonBack.grid(column=3, row=3, columnspan=2, sticky='ew')
      self.button1 = tk.Button(self.window, text="Enter",command=self.create,  bg='gray')
      self.button1.grid(row=3, column=0, columnspan=2, sticky='ew')
      self.button2 = tk.Button(self.window, text="Backup ", bg='gray', command=self.toCSV)
      self.button2.grid(row=5, column=0, columnspan=2, sticky='ew')
      self.window.mainloop()

   def logout(self):
      self.window.destroy()
      import Signup
      Signup.Signup()

   def toCSV(self):
      connection = sqlite3.connect("k7.db")

      t1 = connection.execute("select * from KSU")
      t2 = connection.execute("select * from Cart")
      t3 = connection.execute("select * from Reservations")

      file = open("student.csv", 'w', newline='')
      csvwriter = csv.writer(file)

      for row in t1:
         csvwriter.writerow(row)

      for row in t2:
         csvwriter.writerow(row)

      for row in t3:
         csvwriter.writerow(row)

      file.close()
      connection.close()

   def create(self):
      plate=self.entry1.get()
      collage=self.entry2.get()
      idPat = re.compile("^[0-9]{3}$")
      connection = sqlite3.connect("k7.db")
      checkHavecart = connection.execute(f"select count() from Cart WHERE CartID = {self.entry1.get()} ").fetchone()

      if checkHavecart[0] == 1:
         tk.messagebox.showinfo('Error', 'You already have the Cart')
      if not re.search(idPat, plate):
         tk.messagebox.showinfo('Error', "CartID must contain exactly 3 Numbers")
         return
      connection.execute(f"INSERT INTO Cart VALUES('{plate}','{collage}')")

      connection.commit()
      connection.close()
