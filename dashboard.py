import tkinter as tk
from tkinter import ttk
import database

def open_dashboard(id_no):
    # Create the dashboard window
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")

    # Add dashboard content
    dashboard_label = tk.Label(dashboard, text="Welcome to the Dashboard!")
    dashboard_label.pack()

    # Create the Treeview widget
    treeview = ttk.Treeview(dashboard)
    treeview.pack(fill="both", expand=True)

    # Add columns to the Treeview
    treeview["columns"] = ("ID", "Name")
    treeview.column("#0", width=0, stretch=tk.NO)  # Hide the default column
    treeview.column("ID", width=100, anchor=tk.CENTER)
    treeview.column("Name", width=200, anchor=tk.W)

    # Add column headings
    treeview.heading("ID", text="ID Number")
    treeview.heading("Name", text="Name")

    # Display users personal information
    Personal_label = tk.Label(dashboard, text="Personal information")
    Personal_label.pack()

    # Function to update the name in the Treeview
    def update_name_in_treeview(event=None):
        user_data = database.get_user_data(id_no)
        treeview.set(treeview.selection(), column="Name", value=user_data["name"])

    # Fetch the user's data from the database
    user_data = database.get_user_data(id_no)

    # Add the user's data to the Treeview
    treeview.insert(parent="", index="end", iid=0, text="", values=(user_data["id_no"], user_data["name"]))

    # Edit name function
    def edit_name():
        # Create the edit window
        edit_window = tk.Toplevel(dashboard)
        edit_window.geometry("200x200")
        edit_window.title("Edit Name")

        # Label and entry for name
        tk.Label(edit_window, text="Name:").pack()
        name_entry = tk.Entry(edit_window)
        name_entry.pack()
        name_entry.insert(0, user_data["name"])

        # Save button function
        def save_name(event=None):
            new_name = name_entry.get()
            # Update name in the database
            database.update_name(id_no, new_name)
            # Update name in the Treeview
            treeview.set(treeview.selection(), column="Name", value=new_name)
            # Close the edit window
            edit_window.destroy()

        # Save button
        tk.Button(edit_window, text="Save", command=lambda: (save_name(), update_name_in_treeview())).pack()
        edit_window.bind("<Return>", lambda event: (save_name(), update_name_in_treeview()))

    # Edit button
    edit_button = tk.Button(dashboard, text="Edit", command=edit_name)
    edit_button.pack()


    # Run the dashboard window's event loop
    dashboard.mainloop()

# Call the open_dashboard() function to open the dashboard window
if __name__ == "__main__":
    
    open_dashboard()
