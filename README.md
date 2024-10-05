# CSV Cleaner

## Overview

CSV Cleaner is a Python-based tool designed to help users clean and preprocess CSV files. It offers several operations, including removing null values, handling 'NA' values, removing duplicate rows, cleaning special characters, and managing outliers. The tool features a user-friendly GUI built with Tkinter, allowing users to easily select operations and save the cleaned data.

## Features

- Remove null values from the dataset.
- Handle 'NA' values efficiently.
- Remove duplicate rows.
- Clean special characters from both column names and data entries.
- Handle outliers based on IQR (Interquartile Range).
- Simple and intuitive GUI for user interaction.

## Requirements

- Python 3.x
- Pandas
- NumPy
- Tkinter
- Regular expressions (re)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ohnogaurav/csvcleaner.git
2. Navigate to the project directory:
   ```bash
   cd csvcleaner
3. Install the required packages (if not already installed):
   ````bash
   pip install pandas numpy
## Usage

1. Run the CSV Cleaner script:
   ````bash
   python csv_cleaner.py
2. The program will prompt you to select a CSV file.

3. Based on the contents of the selected file, it will enable relevant cleaning operations.

4. Choose the operations you wish to perform and specify a location to save the cleaned file.


## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

