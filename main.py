import pandas as pd

# read the csv file
df = pd.read_csv('Movies_dataset.csv',
                 dayfirst=True,
                 parse_dates=['release_date'],
                 )

# print the first 5 rows of the dataframe
print(df.head())

# print a description of the dataframe
print(df.describe())

# print information about the dataframe
print(df.info())

# print a list of the cloumns in the dataframe
print(df.columns)


