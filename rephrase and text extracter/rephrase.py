from transformers import pipeline
import tkinter as tk
from tkinter import filedialog

# Initialize the paraphrase generator
paraphrase_generator = pipeline("text2text-generation", model="t5-base")

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Prompt the user to select the input file
input_file_path = filedialog.askopenfilename(title="Select Input File")

# Prompt the user to select the output file
output_file_path = filedialog.asksaveasfilename(title="Select Output File")

# Check if the user canceled the file selection
if not input_file_path or not output_file_path:
    print("File selection canceled.")
    exit()


with open(input_file_path, 'r') as file:
    input_text = file.read()

# Generate paraphrases
paraphrased_text = paraphrase_generator(input_text, max_length=512, num_return_sequences=1)[0]['generated_text']

# Write the paraphrased text to an output file
with open(output_file_path, 'w') as file:
    file.write(paraphrased_text)

print("Paraphrasing complete. Check the output file for results.")
