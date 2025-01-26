import pandas as pd
import requests
from bs4 import BeautifulSoup

df2024= pd.read_html('https://www.nirfindia.org/Rankings/2024/OverallRanking.html')
result = df2024[0]
#print(result)
edf = pd.DataFrame()
for l in df2024[1:]:
    edf = pd.concat([edf, l])

result = result.reset_index(drop=True)
edf = edf.reset_index(drop=True)
df1 = pd.concat([result, edf], axis=1)

df1['Year']= 2024




df2023= pd.read_html('https://www.nirfindia.org/Rankings/2023/OverallRanking.html')
result1 = df2023[0]

edf1 = pd.DataFrame()
for l in df2023[1:]:
    edf1 = pd.concat([edf1, l])

result1 = result1.reset_index(drop=True)
edf1 = edf1.reset_index(drop=True)
df2 = pd.concat([result1, edf1], axis=1)

df2['Year']= 2023






df2022= pd.read_html('https://www.nirfindia.org/Rankings/2022/OverallRanking.html')
result2 = df2022[0]

edf2 = pd.DataFrame()
for l in df2022[1:]:
    edf2 = pd.concat([edf2, l])

result2 = result2.reset_index(drop=True)
edf2 = edf2.reset_index(drop=True)
df3 = pd.concat([result2, edf2], axis=1)

df3['Year']= 2022

dftotal = pd.concat([df1, df2, df3])
print(dftotal)
#dftotal.to_excel('Combined_data.xlsx')

sorted_data = df1.sort_values('TLR (100)', ascending=False)

quartiles = pd.qcut(sorted_data['TLR (100)'], 4, labels=False)

sorted_data['Quartile'] = quartiles

# Extracting the top quartile
top_performing_group = sorted_data[sorted_data['Quartile'] == 3]
print(top_performing_group)
