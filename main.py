from text_processing.input_output import read_input_text, write_rephrased_text
from text_processing.preprocessing import preprocess_text
from text_processing.phrase_identification import identify_complex_phrases
from text_processing.model import generate_simpler_alternatives, replace_complex_phrases
from text_processing.postprocessing import postprocess_text
import sys

def main(input_file, output_file):
    text = read_input_text(input_file)
    sentences, words = preprocess_text(text)
    complex_phrases = identify_complex_phrases(words)
    simple_alternatives = generate_simpler_alternatives(complex_phrases)
    rephrased_sentences = replace_complex_phrases(sentences, complex_phrases, simple_alternatives)
    rephrased_text = postprocess_text(rephrased_sentences)
    write_rephrased_text(rephrased_text, output_file)

def get_file_paths():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    input_file = askopenfilename(title="Select input file", filetypes=[("Text files", "*.txt")])  # show an "Open" dialog box and return the path to the selected file
    output_file = asksaveasfilename(title="Save output file as", defaultextension=".txt", filetypes=[("Text files", "*.txt")])  # show a "Save as" dialog box and return the path to the save location
    return input_file, output_file

if __name__ == '__main__':
    if len(sys.argv) < 3:
        input_file, output_file = get_file_paths()
        if not input_file or not output_file:  # Check if the user cancelled either dialog
            print("File selection cancelled.")
            sys.exit(1)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    main(input_file, output_file)