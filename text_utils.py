# text_utils.py
# Minimal tokenizer example

def tokenize(text):
    return text.split()

def detokenize(tokens):
    return " ".join(tokens)
