import tkinter as tk
from tkinter import messagebox

def calculate_bill():
    size = size_var.get()
    item = item_var.get()
    pepperoni = pepperoni_var.get()
    cheese = cheese_var.get()

    prices = {
        "Paneer Pizza": 180,
        "Mushroom Pizza": 170,
        "Sweet Corn Pizza": 160,
        "Tandoori Chicken Pizza": 220,
        "Margherita": 150,
        "Farmhouse": 200,
    }

    bill = prices[item]

    # Size
    if size == "M":
        bill += 40
    elif size == "L":
        bill += 70

    # Add-ons
    if pepperoni == "Y":
        bill += 30
    if cheese == "Y":
        bill += 20

    messagebox.showinfo("Total Bill", f"Your total bill is: ₹{bill}")

# Window
root = tk.Tk()
root.title("Indian Pizza Deliveries")
root.geometry("550x650")
root.config(bg="#0F1B3D")   # Dark Blue

# Frame (Card Style)
main_frame = tk.Frame(root, bg="#1E3A8A", bd=3, relief="ridge")
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Title
title = tk.Label(main_frame, text="Indian Pizza Deliveries", 
                 font=("Arial", 22, "bold"), fg="white", bg="#1E3A8A")
title.pack(pady=15)

# Section Title Function
def section(title):
    tk.Label(main_frame, text=title, 
             font=("Arial", 14, "bold"), fg="#FFD700", bg="#1E3A8A").pack(pady=5)

# Pizza Selection
section("Select Your Pizza")

item_var = tk.StringVar(value="Paneer Pizza")
items = [
    "Paneer Pizza",
    "Mushroom Pizza",
    "Sweet Corn Pizza",
    "Tandoori Chicken Pizza",
    "Margherita",
    "Farmhouse",
]

for i in items:
    tk.Radiobutton(main_frame, text=i, variable=item_var, value=i,
                   font=("Arial", 12, "bold"),
                   bg="#1E3A8A", fg="white", selectcolor="#FF0000",
                   activebackground="#1E3A8A").pack(anchor="w", padx=20)

# Size
section("Select Size")

size_var = tk.StringVar(value="S")
sizes = [("Small (S)", "S"), ("Medium (M)", "M"), ("Large (L)", "L")]

for text, val in sizes:
    tk.Radiobutton(main_frame, text=text, variable=size_var, value=val,
                   font=("Arial", 12, "bold"),
                   bg="#1E3A8A", fg="white", selectcolor="#FF0000",
                   activebackground="#1E3A8A").pack(anchor="w", padx=20)

# Pepperoni
section("Add Pepperoni?")

pepperoni_var = tk.StringVar(value="N")
for text, val in [("Yes", "Y"), ("No", "N")]:
    tk.Radiobutton(main_frame, text=text, variable=pepperoni_var, value=val,
                   font=("Arial", 12, "bold"),
                   bg="#1E3A8A", fg="white", selectcolor="#FF0000",
                   activebackground="#1E3A8A").pack(anchor="w", padx=20)

# Cheese
section("Add Extra Cheese?")

cheese_var = tk.StringVar(value="N")
for text, val in [("Yes", "Y"), ("No", "N")]:
    tk.Radiobutton(main_frame, text=text, variable=cheese_var, value=val,
                   font=("Arial", 12, "bold"),
                   bg="#1E3A8A", fg="white", selectcolor="#FF0000",
                   activebackground="#1E3A8A").pack(anchor="w", padx=20)

# Button (modern style)
btn = tk.Button(main_frame, text="CALCULATE BILL", command=calculate_bill,
                font=("Arial", 16, "bold"), bg="#FF0000", fg="white",
                padx=20, pady=10, relief="raised", bd=4)
btn.pack(pady=25)

root.mainloop()
