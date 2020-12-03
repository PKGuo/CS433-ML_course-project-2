# Load packages

import sys
import time

# Maths things
import numpy as np

# Plotting
import matplotlib.pyplot as plt

# Algorithm
# Algorithm
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import Ridge
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from functools import partial


import seaborn as sns
import umap

data = np.load('./data/regression_data.npy')
target = np.loadtxt('./data/target_values.txt')
X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size = 100, random_state = 7)

mapper = umap.UMAP(n_neighbors=20,min_dist=0.5,n_components=3).fit(X_train, np.array(Y_train))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u = mapper.embedding_
ax.scatter(u[:,0],u[:,1],u[:,2], c=Y_train,s=10,cmap='Spectral', alpha=1.0)
plt.show()
