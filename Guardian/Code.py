import pandas as pd
import requests

API_KEY="57c165d4-df33-45c1-9cb4-fed1058b8d66"#downloaded from guardian web

urllist=[]
for i in range(1,26):#generating urls to access each page
    a="https://content.guardianapis.com/world/narendra-modi?from-date=2021-01-01&api-key=57c165d4-df33-45c1-9cb4-fed1058b8d66&type=article&page="
    b=str(i)
    c=a+b
    urllist.append(c)
    
info=[]
def json(url1):#collecting info in json format for each url
    response=requests.get(url1)
    x=response.json()
    info.append(x)

output=[json(url1) for url1 in urllist] 

finallist=[]#extracting the required info using pandas
try:
    for k in range(24):
        for j in range(10):
            value=dict(webTitle=info[k]['response']['results'][j]['webTitle'],
            sectionname=info[k]['response']['results'][j]['sectionName'],
            publisheddate=info[k]['response']['results'][j]['webPublicationDate'])
            finallist.append(value)
except Exception as e:
    print(e)
    
datanew=pd.DataFrame(finallist)#dataframe creation
datanew.to_excel('Articles_on_modi.xlsx')#creates excel file
