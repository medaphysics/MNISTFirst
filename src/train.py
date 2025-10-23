# src/train.py
from pathlib import Path
import random
import numpy as np
from typing import Optional, Tuple

import tensorflow as tf
from tensorflow import keras

from .model import build_mnist_cnn
from .data import load_mnist_local_first, ensure_dirs

def set_seed(seed: int = 42):
    np.random.seed(seed)
    random.seed(seed)
    tf.random.set_seed(seed)

def train_and_evaluate(
    data_raw_dir: str = "data/raw",
    results_dir: str = "results",
    epochs: int = 3,
    batch_size: int = 128,
    lr: float = 1e-3,
    validation_split: float = 0.1,
) -> Tuple[keras.Model, float, float]:
    """Train small CNN on MNIST and save artifacts under results/."""
    set_seed(42)

    (x_train, y_train), (x_test, y_test) = load_mnist_local_first(data_raw_dir)

    # dirs
    results = Path(results_dir)
    figs = results / "figures"
    models = results / "models"
    tables = results / "tables"
    ensure_dirs(results, figs, models, tables)

    # model
    model = build_mnist_cnn()
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=lr),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    model.summary()

    # train
    history = model.fit(
        x_train, y_train,
        validation_split=validation_split,
        epochs=epochs,
        batch_size=batch_size,
        verbose=1
    )

    # eval
    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    print(f"[eval] Test accuracy={test_acc:.4f} | loss={test_loss:.4f}")

    # predictions
    y_pred = np.argmax(model.predict(x_test, verbose=0), axis=1)

    # confusion matrix (optional)
    try:
        from sklearn.metrics import confusion_matrix
        import matplotlib.pyplot as plt
        cm = confusion_matrix(y_test, y_pred)
        import matplotlib
        fig = plt.figure(figsize=(6, 5))
        plt.imshow(cm, interpolation="nearest")
        plt.title("MNIST Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("True")
        plt.colorbar()
        plt.tight_layout()
        fig_path = figs / "mnist_confusion.png"
        plt.savefig(fig_path, dpi=150)
        plt.close(fig)
        print(f"[save] confusion matrix -> {fig_path}")
    except Exception as e:
        print(f"[warn] skipping confusion matrix: {e}")

    # save model
    model_path = models / "mnist_cnn.keras"
    model.save(model_path)
    print(f"[save] model -> {model_path}")

    # save small preds table
    try:
        import pandas as pd
        sample_idx = np.arange(min(1000, len(y_test)))
        df = pd.DataFrame({
            "index": sample_idx,
            "true": y_test[sample_idx],
            "pred": y_pred[sample_idx],
        })
        csv_path = tables / "preds.csv"
        df.to_csv(csv_path, index=False)
        print(f"[save] preds -> {csv_path}")
    except Exception as e:
        print(f"[warn] skipping preds csv: {e}")

    return model, test_acc, test_loss
