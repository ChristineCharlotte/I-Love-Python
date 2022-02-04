# import pandas as pd
#
# df = pd.read_csv('csv.csv', index_col=0)
# # print(df.head())

# # new_df = df.rename(columns={'Name': 'Domain Name'}, mapper=str.strip, axis='columns')
# new_df = df.rename( mapper=str.strip, axis='columns')
# # print(new_df)
# # print(df.columns)
#
# cols = list(df.columns)
# cols = [x.lower().strip() for x in cols]
# df.columns = cols
# print(df.head())

import pandas as pd

df = pd.read_csv('csv.csv', index_col=0)
df.columns = [x.lower().strip() for x in df.columns]
# print(df.head())

# mask
admit_mask = df['chance of admit'] > 0.7

# print(df.where(admit_mask).head())
# print(df[df['chance of admit'] > 0.75].head())

result = (df['chance of admit'] > 0.7) & (df['chance of admit'] < 0.9)
# print(result)

# print('\n')

result2 = df['chance of admit'].gt(0.7).lt(0.9).head()
# print('result2', result2)

df['Serial Number'] = df.index

df = df.set_index('Chance Of Admit')
print(df)
