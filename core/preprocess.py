import re

def preprocess_text(text):
    if isinstance(text, str):
        return re.sub(r'[^a-z0-9\s,]', '', text.lower())
    else:
        return str(text).lower()
