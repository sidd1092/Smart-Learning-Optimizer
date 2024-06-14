# 1. Read input text from file
# 2. Preprocess the text
#    a. Tokenize text
#    b. Remove stop words
#    c. Apply stemming
# 3. For each sentence in the text:
#    a. Identify complex phrases
#    b. Use ensemble of ML models to generate simpler alternatives
#    c. Replace complex phrases with simpler ones
# 4. Post-process the rephrased text for coherence
# 5. Write the rephrased text to a new file


import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import re
import os
import sys
import string
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import IsolationForest
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.linear_model import LogisticRegression

# Read input text from file
def read_input_text(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    return text

# Preprocess the text
def preprocess_text(text):
    # Tokenize text
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    
    # Apply stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    return sentences, words

# Identify complex phrases
def identify_complex_phrases(words):
    complex_phrases = []
    for word in words:
        if len(word) > 10:
            complex_phrases.append(word)
    return complex_phrases

# Use ensemble of ML models to generate simpler alternatives
def generate_simpler_alternatives(complex_phrases):
    # Load the dataset
    data = pd.read_csv('data/complex_phrases.csv')
    
    # Split the dataset into training and testing sets
    X = data['Complex Phrase']
    y = data['Simple Phrase']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create a pipeline
    model = make_pipeline(CountVectorizer(), RandomForestClassifier())
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Predict the simple alternatives
    simple_alternatives = model.predict(complex_phrases)
    
    return simple_alternatives

# Replace complex phrases with simpler ones
def replace_complex_phrases(sentences, complex_phrases, simple_alternatives):
    rephrased_sentences = []
    for sentence in sentences:
        for complex_phrase, simple_alternative in zip(complex_phrases, simple_alternatives):
            sentence = sentence.replace(complex_phrase, simple_alternative)
        rephrased_sentences.append(sentence)
    return rephrased_sentences

# Post-process the rephrased text for coherence
def postprocess_text(rephrased_sentences):
    rephrased_text = ' '.join(rephrased_sentences)
    rephrased_text = rephrased_text.replace(' .', '.')
    rephrased_text = rephrased_text.replace(' ,', ',')
    rephrased_text = rephrased_text.replace(' !', '!')
    rephrased_text = rephrased_text.replace(' ?', '?')
    return rephrased_text

# Write the rephrased text to a new file
def write_rephrased_text(rephrased_text, output_file):
    with open(output_file, 'w') as file:
        file.write(rephrased_text)

# Main function
def main(input_file, output_file):
    text = read_input_text(input_file)
    sentences, words = preprocess_text(text)
    complex_phrases = identify_complex_phrases(words)
    simple_alternatives = generate_simpler_alternatives(complex_phrases)
    rephrased_sentences = replace_complex_phrases(sentences, complex_phrases, simple_alternatives)
    rephrased_text = postprocess_text(rephrased_sentences)
    write_rephrased_text(rephrased_text, output_file)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)

# Run the script