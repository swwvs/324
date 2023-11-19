
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
connection.commit()
connection.close()