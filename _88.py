import pandas as pd


df = pd.read_csv('countries_by_area.txt')
df_by_population = df.sort_values('population_2013', ascending=False)
df_by_population['density'] = df_by_population['population_2013'] / df_by_population['area_sqkm']
df_by_population = df_by_population.sort_values('density', ascending=False)
print(df_by_population['country'].head().to_string(index=False))
