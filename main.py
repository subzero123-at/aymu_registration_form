# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
from tkinter import ttk


def submit_form():
    # Get the values from the form fields
    name_entry.get()
    class_var.get()
    email_entry.get()
    gender_var.get()
    country_var.get()

    # Clear the form fields after submission
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    # Create a new window for the confirmation message
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Confirmation")

    # Add a label with the confirmation message
    confirmation_label = tk.Label(confirmation_window, text="Your response has been submitted.", font=("Helvetica", 16))
    confirmation_label.pack(padx=20, pady=50)


root = tk.Tk()
root.title("Registration Form")

# Create the registration form
registration_frame = ttk.Frame(root, padding=20)
registration_frame.pack()

# Name field
name_label = ttk.Label(registration_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(registration_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Class dropdown
class_var = tk.StringVar()
class_label = ttk.Label(registration_frame, text="Class:")
class_label.grid(row=1, column=0, padx=5, pady=5)
class_dropdown = ttk.Combobox(
    registration_frame, textvariable=class_var,
    values=["CSE A", "CSE B", "CSM", "CSD", "MECH", "CIVIL"])

class_dropdown.grid(row=1, column=1, padx=5, pady=5)

# Email field
email_label = ttk.Label(registration_frame, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry = ttk.Entry(registration_frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)

# Gender radio buttons
gender_var = tk.StringVar()
gender_label = ttk.Label(registration_frame, text="Gender:")
gender_label.grid(row=3, column=0, padx=5, pady=5)
male_radio = ttk.Radiobutton(registration_frame, text="Male", variable=gender_var, value="Male")
female_radio = ttk.Radiobutton(registration_frame, text="Female", variable=gender_var, value="Female")
male_radio.grid(row=3, column=1, padx=5, pady=5)
female_radio.grid(row=3, column=2, padx=5, pady=5)

# Country dropdown
country_var = tk.StringVar()
country_label = ttk.Label(registration_frame, text="Country:")
country_label.grid(row=4, column=0, padx=5, pady=5)
country_dropdown = ttk.Combobox(registration_frame, textvariable=country_var,
                                values=["Canada", "India", "UK", "Japan", "Iceland", "South Africa"])
country_dropdown.grid(row=4, column=1, padx=5, pady=5)

# Submit button
submit_button = ttk.Button(registration_frame, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
