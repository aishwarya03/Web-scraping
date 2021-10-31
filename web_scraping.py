from bs4 import BeautifulSoup as bs
import requests
import validators
import re
import pandas as pd
queries=['ui figma', 'digital art']
url_lst=[]
with requests.Session() as s:
    for query in queries:
        response=requests.get("https://www.behance.net/search/projects?tracking_source=typeahead_search_direct&search="+query)
        soup=bs(response.content,'lxml')
        for a in soup.find_all('a',attrs={'href': re.compile("^https://")}):
            url=a['href']
            #print("Found the URL:", url)
            url_lst.append(url)
#print(url_lst)
df=pd.DataFrame(url_lst, columns=['url'])
df.to_csv('result.csv')
print(df)