# src/main.py
import argparse

from .train import train_and_evaluate

def build_parser():
    p = argparse.ArgumentParser(description="MNIST Hello World (TensorFlow/Keras)")
    p.add_argument("--data-raw-dir", default="data/raw", help="raw dataset dir (mnist.npz cache)")
    p.add_argument("--results-dir",  default="results",   help="artifacts root dir")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--batch-size", type=int, default=128)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--val-split", type=float, default=0.1)
    return p

def main():
    args = build_parser().parse_args()
    train_and_evaluate(
        data_raw_dir=args.data_raw_dir,
        results_dir=args.results_dir,
        epochs=args.epochs,
        batch_size=args.batch_size,
        lr=args.lr,
        validation_split=args.val_split,
    )

if __name__ == "__main__":
    main()
