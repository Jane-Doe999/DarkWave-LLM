# saver.py
# Helper to save model weights

import torch

def save_weights(model, path):
    torch.save(model.state_dict(), path)
    print(f"Weights saved to {path}")
