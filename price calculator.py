import tkinter as tk
import customtkinter
from tkinter import messagebox

def calculate_price_per_item_and_compare():
    try:

        total_price1 = total_price_entry1.get().strip()
        number_of_items1 = number_of_items_entry1.get().strip()
        total_price2 = total_price_entry2.get().strip()
        number_of_items2 = number_of_items_entry2.get().strip() 


        if not total_price1 or not number_of_items1 or not total_price2 or not number_of_items2:
            raise ValueError("All fields must be filled.")


        total_price1 = float(total_price1)
        number_of_items1 = int(number_of_items1)
        total_price2 = float(total_price2)
        number_of_items2= int(number_of_items2)


        if number_of_items1 <= 0 or number_of_items2 <= 0:
            raise ValueError("number of items must be greater than zero for both.")
        

        price_per_item1 = total_price1 / number_of_items1
        price_per_item1 = round(price_per_item1,2)


        price_per_item2 = total_price2 / number_of_items2
        price_per_item2 = round(price_per_item2,2)
        

        if price_per_item1 < price_per_item2:
            comparison_result= "\n First set is cheaper! "
        elif price_per_item1 > price_per_item2:
            comparison_result = "\n Second set is cheaper!"
        else: comparison_result = " \n same price! "  
        
        result_label.configure(text=f"\n price per item in set 1: ฿{price_per_item1}"
                            f"\n price per item in set 2: ฿{price_per_item2}"
                            f"{comparison_result}"
                            )
    except ValueError as e:
        messagebox.showerror("error", str(e))

root = customtkinter.CTk()
root.title("PPI Calculator")

customtkinter.CTkLabel(root, text="total price of set 1:").grid(row=0, column=0, padx=10, pady=10)
total_price_entry1 = customtkinter.CTkEntry(root)
total_price_entry1.grid(row=0, column=1, padx=10, pady=10)

customtkinter.CTkLabel(root, text="number of items of set 1:").grid(row=1, column=0, padx=10, pady=10)
number_of_items_entry1 = customtkinter.CTkEntry(root)
number_of_items_entry1.grid(row=1, column=1, padx=10, pady=10)

customtkinter.CTkLabel(root, text="total price of set 2:").grid(row=2, column=0, padx=10, pady=10)
total_price_entry2 = customtkinter.CTkEntry(root)
total_price_entry2.grid(row=2, column=1, padx=10, pady=10)

customtkinter.CTkLabel(root, text="number of items of set 2:").grid(row=3, column=0, padx=10, pady=10)
number_of_items_entry2 = customtkinter.CTkEntry(root)
number_of_items_entry2.grid(row=3, column=1, padx=10, pady=10)

calculate_button = customtkinter.CTkButton(root, text="calculate and compare", command=calculate_price_per_item_and_compare)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = customtkinter.CTkLabel(root, text="")
result_label.grid(row=6, column=0, columnspan=2, pady=13)

root.mainloop()