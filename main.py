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

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)