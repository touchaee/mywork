import pandas as pd
import numpy as np
import os

cwd = os.path.abspath('')

for file in os.listdir(cwd):
    filename = os.fsdecode(file)
    if filename.endswith('.xlsx'):
        print(filename)
    else:
        pass

dict_store_df = {}
for file in os.listdir(cwd):
    filename = os.fsdecode(file)
    if filename == 'result.xlsx':
        pass
    elif filename.endswith('.xlsx'):
        dict_store_df['df{}'.format(filename[0])] = pd.read_excel(filename, skiprows= 12)
    else:
        pass


for key in dict_store_df:
    dict_store_df[key] = dict_store_df[key][['Title', 'Citations']]
    dict_store_df[key].drop(dict_store_df[key].tail(2).index,inplace=True)

month = pd.read_excel('2.xlsx', skiprows= 6)
month = month.iloc[1,2]

result = pd.merge(dict_store_df['df2'], dict_store_df['df1'], how = 'left', on = 'Title')
result['change'] = result['Citations_x'] - result['Citations_y']
result = result[['Title', 'Citations_y','change']]
result.columns = ['Title', 'First', month]
result['Total'] = result['First'] + result[month]
result.head()

for i in range(3,len(dict_store_df)+1):
    month = pd.read_excel('{}.xlsx'.format(i), skiprows= 6)
    month = month.iloc[1,2]
    result = pd.merge(dict_store_df['df{}'.format(i)], result, how='left', on = 'Title')
    result.fillna(0, inplace = True)
    result[month] = result['Citations'] - result['Total']
    del result['Total']
    del result['Citations']
    result['Total'] = result.iloc[:, 1:].sum(axis = 1)

result.index = range(1, len(result)+1)

result.to_excel('result.xlsx')
