import pandas as pd

# read the csv file
df = pd.read_csv('Movies_dataset.csv')

# print the first 5 rows of the dataframe
print(df.head())

# print a description of the dataframe
print(df.describe())

# print a list of the cloumns in the dataframe
print(df.columns)


