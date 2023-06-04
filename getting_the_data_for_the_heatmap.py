import pandas as pd
#Here we get the data to use for the heatmap
df_model=pd.read_csv('./df_model_hourly.csv')
dfs = df_model[['location', 'timestamp', 'noise_level']]
dfs = dfs.drop_duplicates(subset=['location',  'timestamp'])
df_wide = dfs.pivot(index='timestamp', columns='location', values='noise_level')
df_wide.to_csv('max_noise_per_hour_per_location.csv')