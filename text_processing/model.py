import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer

# Use ensemble of ML models to generate simpler alternatives
def generate_simpler_alternatives(complex_phrases):
    data = pd.read_csv('data/complex_phrases.csv')
    X = data['Complex Phrase']
    y = data['Simple Phrase']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = make_pipeline(CountVectorizer(), RandomForestClassifier())
    model.fit(X_train, y_train)
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