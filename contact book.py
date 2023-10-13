import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        # Labels
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Phone Number:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)

        # Entry Fields
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=lambda: self.blink_button(self.add_button, self.add_contact))
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        self.update_button = tk.Button(root, text="Update Contact", command=lambda: self.blink_button(self.update_button, self.update_contact))
        self.update_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        self.delete_button = tk.Button(root, text="Delete Contact", command=lambda: self.blink_button(self.delete_button, self.delete_contact))
        self.delete_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        self.search_button = tk.Button(root, text="Search Contact", command=lambda: self.blink_button(self.search_button, self.search_contact))
        self.search_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        self.display_button = tk.Button(root, text="Display Contacts", command=lambda: self.blink_button(self.display_button, self.display_contacts))
        self.display_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        # Text Box for Displaying Contacts
        self.contact_display = tk.Text(root, height=10, width=40)
        self.contact_display.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

    def blink_button(self, button, action):
        original_bg = button.cget("background")
        button.configure(background="green")
        self.root.update()
        self.root.after(200, lambda: button.configure(background=original_bg))
        action()

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()[:10]  # Limit to the first 10 characters
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and len(phone_number) == 10:
            self.contacts[name] = {
                "Phone Number": phone_number,
                "Email": email,
                "Address": address,
            }
            messagebox.showinfo("Success", f"Added {name} to the contact book.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Both Name and a 10-digit Phone Number are required.")

    def update_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()[:10]  # Limit to the first 10 characters
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name in self.contacts:
            self.contacts[name] = {
                "Phone Number": phone_number,
                "Email": email,
                "Address": address,
            }
            messagebox.showinfo("Success", f"Updated {name}'s contact details.")
            self.clear_entries()
        else:
            messagebox.showinfo("Contact Not Found", f"{name} not found in the contact book.")
            self.clear_entries()

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Deleted {name} from the contact book.")
            self.clear_entries()
        else:
            messagebox.showinfo("Contact Not Found", f"{name} not found in the contact book.")
            self.clear_entries()

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            contact_info = self.contacts[name]
            message = f"Name: {name}\n"
            for field, value in contact_info.items():
                message += f"{field}: {value}\n"
            messagebox.showinfo("Contact Found", message)
            self.clear_entries()
        else:
            messagebox.showinfo("Contact Not Found", f"{name} not found in the contact book.")
            self.clear_entries()

    def display_contacts(self):
        if self.contacts:
            self.contact_display.delete(1.0, tk.END)
            contact_list = ""
            for name, contact_info in self.contacts.items():
                contact_list += f"Name: {name}\n"
                for field, value in contact_info.items():
                    contact_list += f"{field}: {value}\n"
                contact_list += "\n"
            self.contact_display.insert(tk.END, contact_list)
        else:
            messagebox.showinfo("Contact Book", "Contact book is empty.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
