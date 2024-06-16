# Post-process the rephrased text for coherence
def postprocess_text(rephrased_sentences):
    rephrased_text = ' '.join(rephrased_sentences)
    rephrased_text = rephrased_text.replace(' .', '.')
    rephrased_text = rephrased_text.replace(' ,', ',')
    rephrased_text = rephrased_text.replace(' !', '!')
    rephrased_text = rephrased_text.replace(' ?', '?')
    return rephrased_text