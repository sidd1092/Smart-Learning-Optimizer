# Read input text from file
def read_input_text(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    return text

# Write the rephrased text to a new file
def write_rephrased_text(rephrased_text, output_file):
    with open(output_file, 'w') as file:
        file.write(rephrased_text)