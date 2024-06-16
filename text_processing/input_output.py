# Read input text from file
def read_input_text(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    return text

# Write the rephrased text to a new file
def write_rephrased_text(rephrased_text, output_file):
    output_path = r'C:\Users\ssidd\OneDrive\Desktop\minorProject_try1\Output_s'
    with open(output_path, 'w') as file:
        file.write(rephrased_text)