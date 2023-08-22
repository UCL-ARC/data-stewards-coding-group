
import pandas as pd
import seaborn as sns

# import dataframe 
df = pd.read_csv("Movies_dataset.csv")
df_2023 = df[df['release_date'].str.contains('2023', na=False)]
df_2023['release_date'] = pd.to_datetime(df_2023['release_date'], infer_datetime_format=True) # note infer is deprecated
# Plot the data using Seaborn
movie_plot = sns.scatterplot(data=df_2023, x="popularity", y="release_date", hue="vote_count")

fig = movie_plot.get_figure()
fig.savefig("2023_plot.png", dpi=400)
