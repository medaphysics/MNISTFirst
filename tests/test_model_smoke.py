# tests/test_model_smoke.py
import numpy as np
import tensorflow as tf

from src.model import build_mnist_cnn

def test_build_and_forward():
    model = build_mnist_cnn()
    # dummy batch (8 samples)
    x = np.random.rand(8, 28, 28, 1).astype("float32")
    y = model(x, training=False).numpy()

    # shape checks
    assert y.shape == (8, 10), "Output shape must be (batch, num_classes=10)"

    # softmax sanity: rows sum ~ 1
    row_sums = y.sum(axis=1)
    assert np.allclose(row_sums, 1.0, atol=1e-5), "Softmax rows must sum to 1"

    # no NaNs / infs
    assert np.isfinite(y).all(), "Output must be finite"
