# architecture.py
# Minimal placeholder transformer for DarkWave-LLM

import torch
import torch.nn as nn

class SimpleLLM(nn.Module):
    def __init__(self, vocab_size=10000, embed_dim=128, hidden_dim=256):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.rnn = nn.GRU(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)
    
    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.rnn(x)
        out = self.fc(out)
        return out
