


import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data.csv')  # adjust filename to match your download
df.head()

# Keep only OCEAN columns
ocean_cols = ['O', 'C', 'E', 'A', 'N']
df_ocean = df[ocean_cols].dropna()

# Normalize to 0-1 or standardize — important before K-means
scaler = StandardScaler()
X = scaler.fit_transform(df_ocean)