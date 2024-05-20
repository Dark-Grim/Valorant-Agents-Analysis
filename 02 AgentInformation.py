from bs4 import BeautifulSoup
# from requests.auth import HTTPBasicAuth
import requests
import pandas as pd

with open("TestContent/content.html","r", encoding="utf-8") as f:
    htmlDoc = f.read()

soup = BeautifulSoup(htmlDoc,'html5lib')
tableOfCharacters =  soup.find('table', class_ = 'wikitable sortable')
titles = tableOfCharacters.find_all('th')


tableHeader = [title.text.strip() for title in titles] # List Comprehension

df = pd.DataFrame(columns= tableHeader)
# print(df)

resource_patch_index = tableHeader.index('Release Patch')

tableContents = tableOfCharacters.find_all('tr')
for row in tableContents[1:]:
    rowData = row.find_all('td')
    individualRowData = [data.text.strip() for data in rowData]

    if len(individualRowData) < len(tableHeader):
        individualRowData.insert(resource_patch_index,'Beta')

    length = len(df)
    df.loc[length] = individualRowData
df.to_csv(r'D:\Valorant Dataset\Data\AgentInformation.csv',index=False)
