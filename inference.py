"""YOLO11n object detection on one image: python inference.py path/to/image.jpg"""
import os
import sys

import torch
from ultralytics import YOLO
from ultralytics.utils import ASSETS

image = sys.argv[1] if len(sys.argv) > 1 else str(ASSETS / "bus.jpg")
if not os.path.exists(image):
    sys.exit(f"Image not found: {image}")

device = 0 if torch.cuda.is_available() else "cpu"
model = YOLO("yolo11n.pt")
result = model.predict(image, conf=0.25, iou=0.45, device=device, verbose=False)[0]

for box in result.boxes:
    name = model.names[int(box.cls[0])]
    print(f"{name:12s} {float(box.conf[0]):.3f}  {[round(v, 1) for v in box.xyxy[0].tolist()]}")
print(f"{len(result.boxes)} objects | speed (ms): {result.speed}")

os.makedirs("results", exist_ok=True)
out = os.path.join("results", os.path.splitext(os.path.basename(image))[0] + "_pred.jpg")
result.save(filename=out)
print("Saved", out)
