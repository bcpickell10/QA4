import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GreenGrove Farms Inventory Management System")
        
        # Inventory data
        self.inventory = {
            "Tomatoes": {"quantity": 100, "batch": "Batch 001", "purchase_date": "2024-04-24", "expiry_date": "2024-05-15", "upc": "123456789012"},
            "Apples": {"quantity": 80, "batch": "Batch 002", "purchase_date": "2024-04-20", "expiry_date": "2024-05-10", "upc": "123456789013"},
            "Lettuce": {"quantity": 50, "batch": "Batch 001", "purchase_date": "2024-04-22", "expiry_date": "2024-05-12", "upc": "123456789014"}
        }
        
        # Sales data
        self.sales = {
            "Tomatoes": {"quantity_sold": 0, "price": 2.5},
            "Apples": {"quantity_sold": 0, "price": 1.75},
            "Lettuce": {"quantity_sold": 0, "price": 3.0}
        }

        # Create notebook
        self.notebook = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Inventory")
        self.notebook.add(self.tab2, text="Sales & Supply Data")
        self.notebook.add(self.tab3, text="Crop Processing & Shipment")
        self.notebook.pack(expand=1, fill="both")

        # Tab 1: Inventory Management
        self.create_inventory_tab()

        # Tab 2: Sales & Supply Data
        self.create_sales_supply_tab()
        
        # Tab 3: Crop Processing & Shipment
        self.create_crop_processing_shipment_tab()
        
    def create_inventory_tab(self):
        # Treeview for inventory
        self.inventory_tree = ttk.Treeview(self.tab1, columns=("Quantity", "Batch", "Purchase Date", "Expiry Date", "UPC"))
        self.inventory_tree.heading("#0", text="Product")
        self.inventory_tree.heading("Quantity", text="Quantity")
        self.inventory_tree.heading("Batch", text="Batch")
        self.inventory_tree.heading("Purchase Date", text="Purchase Date")
        self.inventory_tree.heading("Expiry Date", text="Expiry Date")
        self.inventory_tree.heading("UPC", text="UPC")

        # Inserting inventory data into the treeview
        for product, data in self.inventory.items():
            self.inventory_tree.insert("", "end", text=product, values=(data["quantity"], data["batch"], data["purchase_date"], data["expiry_date"], data["upc"]))
        
        self.inventory_tree.pack(expand=True, fill="both")

        # Frame for actions
        action_frame = tk.Frame(self.tab1)
        action_frame.pack(pady=10)

        # Labels and Entry fields
        self.product_label = tk.Label(action_frame, text="Product:")
        self.product_label.grid(row=0, column=0, padx=5, pady=5)
        self.product_var = tk.StringVar()
        self.product_entry = tk.Entry(action_frame, textvariable=self.product_var)
        self.product_entry.grid(row=0, column=1, padx=5, pady=5)

        self.quantity_label = tk.Label(action_frame, text="Quantity:")
        self.quantity_label.grid(row=0, column=2, padx=5, pady=5)
        self.quantity_var = tk.IntVar()
        self.quantity_entry = tk.Entry(action_frame, textvariable=self.quantity_var)
        self.quantity_entry.grid(row=0, column=3, padx=5, pady=5)

        self.batch_label = tk.Label(action_frame, text="Batch:")
        self.batch_label.grid(row=1, column=0, padx=5, pady=5)
        self.batch_var = tk.StringVar()
        self.batch_entry = tk.Entry(action_frame, textvariable=self.batch_var)
        self.batch_entry.grid(row=1, column=1, padx=5, pady=5)

        self.purchase_date_label = tk.Label(action_frame, text="Purchase Date (YYYY-MM-DD):")
        self.purchase_date_label.grid(row=1, column=2, padx=5, pady=5)
        self.purchase_date_var = tk.StringVar()
        self.purchase_date_entry = tk.Entry(action_frame, textvariable=self.purchase_date_var)
        self.purchase_date_entry.grid(row=1, column=3, padx=5, pady=5)

        self.expiry_date_label = tk.Label(action_frame, text="Expiry Date (YYYY-MM-DD):")
        self.expiry_date_label.grid(row=2, column=0, padx=5, pady=5)
        self.expiry_date_var = tk.StringVar()
        self.expiry_date_entry = tk.Entry(action_frame, textvariable=self.expiry_date_var)
        self.expiry_date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.upc_label = tk.Label(action_frame, text="UPC:")
        self.upc_label.grid(row=2, column=2, padx=5, pady=5)
        self.upc_var = tk.StringVar()
        self.upc_entry = tk.Entry(action_frame, textvariable=self.upc_var)
        self.upc_entry.grid(row=2, column=3, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(action_frame, text="Add to Inventory", command=self.add_to_inventory)
        self.add_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

    def add_to_inventory(self):
        product = self.product_var.get()
        quantity = self.quantity_var.get()
        batch = self.batch_var.get()
        purchase_date = self.purchase_date_var.get()
        expiry_date = self.expiry_date_var.get()
        upc = self.upc_var.get()

        if product and quantity and batch and purchase_date and expiry_date and upc:
            if product not in self.inventory:
                self.inventory[product] = {"quantity": quantity, "batch": batch, "purchase_date": purchase_date, "expiry_date": expiry_date, "upc": upc}
                self.inventory_tree.insert("", "end", text=product, values=(quantity, batch, purchase_date, expiry_date, upc))
            else:
                self.inventory[product]["quantity"] += quantity
                self.inventory_tree.set(product, "Quantity", self.inventory[product]["quantity"])
            messagebox.showinfo("Success", f"{quantity} {product}(s) added to inventory.")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    def create_sales_supply_tab(self):
        # Treeview for sales and supply data
        self.sales_tree = ttk.Treeview(self.tab2, columns=("Quantity Sold", "Price"))
        self.sales_tree.heading("#0", text="Product")
        self.sales_tree.heading("Quantity Sold", text="Quantity Sold")
        self.sales_tree.heading("Price", text="Price")

        # Inserting sales data into the treeview
        for product, data in self.sales.items():
            self.sales_tree.insert("", "end", text=product, values=(data["quantity_sold"], data["price"]))
        
        self.sales_tree.pack(expand=True, fill="both")

        # Frame for actions
        action_frame = tk.Frame(self.tab2)
        action_frame.pack(pady=10)

        # Labels and Entry fields
        self.product_label_sales = tk.Label(action_frame, text="Product:")
        self.product_label_sales.grid(row=0, column=0, padx=5, pady=5)
        self.product_var_sales = tk.StringVar()
        self.product_entry_sales = tk.Entry(action_frame, textvariable=self.product_var_sales)
        self.product_entry_sales.grid(row=0, column=1, padx=5, pady=5)

        self.quantity_sold_label = tk.Label(action_frame, text="Quantity Sold:")
        self.quantity_sold_label.grid(row=0, column=2, padx=5, pady=5)
        self.quantity_sold_var = tk.IntVar()
        self.quantity_sold_entry = tk.Entry(action_frame, textvariable=self.quantity_sold_var)
        self.quantity_sold_entry.grid(row=0, column=3, padx=5, pady=5)

        # Buttons
        self.sell_button = tk.Button(action_frame, text="Sell", command=self.sell_product)
        self.sell_button.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

    def sell_product(self):
        product = self.product_var_sales.get()
        quantity_sold = self.quantity_sold_var.get()

        if product and quantity_sold:
            if product in self.inventory:
                if self.inventory[product]["quantity"] >= quantity_sold:
                    self.sales[product]["quantity_sold"] += quantity_sold
                    self.sales_tree.set(product, "Quantity Sold", self.sales[product]["quantity_sold"])
                    self.inventory[product]["quantity"] -= quantity_sold
                    self.inventory_tree.set(product, "Quantity", self.inventory[product]["quantity"])
                    messagebox.showinfo("Success", f"{quantity_sold} {product}(s) sold.")
                else:
                    messagebox.showerror("Error", f"Not enough {product} in inventory.")
            else:
                messagebox.showerror("Error", f"{product} not found in inventory.")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    def create_crop_processing_shipment_tab(self):
        # Treeview for crop processing and shipment
        self.crop_shipment_tree = ttk.Treeview(self.tab3, columns=("Batch", "Total Quantity", "Shipment Location", "Shipment Date", "Sell by Date", "Price"))
        self.crop_shipment_tree.heading("#0", text="Product")
        self.crop_shipment_tree.heading("Batch", text="Batch")
        self.crop_shipment_tree.heading("Total Quantity", text="Total Quantity")
        self.crop_shipment_tree.heading("Shipment Location", text="Shipment Location")
        self.crop_shipment_tree.heading("Shipment Date", text="Shipment Date")
        self.crop_shipment_tree.heading("Sell by Date", text="Sell by Date")
        self.crop_shipment_tree.heading("Price", text="Price")

        # Inserting crop processing and shipment data into the treeview
        for product, data in self.inventory.items():
            self.crop_shipment_tree.insert("", "end", text=product, values=(data["batch"], data["quantity"], "", "", "", ""))
        
        self.crop_shipment_tree.pack(expand=True, fill="both")

        # Frame for actions
        action_frame = tk.Frame(self.tab3)
        action_frame.pack(pady=10)

        # Labels and Entry fields
        self.product_label_shipment = tk.Label(action_frame, text="Product:")
        self.product_label_shipment.grid(row=0, column=0, padx=5, pady=5)
        self.product_var_shipment = tk.StringVar()
        self.product_entry_shipment = tk.Entry(action_frame, textvariable=self.product_var_shipment)
        self.product_entry_shipment.grid(row=0, column=1, padx=5, pady=5)

        self.batch_label_shipment = tk.Label(action_frame, text="Batch:")
        self.batch_label_shipment.grid(row=0, column=2, padx=5, pady=5)
        self.batch_var_shipment = tk.StringVar()
        self.batch_entry_shipment = tk.Entry(action_frame, textvariable=self.batch_var_shipment)
        self.batch_entry_shipment.grid(row=0, column=3, padx=5, pady=5)

        self.total_quantity_label = tk.Label(action_frame, text="Total Quantity:")
        self.total_quantity_label.grid(row=1, column=0, padx=5, pady=5)
        self.total_quantity_var = tk.IntVar()
        self.total_quantity_entry = tk.Entry(action_frame, textvariable=self.total_quantity_var)
        self.total_quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        self.shipment_location_label = tk.Label(action_frame, text="Shipment Location:")
        self.shipment_location_label.grid(row=1, column=2, padx=5, pady=5)
        self.shipment_location_var = tk.StringVar()
        self.shipment_location_entry = tk.Entry(action_frame, textvariable=self.shipment_location_var)
        self.shipment_location_entry.grid(row=1, column=3, padx=5, pady=5)

        self.shipment_date_label = tk.Label(action_frame, text="Shipment Date (YYYY-MM-DD):")
        self.shipment_date_label.grid(row=2, column=0, padx=5, pady=5)
        self.shipment_date_var = tk.StringVar()
        self.shipment_date_entry = tk.Entry(action_frame, textvariable=self.shipment_date_var)
        self.shipment_date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.sell_by_date_label = tk.Label(action_frame, text="Sell by Date (YYYY-MM-DD):")
        self.sell_by_date_label.grid(row=2, column=2, padx=5, pady=5)
        self.sell_by_date_var = tk.StringVar()
        self.sell_by_date_entry = tk.Entry(action_frame, textvariable=self.sell_by_date_var)
        self.sell_by_date_entry.grid(row=2, column=3, padx=5, pady=5)

        self.price_label = tk.Label(action_frame, text="Price:")
        self.price_label.grid(row=3, column=0, padx=5, pady=5)
        self.price_var = tk.DoubleVar()
        self.price_entry = tk.Entry(action_frame, textvariable=self.price_var)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        self.add_shipment_button = tk.Button(action_frame, text="Add Shipment", command=self.add_shipment)
        self.add_shipment_button.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

    def add_shipment(self):
        product = self.product_var_shipment.get()
        batch = self.batch_var_shipment.get()
        total_quantity = self.total_quantity_var.get()
        shipment_location = self.shipment_location_var.get()
        shipment_date = self.shipment_date_var.get()
        sell_by_date = self.sell_by_date_var.get()
        price = self.price_var.get()

        if product and batch and total_quantity and shipment_location and shipment_date and sell_by_date and price:
            if product in self.inventory:
                self.inventory[product]["quantity"] -= total_quantity
                self.inventory_tree.set(product, "Quantity", self.inventory[product]["quantity"])
                self.crop_shipment_tree.insert("", "end", text=product, values=(batch, total_quantity, shipment_location, shipment_date, sell_by_date, price))
                messagebox.showinfo("Success", f"Shipment added for {product}.")
            else:
                messagebox.showerror("Error", f"{product} not found in inventory.")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")


def main():
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
