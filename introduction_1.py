# -*- coding: utf-8 -*-
"""Introduction_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uZPJ0uQnCWmRyAWaKWdTbUZcC3nKf4Bu
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf
print(tf.version)

#create tensor t as array of zeros of dimension [5,5,5,5]
t = tf.zeros([5,5,5,5])
#reshape the tensor t to shape(5,125)
t = tf.reshape(t, [5, -1])
print(t)