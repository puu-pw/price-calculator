# price-calculator
Price Per Item (PPI) Calculator
This is a simple Price Per Item (PPI) Calculator created using Python's tkinter and customtkinter libraries. The application compares the price per item between two sets and informs you which set is cheaper, or if both are the same price.

Features
User-friendly interface for entering prices and item quantities.
Error handling for invalid input (e.g., empty fields, non-numeric values, zero or negative item quantities).
Calculation and display of price per item for each set.
Comparison result indicating which set is cheaper.
Prerequisites
Before you begin, ensure you have the following installed on your machine:

Python 3.x
tkinter (comes pre-installed with Python)
customtkinter (install via pip)
Installation
Clone this repository or download the .py file.

Install the required Python package customtkinter:

bash
Copy code
pip install customtkinter
Run the PPI_Calculator.py file:

bash
Copy code
python PPI_Calculator.py
Usage
Input the total price and number of items for Set 1:
In the first two fields, enter the total price and the number of items for the first set.
Input the total price and number of items for Set 2:
In the next two fields, enter the total price and the number of items for the second set.
Calculate and Compare:
Click the "Calculate and Compare" button.
The result will display the price per item for both sets and indicate which set is cheaper or if they are the same price.
Error Handling
The application checks for:

Empty fields: All fields must be filled.
Valid numeric input: Prices must be numbers, and the number of items must be positive integers.
Number of items: The number of items in each set must be greater than zero.
If any of these checks fail, an error message will be displayed.

Example
Let's say you have:

Set 1: $100 total price for 10 items.
Set 2: $120 total price for 12 items.
After clicking the "Calculate and Compare" button, the app will show:

Price per item in Set 1: ฿10.0
Price per item in Set 2: ฿10.0
Result: "Same price!"
License
This project is open-source and available under the MIT License.

Contributions
Contributions, issues, and feature requests are welcome!
