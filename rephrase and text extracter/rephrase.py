from transformers import pipeline
import os
import tensorflow as tf

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0 = all messages are logged, 1 = INFO messages are not printed, 2 = INFO and WARNING messages are not printed, 3 = INFO, WARNING, and ERROR messages are not printed

# Ensure that deprecation warnings are not shown
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
# Initialize the paraphrase generator
paraphrase_generator = pipeline("text2text-generation", model="t5-base")

# Read input text file
input_file_path = r'C:\Users\ssidd\OneDrive\Desktop\minorProject_try1\input_s\input.txt'
output_file_path = r'C:\Users\ssidd\OneDrive\Desktop\minorProject_try1\Output_s\aaa_.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Generate paraphrases
paraphrased_text = paraphrase_generator(input_text, max_length=512, num_return_sequences=1)[0]['generated_text']

# Write the paraphrased text to an output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(paraphrased_text)

print("Paraphrasing complete. Check the output file for results.")

