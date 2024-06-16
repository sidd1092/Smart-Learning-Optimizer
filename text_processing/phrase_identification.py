# Identify complex phrases
def identify_complex_phrases(words):
    complex_phrases = []
    for word in words:
        if len(word) > 10:
            complex_phrases.append(word)
    return complex_phrases