# Read input text from file
def read_input_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
# Write the rephrased text to a new file
def write_rephrased_text(rephrased_text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(rephrased_text)