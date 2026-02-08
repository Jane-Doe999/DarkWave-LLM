import torch
from model import TinyTransformer

checkpoint = torch.load("weights.pt")

stoi = checkpoint["stoi"]
itos = checkpoint["itos"]

def encode(s):
    return [stoi.get(c,0) for c in s]

def decode(l):
    return "".join([itos[i] for i in l])

model = TinyTransformer(len(stoi))
model.load_state_dict(checkpoint["model"])
model.eval()

def generate(prompt, max_new_tokens=200):
    x = torch.tensor([encode(prompt)], dtype=torch.long)

    for _ in range(max_new_tokens):
        logits = model(x)
        next_token = torch.argmax(logits[0, -1]).unsqueeze(0).unsqueeze(0)
        x = torch.cat([x, next_token], dim=1)

    return decode(x[0].tolist())

while True:
    user = input("You: ")
    prompt = f"User: {user}\nAI:"
    print(generate(prompt))
