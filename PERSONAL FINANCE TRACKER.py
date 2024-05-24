import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class Transaction:
    def __init__(self, amount, category, transaction_type, date):
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.date = date


class FinanceTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.transactions = []

        tk.Label(root, text="Amount:").grid(row=0, column=0, sticky="w")
        tk.Label(root, text="Category:").grid(row=1, column=0, sticky="w")
        tk.Label(root, text="Type:").grid(row=2, column=0, sticky="w")
        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="w")

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)

        self.transaction_type_var = tk.StringVar(root)
        self.transaction_type_var.set("Expenses")
        self.transaction_type_menu = tk.OptionMenu(root, self.transaction_type_var, "Expenses", "Income", "Transfer")
        self.transaction_type_menu.grid(row=2, column=1, sticky="ew")
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=3, column=1)

        tk.Button(root, text="Add Transaction", command=self.add_transaction).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(root, text="View Transactions", command=self.view_transactions).grid(row=5, column=0, columnspan=2, pady=10)

    def add_transaction(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        transaction_type = self.transaction_type_var.get()
        date = self.date_entry.get()

        if not all((amount, category, date)):
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        try:
            amount = float(amount)
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")
            return

        transaction = Transaction(amount, category, transaction_type, date)
        self.transactions.append(transaction)
        messagebox.showinfo("Success", "Transaction added successfully.")
        self.clear_entry_fields()

    def view_transactions(self):
        if not self.transactions:
            messagebox.showinfo("No Transactions", "No transactions found.")
            return

        transactions_text = ""
        for idx, transaction in enumerate(self.transactions, start=1):
            transactions_text += f"{idx}. {transaction.transaction_type}Amount: ₱{transaction.amount}\n Category: {transaction.category}\n Date: {transaction.date}\n"

        messagebox.showinfo("Transactions", transactions_text)

    def clear_entry_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)


def authenticate(username, password):
    if username == "babyjack" and password == "12345678":
        print("Login Successful!")
        on_login_success()
    else:
        on_login_failure()


def on_login_success():
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()


def on_login_failure():
    messagebox.showerror("Login Failed", "Invalid username or password.")


def show_login_window():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.config(bg="#f5f5f5")

    username_label = tk.Label(login_window, text="Username:", font=("Arial", 12), bg="#f5f5f5")
    username_label.pack(pady=5, padx=20, anchor="w")
    username_entry = tk.Entry(login_window, font=("Arial", 12))
    username_entry.pack(pady=5, padx=20, ipady=5, ipadx=10)

    password_label = tk.Label(login_window, text="Password:", font=("Arial", 12), bg="#f5f5f5")
    password_label.pack(pady=5, padx=20, anchor="w")
    password_entry = tk.Entry(login_window, show="*", font=("Arial", 12))
    password_entry.pack(pady=5, padx=20, ipady=5, ipadx=10)

    login_button = tk.Button(login_window, text="Login",
                             command=lambda: authenticate(username_entry.get(), password_entry.get()),
                             font=("Arial", 12, "bold"), bg="#4caf50", fg="white")
    login_button.pack(pady=10, padx=20, ipady=5, ipadx=10, anchor="w")

    login_window.mainloop()


show_login_window()
