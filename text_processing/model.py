import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer

# Assuming this is a simplified version of generate_simpler_alternatives
def generate_simpler_alternatives(complex_phrases):
    simpler_alternatives = []
    for phrase in complex_phrases:
        try:
            # Simulate generating a simpler alternative (this logic will vary)
            simpler_alternative = "simplified_" + phrase  # Placeholder logic
            simpler_alternatives.append(simpler_alternative)
        except Exception as e:
            print(f"Error processing phrase '{phrase}': {e}")
            simpler_alternatives.append(phrase)  # Fallback to the original phrase
    return simpler_alternatives
# Replace complex phrases with simpler ones
def replace_complex_phrases(sentences, complex_phrases, simple_alternatives):
    rephrased_sentences = []
    for sentence in sentences:
        for complex_phrase, simple_alternative in zip(complex_phrases, simple_alternatives):
            sentence = sentence.replace(complex_phrase, simple_alternative)
        rephrased_sentences.append(sentence)
    return rephrased_sentences