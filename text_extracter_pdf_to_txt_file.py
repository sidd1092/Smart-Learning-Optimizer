import tkinter as tk
from tkinter import filedialog, simpledialog
import PyPDF2
import os
import re


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:  # Check if text was extracted
                # Attempt to add newlines after sentences
                page_text = re.sub(r'(?<=[.!?])\s', r'\g<0>\n', page_text)
                text += page_text  # Append the modified text
    return text

def save_text_to_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

def get_unique_filename(output_path):
    if not os.path.exists(output_path):
        return output_path
    else:
        root = tk.Tk()
        root.withdraw()  # Hide the Tkinter root window
        # Ask the user for a new filename until a unique one is provided
        while os.path.exists(output_path):
            base, extension = os.path.splitext(output_path)
            new_filename = simpledialog.askstring("File exists", "File already exists. Enter a extra add-on to name of file:")
            new_filename = new_filename.replace(" ", "_")
            if new_filename:
                output_path = base + "_" + new_filename + extension
            else:
                # User cancelled or closed the dialog; return None to indicate failure
                return None
        return output_path

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Open a file dialog to select the PDF file
pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

# Check if a file was selected
if pdf_path:
    extracted_text = extract_text_from_pdf(pdf_path)
    output_filename ="input.txt"
    output_path = r"C:\Users\ssidd\OneDrive\Desktop\minorProject_try1\input_s" + "\\" + output_filename
    unique_output_path = get_unique_filename(output_path)
    if unique_output_path:
        save_text_to_file(extracted_text, unique_output_path)
        print(f"Extracted text saved to: {unique_output_path}")
    else:
        print("Operation cancelled by the user.")
else:
    print("No PDF file selected.")