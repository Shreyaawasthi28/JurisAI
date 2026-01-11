import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    doc = nlp(text.lower())
    cleaned_text = " ".join(
        token.text for token in doc
        if not token.is_stop and token.is_alpha
    )
    return cleaned_text
