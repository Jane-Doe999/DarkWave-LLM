# loader.py
# Helper to load dataset or weights

import torch

def load_weights(model, path):
    model.load_state_dict(torch.load(path))
    print(f"Weights loaded from {path}")
