import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow
from tensorflow import keras
import torch
import sklearn

# NumPy Operations
array = np.array([10, 20, 30, 40, 50])
print("NumPy Array: ", array)
print("Mean:", np.mean(array))

# Pandas DataFrame
data = {"Name": ["A", "B", "C"], "Marks": [85, 90, 78]}
df = pd.DataFrame(data)
print("In Pandas DataFrame:")
print(df)

# Matplotlib Plot
plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
plt.title("Simple Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Seaborn Plot
sns.scatterplot(x=[1, 2, 3, 4], y=[10, 20, 30, 40])
plt.title("Seaborn Scatter Plot")
plt.show()

# Library Versions & Deep Learning Models
print("In scikit-learn Version: ", sklearn.__version__)
print("In TensorFlow Version:", tensorflow.__version__)
model = keras.Sequential()
print("Keras model created successfully.")
tensor = torch.tensor([1, 2, 3, 4])
print("PyTorch Tensor: ", tensor)
print("PyTorch Version : ", torch.__version__)
