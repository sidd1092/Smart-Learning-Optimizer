from pdf2docx import Converter
import tkinter as tk
from tkinter import filedialog, messagebox
def pdf_to_word_with_dialog():
    root = tk.Tk()
    root.withdraw()  
    pdf_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        messagebox.showerror("Error", "No PDF file selected!")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
    if not save_path:
        messagebox.showerror("Error", "No save path specified!")
        return
    cv = Converter(pdf_path)
    cv.convert(save_path, start=0, end=None)
    cv.close()
    messagebox.showinfo("Success", "PDF has been converted to Word successfully!")
pdf_to_word_with_dialog()