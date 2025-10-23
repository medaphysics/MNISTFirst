# src/data.py
from pathlib import Path
import numpy as np
from tensorflow import keras

def ensure_dirs(*paths):
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)

def load_mnist_local_first(raw_dir: str = "data/raw"):
    """Load MNIST from local cache if exists, else Keras loader (and cache)."""
    raw = Path(raw_dir)
    ensure_dirs(raw)
    local = raw / "mnist.npz"

    if local.exists():
        with np.load(local, allow_pickle=True) as f:
            x_train, y_train = f["x_train"], f["y_train"]
            x_test, y_test = f["x_test"], f["y_test"]
        print(f"[data] Loaded from {local}")
    else:
        print("[data] Local mnist.npz not found; using keras.datasets.mnist (will cache).")
        (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
        np.savez_compressed(local, x_train=x_train, y_train=y_train,
                            x_test=x_test, y_test=y_test)
        print(f"[data] Cached to {local}")

    # normalize & add channel dimension
    x_train = (x_train.astype("float32") / 255.0)[..., np.newaxis]
    x_test  = (x_test.astype("float32")  / 255.0)[..., np.newaxis]
    return (x_train, y_train), (x_test, y_test)
