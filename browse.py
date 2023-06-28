import tkinter as tk
from tkinter import ttk
import database

def browser():
    # Create the browse window
    browse_window = tk.Toplevel()
    browse_window.title("Browse")
    browse_window.geometry("400x300")

    # Create the search frame
    search_frame = tk.Frame(browse_window)
    search_frame.pack(pady=10)

    # Create the search label and entry
    search_label = tk.Label(search_frame, text="Search by ID:")
    search_label.pack(side=tk.LEFT)
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT)

    # Create the Treeview widget
    treeview = ttk.Treeview(browse_window)
    treeview.pack(fill="both", expand=True)

    # Add columns to the Treeview
    treeview["columns"] = ("Id", "Name")
    treeview.column("#0", width=0, stretch=tk.NO)  # Hide the default column
    treeview.column("Id", width=100, anchor=tk.CENTER)
    treeview.column("Name", width=150, anchor=tk.W)
    

    # Add column headings
    treeview.heading("Id", text="ID Number")
    treeview.heading("Name", text="Name")

    # Fetch the users from the database
    users = database.browse()

    
    # Insert data into the Treeview
    for row in users:
        treeview.insert("", tk.END, values=(row[0], row[1]))

    # Function to search for a user by ID
    def search_id(event=None):
        search_text = search_entry.get()
        filtered_data = database.search_data_by_id(search_text)
        # Clear existing data in the Treeview
        treeview.delete(*treeview.get_children())
        # Insert filtered data into the Treeview
        for row in filtered_data:
            treeview.insert("", tk.END, values=(row["Id"], row["Name"]))

    # Bind the Enter key to the search function
    search_entry.bind("<Return>", search_id)

    # Run the browse window's event loop
    browse_window.mainloop()

if __name__ == "__main__":
    browser()