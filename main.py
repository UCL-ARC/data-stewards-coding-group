import pandas as pd

# read the csv file
df = pd.read_csv('Movies_dataset.csv')

## print the first 5 rows of the dataframe
#print(df.head())

## print a description of the dataframe
#print(df.describe())

## print information about the dataframe
#print(df.info())

## print a list of the cloumns in the dataframe
#print(df.columns)

# create subset dataframe with the columns: year, title and vote_average
df['year'] = df['release_date'].dt.year

df_subset = df[['year', 'title', 'vote_average']]

df_cleaned = df_subset[df_subset['year'] <= 2023]
# group the dataframe by the year column
grouped = df_cleaned.groupby('year')

vote_dict = {}

for name, group in grouped:
    vote_dict[name] = group['vote_average'].mean()

print(vote_dict)
