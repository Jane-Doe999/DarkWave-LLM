import torch
from model import TinyTransformer
from tqdm import tqdm

# --- Load dataset ---
with open("dataset.txt", "r", encoding="utf-8") as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)

stoi = {ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)}

def encode(s):
    return [stoi[c] for c in s]

def decode(l):
    return "".join([itos[i] for i in l])

data = torch.tensor(encode(text), dtype=torch.long)

# --- Model ---
model = TinyTransformer(vocab_size)
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)
loss_fn = torch.nn.CrossEntropyLoss()

# --- Training settings ---
block_size = 128
batch_size = 32
epochs = 3

def get_batch():
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x, y

print("Training started...")

for epoch in range(epochs):
    for step in tqdm(range(2000)):
        xb, yb = get_batch()
        logits = model(xb)

        loss = loss_fn(logits.view(-1, vocab_size), yb.view(-1))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch} loss:", loss.item())

torch.save({
    "model": model.state_dict(),
    "stoi": stoi,
    "itos": itos
}, "weights.pt")

print("Training complete. Weights saved.")
