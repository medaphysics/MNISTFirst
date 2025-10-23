import numpy as np, tensorflow as tf, pathlib
m = tf.keras.models.load_model("results/models/mnist_cnn.keras")
x = np.random.rand(1,28,28,1).astype("float32")
y = m(x, training=False).numpy()
print("probs:", y.round(4), "argmax:", y.argmax())