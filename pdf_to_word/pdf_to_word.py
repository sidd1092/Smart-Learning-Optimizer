import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document
import io
from PIL import Image
import tempfile
import os

import fitz  # PyMuPDF

def convert_pdf_to_word_with_images(pdf_path, word_path):
    document = Document()
    document.add_heading('PDF to Word Conversion', 0)

    pdf = fitz.open(pdf_path)
    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        text = page.get_text("text")
        document.add_paragraph(text)

        # Extract images
        for image_index, img in enumerate(page.get_images(full=True)):
            # get the XREF of the image
            xref = img[0]
            # Extract the image bytes
            base_image = pdf.extract_image(xref)
            image_bytes = base_image["image"]

            # Use BytesIO to handle the image as a file-like object
            image_stream = io.BytesIO(image_bytes)
            image = Image.open(image_stream)

            # Convert color space to RGB if necessary
            if image.mode in ["CMYK", "RGBA"]:
                image = image.convert("RGB")

            # Handle transparency by filling the background with white
            if image.mode == "RGBA":
                filled_image = Image.new("RGB", image.size, (255, 255, 255))
                filled_image.paste(image, mask=image.split()[3])  # 3 is the alpha channel
                image = filled_image

            # Save the image to a temporary file and insert into the document
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_image:
                image.save(tmp_image.name)
                document.add_picture(tmp_image.name)

            # Optionally, remove the temporary file if desired
            os.unlink(tmp_image.name)

    # Save the Word document
    document.save(word_path)

def convert_pdf_to_word_with_dialog():
    root = tk.Tk()
    root.withdraw()  # to hide the small tk window
    pdf_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        messagebox.showerror("Error", "No PDF file selected!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
    if not save_path:
        messagebox.showerror("Error", "No save path specified!")
        return

    convert_pdf_to_word_with_images(pdf_path, save_path)
    messagebox.showinfo("Success", "PDF has been converted to Word successfully!")

if __name__ == "__main__":
    convert_pdf_to_word_with_dialog()