"""Minimal GPU training loop: an MLP learns to classify synthetic 2-class data."""
import os
import time

import torch
from torch import nn

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device:", torch.cuda.get_device_name(0) if device.type == "cuda" else "CPU")

torch.manual_seed(0)
X = torch.randn(10_000, 20, device=device)
y = (X[:, :5].sum(dim=1) > 0).long()          # label depends on the first 5 features

model = nn.Sequential(nn.Linear(20, 64), nn.ReLU(), nn.Linear(64, 2)).to(device)
opt = torch.optim.Adam(model.parameters(), lr=1e-2)
loss_fn = nn.CrossEntropyLoss()

start = time.perf_counter()
for epoch in range(1, 51):
    opt.zero_grad()
    loss = loss_fn(model(X), y)                # forward
    loss.backward()                            # backward (gradients)
    opt.step()                                 # update weights
    if epoch % 10 == 0:
        acc = (model(X).argmax(1) == y).float().mean().item()
        print(f"epoch {epoch:2d}  loss {loss.item():.4f}  accuracy {acc:.3f}")
if device.type == "cuda":
    torch.cuda.synchronize()
print(f"Training time: {time.perf_counter() - start:.2f} s")

os.makedirs("models", exist_ok=True)
torch.save(model.state_dict(), "models/mlp.pt")
print("Saved models/mlp.pt")
