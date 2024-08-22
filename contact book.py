import tkinter as tk
from tkinter import messagebox

contact = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contact[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", f"Contact {name} added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required fields!")

def display_contacts():
    display_window = tk.Toplevel(root)
    display_window.title("Contact List")
    
    for name, info in contact.items():
        tk.Label(display_window, text=f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}").pack()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Manager")

tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0)
tk.Button(root, text="Display Contacts", command=display_contacts).grid(row=4, column=1)

root.mainloop()
