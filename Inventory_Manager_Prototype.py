import tkinter as tk
from tkinter import ttk

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GreenGrove Farms Inventory Management System")

        # Variables to store product information
        self.products = []
        self.selected_product = None

        # Creating a frame
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        # Product Name
        self.product_name_label = ttk.Label(self.frame, text="Product Name:")
        self.product_name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.product_name_entry = ttk.Entry(self.frame)
        self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Product Quantity
        self.product_quantity_label = ttk.Label(self.frame, text="Quantity:")
        self.product_quantity_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.product_quantity_entry = ttk.Entry(self.frame)
        self.product_quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        # Product Expiry Date
        self.product_expiry_label = ttk.Label(self.frame, text="Expiry Date:")
        self.product_expiry_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.product_expiry_entry = ttk.Entry(self.frame)
        self.product_expiry_entry.grid(row=2, column=1, padx=5, pady=5)

        # Add Product Button
        self.add_product_button = ttk.Button(self.frame, text="Add Product", command=self.add_product)
        self.add_product_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Product List
        self.product_list_label = ttk.Label(self.frame, text="Product List:")
        self.product_list_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.product_listbox = tk.Listbox(self.frame, height=10, width=40)
        self.product_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.product_listbox.bind('<<ListboxSelect>>', self.select_product)

        # Delete Product Button
        self.delete_product_button = ttk.Button(self.frame, text="Delete Product", command=self.delete_product)
        self.delete_product_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Export Inventory Button
        self.export_button = ttk.Button(self.frame, text="Export Inventory", command=self.export_inventory)
        self.export_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_product(self):
        name = self.product_name_entry.get()
        quantity = self.product_quantity_entry.get()
        expiry = self.product_expiry_entry.get()

        if name and quantity and expiry:
            product = (name, quantity, expiry)
            self.products.append(product)
            self.update_product_listbox()
            self.clear_entries()
        else:
            self.show_error_message("Please fill in all fields.")

    def update_product_listbox(self):
        self.product_listbox.delete(0, tk.END)
        for product in self.products:
            self.product_listbox.insert(tk.END, product[0])

    def select_product(self, event):
        try:
            index = self.product_listbox.curselection()[0]
            self.selected_product = self.products[index]
        except IndexError:
            pass

    def delete_product(self):
        if self.selected_product:
            self.products.remove(self.selected_product)
            self.update_product_listbox()
            self.clear_entries()
        else:
            self.show_error_message("Please select a product to delete.")

    def export_inventory(self):
        # Functionality for exporting the inventory to be added
        pass

    def clear_entries(self):
        self.product_name_entry.delete(0, tk.END)
        self.product_quantity_entry.delete(0, tk.END)
        self.product_expiry_entry.delete(0, tk.END)

    def show_error_message(self, message):
        error_message_window = tk.Toplevel()
        error_message_window.title("Error")
        error_label = ttk.Label(error_message_window, text=message)
        error_label.pack(padx=20, pady=20)
        ok_button = ttk.Button(error_message_window, text="OK", command=error_message_window.destroy)
        ok_button.pack(pady=10)


def main():
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
