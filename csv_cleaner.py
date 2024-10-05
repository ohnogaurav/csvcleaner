import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import re

def clean_special_characters(string):
    """Remove special characters from a string."""
    return re.sub(r'[^\w\s]', '', string)

def clean_csv(input_file, output_file, operations):
    # Read the CSV file
    df = pd.read_csv(input_file)

    log_messages = []

    # 1. Print total columns and rows
    log_messages.append(f"Total columns: {df.shape[1]}")
    log_messages.append(f"Total rows: {df.shape[0]}")

    # --- Cleaning Process based on selected operations ---
    if 'remove_null' in operations:
        initial_row_count = df.shape[0]
        df.dropna(inplace=True)
        log_messages.append(f"Removed {initial_row_count - df.shape[0]} rows due to null values.")

    if 'remove_na' in operations:
        initial_row_count = df.shape[0]
        df.replace('NA', np.nan, inplace=True)
        df.dropna(inplace=True)
        log_messages.append(f"Removed {initial_row_count - df.shape[0]} rows due to 'NA' values.")

    if 'remove_duplicates' in operations:
        initial_row_count = df.shape[0]
        df.drop_duplicates(inplace=True)
        log_messages.append(f"Removed {initial_row_count - df.shape[0]} duplicate rows.")

    # Handle cleaning special characters
    if 'clean_special_chars' in operations:
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].apply(clean_special_characters)
            log_messages.append(f"Cleaned special characters in column '{col}'.")

        # Clean column names
        df.columns = [clean_special_characters(col) for col in df.columns]

    # Handle outliers
    if 'handle_outliers' in operations:
        for col in df.select_dtypes(include=[np.number]).columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outlier_count = df[(df[col] < lower_bound) | (df[col] > upper_bound)].shape[0]
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)].copy()
            log_messages.append(f"Removed {outlier_count} outlier rows from column '{col}'.")

    # Save the cleaned CSV file
    df.to_csv(output_file, index=False)

    # Show log messages
    log_messages.append(f"Cleaned CSV saved to {output_file}")
    log_messages.append(f"New number of rows: {df.shape[0]}")
    log_messages.append(f"New number of columns: {df.shape[1]}")
    
    # Display the logs in a message box
    messagebox.showinfo("Cleaning Log", "\n".join(log_messages))

def open_file_dialog():
    """Open a file dialog to select a CSV file."""
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Select a CSV File"
    )
    return file_path

def save_file_dialog():
    """Open a file dialog to save the cleaned CSV file."""
    output_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save Cleaned CSV File"
    )
    return output_path

def run_cleaning():
    """Execute the cleaning based on user-selected operations."""
    input_file = open_file_dialog()
    if not input_file:
        return

    output_file = save_file_dialog()
    if not output_file:
        return

    operations = []
    if remove_null_var.get():
        operations.append('remove_null')
    if remove_na_var.get():
        operations.append('remove_na')
    if remove_duplicates_var.get():
        operations.append('remove_duplicates')
    if clean_special_chars_var.get():
        operations.append('clean_special_chars')
    if handle_outliers_var.get():
        operations.append('handle_outliers')

    if operations:
        clean_csv(input_file, output_file, operations)
    else:
        messagebox.showwarning("Warning", "No operation selected. Please choose at least one operation.")

# Tkinter GUI setup
root = tk.Tk()
root.title("CSV Cleaning Tool")

# Checkbox variables
remove_null_var = tk.BooleanVar()
remove_na_var = tk.BooleanVar()
remove_duplicates_var = tk.BooleanVar()
clean_special_chars_var = tk.BooleanVar()
handle_outliers_var = tk.BooleanVar()

# Create checkboxes for operations
tk.Checkbutton(root, text="Remove Null Values", variable=remove_null_var).pack()
tk.Checkbutton(root, text="Remove 'NA' Values", variable=remove_na_var).pack()
tk.Checkbutton(root, text="Remove Duplicate Rows", variable=remove_duplicates_var).pack()
tk.Checkbutton(root, text="Clean Special Characters", variable=clean_special_chars_var).pack()
tk.Checkbutton(root, text="Handle Outliers", variable=handle_outliers_var).pack()

# Run button
tk.Button(root, text="Run Cleaning", command=run_cleaning).pack()

root.mainloop()
