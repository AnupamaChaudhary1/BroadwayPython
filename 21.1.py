import pandas as pd

# Example DataFrame
data = {
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York'],
    'Temperature': [30, 25, 32, 28, 31],
    'Humidity': [80, 75, 85, 70, 78]
}

df = pd.DataFrame(data)
# print(df)
# mean_df = df.groupby('City').mean()
# print(mean_df)

# median_df = df.groupby('City').median()
# print(median_df)

# Drop the row with index 1 (Los Angeles)
# df_dropped = df.drop(1)
# print(df_dropped)

mode_df = df.groupby('City').agg(lambda x: x.mode()[0])
print(mode_df)

# df_filtered = df[df['Temperature'] >= 30]
# print(df_filtered)

# agg_df = df.groupby('City').agg({
#     'Temperature': ['mean', 'min', 'max'],
#     'Humidity': ['mean', 'std']
# })
# print(agg_df)





