import tkinter as tk
from tkinter import messagebox
import dashboard
import database


def login(event=None):
    id_no = id_entry.get()
    password = password_entry.get()

    #Authenticate the user
    if database.authenticate(id_no, password):
        messagebox.showinfo("Login", "Login successful!")
        window.destroy()
        dashboard.open_dashboard(id_no)
    else:
        messagebox.showerror("Login", "Login failed!")

    

# Create the main window
window = tk.Tk()
window.title("Login")
window.geometry("300x200")

# Create the username label and entry
id_label = tk.Label(window, text="Id number:")
id_label.pack()
id_entry = tk.Entry(window)
id_entry.pack()

# Create the password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create the login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

# Browse import
def open_browse():
    import browse
    browse.browser()

# Browse the database
browse_button = tk.Button(window, text="Browse", command=open_browse)
browse_button.pack()

# Bind the Enter key to the login function
window.bind("<Return>", login)

# Run the main window's event loop
window.mainloop()
