import tkinter as tk
from tkinter import messagebox


def check_account():
    account_number = account_entry.get()


    if account_number.startswith('8'):
        messagebox.showinfo('Account Check', 'This is a Savings Account.')
    elif account_number.startswith('9'):
        messagebox.showinfo('Account Check', 'This is a Current Account.')
    else:
        messagebox.showinfo('Account Check', 'Invalid Account Number.')


window = tk.Tk()
window.title("Account Type Checker")

account_label = tk.Label(window, text="Account Number:")
account_label.pack()

account_entry = tk.Entry(window)
account_entry.pack()

check_button = tk.Button(window, text="Check Account", command=check_account)
check_button.pack()

window.mainloop()
