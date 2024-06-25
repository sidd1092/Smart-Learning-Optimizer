import os
from pdf2docx import Converter
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading

class PDFtoWordConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF to Word Converter")
        
        # Center the window on the screen
        window_width = 400
        window_height = 200
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.master.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        
        self.master.resizable(False, False)

        # Styling
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10), borderwidth='1')
        self.style.configure('TLabel', font=('Arial', 10), background='light grey', relief='flat')
        self.style.configure('TFrame', background='light grey')

        # Layout
        self.frame = ttk.Frame(self.master, padding="10", style='TFrame')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.select_button = ttk.Button(self.frame, text="Select PDF", command=self.select_pdf)
        self.select_button.pack(side=tk.TOP, fill=tk.X, pady=(10, 5), padx=10)

        self.status_label = ttk.Label(self.frame, text="Select a PDF file to start the conversion.", wraplength=380, style='TLabel')
        self.status_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(5, 10), padx=10)

        # Progress Bar
        self.progress = ttk.Progressbar(self.frame, orient=tk.HORIZONTAL, length=100, mode='indeterminate')

    def select_pdf(self):
        self.pdf_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
        if self.pdf_path:
            self.save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Document", "*.docx")], initialfile=os.path.splitext(os.path.basename(self.pdf_path))[0] + "_converted_to_word")
            if self.save_path:
                self.status_label.config(text="PDF selected. Converting...")
                self.select_button.pack_forget()  # Hide select button
                self.progress.pack(side=tk.TOP, fill=tk.X, pady=(10, 5), padx=10)  # Show progress bar
                threading.Thread(target=self.convert_to_word).start()  # Start conversion in a separate thread
            else:
                self.status_label.config(text="Conversion cancelled. Please select a PDF file again.")
        else:
            self.status_label.config(text="No PDF file selected. Please select a file.")

    def convert_to_word(self):
        if not self.pdf_path:
            messagebox.showerror("Error", "No PDF file selected!")
            return
        try:
            self.progress.start(10)  # Start progress bar animation
            cv = Converter(self.pdf_path)
            cv.convert(self.save_path, start=0, end=None)
            cv.close()
            self.progress.stop()  # Stop progress bar animation
            self.progress.pack_forget()  # Hide progress bar
            messagebox.showinfo("Success", "PDF has been converted to Word successfully!")
            self.ask_for_more_conversions()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert PDF to Word: {e}")
            self.status_label.config(text="Conversion failed. Try again.")

    def ask_for_more_conversions(self):
        answer = messagebox.askyesno("Continue", "Do you want to convert another PDF?")
        if answer:
            self.status_label.config(text="Select a PDF file to start the conversion.")
            self.pdf_path = ""
            self.save_path = ""
            self.select_button.pack(side=tk.TOP, fill=tk.X, pady=(10, 5), padx=10)  # Show select button again
            self.progress.pack_forget()  # Ensure progress bar is hidden
        else:
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFtoWordConverterApp(root)
    root.mainloop()