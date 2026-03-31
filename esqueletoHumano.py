import pandas as pd
df = pd.read_csv('csv/adult-human-skeleton.csv')
print(df.head())
print('--------------------------------------------------------')
print(df['region'].value_counts())
print('--------------------------------------------------------')
print(df.sort_values(by='fused_from', ascending=False).head())
print('--------------------------------------------------------')
print(df.query('region == "neck"'))
