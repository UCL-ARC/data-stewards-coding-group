#%% imports
 import pandas as pd
 import datetime as dt


#%% dataframe
df = pd.read_csv('Movies_dataset.csv', dayfirst=True, parse_dates=['release_date'])

#%% headers
print(df.head())

#%% description
print(df.describe())

#%% columns
print(df.columns)

#%% info
print(df.info)

#%% check
date = df['release_date']
print(date)

#%%
df['year'] = df['release_date'].dt.year
df_cleaned = df['year'] <=2023
df_subset = df[['year','title','vote_average']]
print(df_subset.info)
grouped = df_subset.groupby('year')

for name, group in grouped:
    print(name)
    print(group.head())
    print()