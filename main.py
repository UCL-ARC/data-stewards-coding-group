import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movies_df = pd.read_csv('Movies_dataset.csv')


# describing the data set
print(movies_df.head())
print(movies_df.describe())
