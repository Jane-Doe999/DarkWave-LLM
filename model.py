import torch
import torch.nn as nn
import torch.nn.functional as F

class TinyTransformer(nn.Module):
    def __init__(self, vocab_size, embed_size=128, heads=4, layers=4, max_len=128):
        super().__init__()

        self.embed = nn.Embedding(vocab_size, embed_size)
        self.pos = nn.Embedding(max_len, embed_size)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_size,
            nhead=heads,
            dim_feedforward=embed_size * 4,
            batch_first=True
        )

        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=layers)
        self.fc = nn.Linear(embed_size, vocab_size)

    def forward(self, x):
        B, T = x.shape
        pos = torch.arange(T, device=x.device).unsqueeze(0).expand(B, T)

        x = self.embed(x) + self.pos(pos)
        x = self.transformer(x)
        x = self.fc(x)
        return x
