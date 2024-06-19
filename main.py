import tkinter as tk
from tkinter import filedialog
from text_processing.input_output import read_input_text, write_rephrased_text
from text_processing.preprocessing import preprocess_text
from text_processing.phrase_identification import identify_complex_phrases
from text_processing.model import generate_simpler_alternatives, replace_complex_phrases
from text_processing.postprocessing import postprocess_text

def main():
    # Initialize Tkinter root
    root = tk.Tk()
    root.withdraw()   # Hide the main window

    # Open file dialog for selecting the input file
    input_file = filedialog.askopenfilename(
        title="Select Input File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if not input_file:  # If no file is selected
        return

    # Open file dialog for specifying the output file
    output_file = filedialog.asksaveasfilename(
        title="Save Output File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
        defaultextension=".txt"
    )
    if not output_file:  # If no file is specified
        return

    try:
        # Processing
        text = read_input_text(input_file)
        sentences, words = preprocess_text(text)
        complex_phrases = identify_complex_phrases(words)
        simple_alternatives = generate_simpler_alternatives(complex_phrases)
        rephrased_sentences = replace_complex_phrases(sentences, complex_phrases, simple_alternatives)
        rephrased_text = postprocess_text(rephrased_sentences)
        write_rephrased_text(rephrased_text, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Processing completed.")

if __name__ == '__main__':
    main()