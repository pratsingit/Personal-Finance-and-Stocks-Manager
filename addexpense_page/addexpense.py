from mysql.connector import Error
from tkinter import messagebox
from tkinter import *
from datetime import datetime


import random
import mysql.connector
import tkinter as tk
import sys


from pathlib import Path


sys.path.append(str(Path("A:\\Final_Project\\login_page\\login.py").parent.parent))


from login_page.login import login


path = "A:\\Final_Project\\addexpense_page\\"


class addexpense(tk.Frame):

    def is_valid_amount(amount):
        if not amount.isdigit():
            return False
        return True

    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def is_valid_source(source):
        return all(char.isalpha() or char.isspace() for char in source)

    def generate_unique_number():
        used_numbers = set()
        while True:
            num = random.randint(1000, 9999)
            if num not in used_numbers:
                used_numbers.add(num)
                return num

    def is_valid_debit_account(debit_account):

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="Personal_Finance_Management"
            )
            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT account_id FROM Account WHERE account_id = %s"
                cursor.execute(query, (debit_account,))
                if cursor.fetchall():
                    return True
                else:
                    return False

        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def is_valid_category(category):
        return all(char.isalpha() or char.isspace() for char in category)
    
    def insert_expense(amount, date, source, remarks, debit_account, category):
        
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='Personal_Finance_Management'
            )

            if connection.is_connected():
                cursor = connection.cursor()
                user_id = login.loggedin_userid
                account_id = debit_account
                date_datetime = datetime.strptime(date, '%d-%m-%Y')
                date_mysql_format = date_datetime.strftime('%Y-%m-%d')
                expense_id = addexpense.generate_unique_number()
                balance_query = f"SELECT balance FROM Account WHERE account_id = '{account_id}' AND user_id = 8491"
                cursor.execute(balance_query)
                current_balance = cursor.fetchone()[0]
                if float(current_balance) < float(amount):
                    return "insufficient_balance"
                query = f"INSERT INTO Expenditure (expense_id, user_id, account_id, expense, expense_date, source, remarks, category) VALUES ('{expense_id}', 8491, '{account_id}', '{amount}', '{date_mysql_format}', '{source}', '{remarks}', '{category}')"
                cursor.execute(query)
                update_query = f"UPDATE Account SET balance = balance - {amount} WHERE account_id = '{account_id}' AND user_id = 8491"
                cursor.execute(update_query)
                connection.commit()
                return True

        except Error as e:
            print("Error while connecting to MySQL", e)
            return False

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg='#093545')

        global img0, img1, background_img, entry0_img, entry1_img, entry2_img, entry3_img, entry4_img, entry5_img
        
        def clear_entry_fields():
            entry0.delete(0, tk.END)
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            entry3.delete(0, tk.END)
            entry4.delete(0, tk.END)
            entry5.delete(0, tk.END)

        self.controller = controller

        background_img = tk.PhotoImage(file=path + "addexpense0.png")

        bck_label = tk.Label(self, image=background_img,
                             relief="flat", bg="#093545")

        bck_label.place(x=0, y=0, width=1537, height=864)

        entry0_img = tk.PhotoImage(file=path + "addexpense1.png")

        entry0_label = tk.Label(self, image=entry0_img,
                                relief="flat", bg="#093A45")

        entry0_label.place(x=266, y=273, width=441, height=54)

        entry0_font = ("Lexend Deca", 20)

        entry0 = tk.Entry(self,
                          bd=0,
                          bg="#093A45",
                          highlightthickness=0,
                          font=entry0_font,
                          fg="white")

        entry0.place(x=276, y=273,
                     width=421,
                     height=52)

        entry1_img = tk.PhotoImage(file=path + "addexpense2.png")

        entry1_label = tk.Label(self, image=entry1_img,
                                relief="flat", bg="#093A45")

        entry1_label.place(x=851, y=405, width=441, height=54)

        entry1_font = ("Lexend Deca", 20)

        entry1 = tk.Entry(self,
                          bd=0,
                          bg="#093A45",
                          highlightthickness=0,
                          font=entry1_font,
                          fg="white")

        entry1.place(
            x=861, y=405,
            width=421,
            height=52)

        entry2_img = tk.PhotoImage(file=path + "addexpense3.png")

        entry2_label = tk.Label(self, image=entry2_img,
                                relief="flat", bg="#093A45")

        entry2_label.place(x=851, y=536, width=441, height=54)

        entry2_font = ("Lexend Deca", 20)

        entry2 = tk.Entry(self,
                          bd=0,
                          bg="#093A45",
                          highlightthickness=0,
                          font=entry2_font,
                          fg="white")

        entry2.place(
            x=861, y=536,
            width=421,
            height=52)

        entry3_img = tk.PhotoImage(file=path + "addexpense4.png")

        entry3_label = tk.Label(self, image=entry3_img,
                                relief="flat", bg="#093A45")

        entry3_label.place(x=851, y=273, width=441, height=54)

        entry3_font = ("Lexend Deca", 20)

        entry3 = tk.Entry(self,
                          bd=0,
                          bg="#093A45",
                          highlightthickness=0,
                          font=entry3_font,
                          fg="white")

        entry3.place(
            x=861, y=273,
            width=421,
            height=52)

        entry4_img = tk.PhotoImage(file=path + "addexpense5.png")

        entry4_label = tk.Label(self, image=entry4_img,
                                relief="flat", bg="#093A45")

        entry4_label.place(x=266, y=405, width=441, height=54)

        entry4_font = ("Lexend Deca", 20)

        entry4 = tk.Entry(self,
                          bd=0,
                          bg="#093A45",
                          highlightthickness=0,
                          font=entry4_font,
                          fg="white")

        entry4.place(
            x=276, y=405,
            width=421,
            height=52)

        entry5_img = tk.PhotoImage(file=path + "addexpense6.png")

        entry5_label = tk.Label(self, image=entry5_img,
                                relief="flat", bg="#093A45")

        entry5_label.place(x=266, y=536, width=441, height=54)

        entry5_font = ("Lexend Deca", 20)

        entry5 = tk.Entry(self,
                          bd=0,
                          bg="#093A45",
                          highlightthickness=0,
                          font=entry5_font,
                          fg="white")

        entry5.place(
            x=276, y=536,
            width=421,
            height=52)

        def b0_clicked():

            amount = entry0.get()
            date = entry4.get()
            source = entry5.get()
            remarks = entry3.get()
            debit_account = entry1.get()
            category = entry2.get()

            if not all([amount, date, source, remarks, debit_account, category]):
                tk.messagebox.showerror("Error", "Please fill all the fields")
                return

            if not addexpense.is_valid_debit_account(debit_account):
                tk.messagebox.showerror("Error", "Invalid Debit Account")
                return

            if not addexpense.is_valid_date(date):
                tk.messagebox.showerror("Error", "Invalid Transaction Date")
                return

            if not addexpense.is_valid_amount(amount):
                tk.messagebox.showerror("Error", "Invalid amount")
                return

            if not addexpense.is_valid_source(source):
                tk.messagebox.showerror(
                    "Error", "Invalid Source")
                return
            
            if not addexpense.is_valid_category(category):
                tk.messagebox.showerror(
                    "Error", "Invalid Category")
                return

            result = addexpense.insert_expense(
                amount, date, source, remarks, debit_account, category)
            if result == "insufficient_balance":
                tk.messagebox.showerror(
                    "Error", "Insufficient account balance")
            elif result:
                tk.messagebox.showinfo(
                    "Success", "Expense added successfully!")
                controller.show_frame("myexpenses")
            else:
                tk.messagebox.showerror(
                    "Error", "Failed to add account. Please try again.")

        img0 = tk.PhotoImage(file=path + "addexpense7.png")
        b0 = tk.Button(self,
                       image=img0,
                       borderwidth=0,
                       highlightthickness=0,
                       command=b0_clicked,
                       bg="#092f40",
                       background="#092f40",
                       activebackground="#092f40",
                       cursor="hand2",
                       relief="flat")

        b0.place(
            x=796, y=661,
            width=266,
            height=62)

        def b1_clicked():
            print("b1 clicked")

        img1 = tk.PhotoImage(file=path + "addexpense8.png")

        b1 = tk.Button(self,
                       image=img1,
                       borderwidth=0,
                       highlightthickness=0,
                       command=b1_clicked,
                       bg="#092f40",
                       background="#092f40",
                       activebackground="#092f40",
                       cursor="hand2",
                       relief="flat")

        b1.place(
            x=477, y=661,
            width=266,
            height=62)
