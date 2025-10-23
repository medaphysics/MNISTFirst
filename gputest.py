import tensorflow as tf, pprint, sys
print("TF:", tf.__version__)
print("GPUs:", tf.config.list_physical_devices("GPU"))

try: info = tf.sysconfig.get_build_info()
except Exception as e: sys.exit(0)
pprint.pp(info)
