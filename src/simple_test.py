import numpy as np, tensorflow as tf
from tensorflow import keras

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

model = tf.keras.models.load_model("results/models/mnist_cnn.keras")
(_, _), (x_test, y_test) = keras.datasets.mnist.load_data()

x = (x_test[0].astype("float32")/255.0)[None, ..., None]  # (1,28,28,1)

probs = model(x, training=False).numpy()[0]

print("true:", y_test[0], "pred:", probs.argmax(), "sum:", probs.sum())
