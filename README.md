# Experiment-4-PyTorch-CUDA

Deep Learning Laboratory – Experiment 4: Project Repository, Git Workflow and PyTorch–CUDA Development Environment Setup.

## Project structure

```
Experiment-4-PyTorch-CUDA/
├── dataset/          # datasets (ignored by Git)
├── models/           # trained weights (*.pt / *.pth ignored by Git)
├── notebooks/        # E4_PyTorch_CUDA_Setup.ipynb – CUDA checks and CPU vs GPU benchmark
├── results/          # generated outputs (ignored by Git)
├── train.py          # small PyTorch training loop on the GPU
├── inference.py      # YOLO11 inference on an image
├── requirements.txt  # pinned dependencies
├── README.md
└── .gitignore
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows  (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu128
```

The CUDA-enabled PyTorch wheel includes the CUDA runtime it needs. You don't have to install the CUDA Toolkit separately, but you do need a recent NVIDIA driver.

## Verify the GPU

```bash
python -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

## Run

```bash
python train.py                      # trains a small MLP on the GPU, saves models/mlp.pt
python inference.py path/to/img.jpg  # YOLO11n detection, writes results/<img>_pred.jpg
```

## Tools

Git, GitHub, Python 3, PyTorch, CUDA, NVIDIA GPU, VS Code / Jupyter.
