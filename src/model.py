# src/model.py
from tensorflow import keras
from tensorflow.keras import layers

def build_mnist_cnn(num_classes: int = 10, input_shape=(28, 28, 1)) -> keras.Model:
    """Tiny CNN for MNIST. Returns an UNCOMPILED model."""
    model = keras.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(16, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax'),
    ])
    return model
