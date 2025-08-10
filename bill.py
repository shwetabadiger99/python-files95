import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Food Billing System")

# Frames
order_frame = ttk.Frame(root)
order_frame.pack(padx=10, pady=10, fill="both", expand=True)

billing_frame = ttk.Frame(root)
billing_frame.pack(padx=10, pady=10, fill="x")

# Data
order_items = []
total_amount = 0

# Functions
def add_item(item, price):
    order_items.append((item, price))
    update_order_list()
    update_total_amount()

def remove_selected_item():
    selection = order_list_box.curselection()
    if selection:
        index = selection[0]
        order_items.pop(index)
        update_order_list()
        update_total_amount()

def update_order_list():
    order_list_box.delete(0, tk.END)
    for item, price in order_items:
        order_list_box.insert(tk.END, f"{item}: ${price:.2f}")

def update_total_amount():
    total = sum(price for _, price in order_items)
    total_amount_label.config(text=f"Total: ${total:.2f}")

# Menu
menu_items = {
    "Pizza": 10.00,
    "Burger": 8.00,
    "Fries": 5.00,
    "Salad": 7.00,
    "Soda": 2.00,
}

for item, price in menu_items.items():
    button = ttk.Button(order_frame, text=item, command=lambda i=item, p=price: add_item(i, p))
    button.pack(side=tk.LEFT, padx=5, pady=5)

# Order list
order_list_box = tk.Listbox(billing_frame)
order_list_box.pack(side=tk.LEFT, fill="both", expand=True)

# Remove button
remove_button = ttk.Button(billing_frame, text="Remove Selected", command=remove_selected_item)
remove_button.pack(side=tk.LEFT, padx=5, pady=5)

# Total label
total_amount_label = ttk.Label(billing_frame, text="Total: $0.00")
total_amount_label.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()
