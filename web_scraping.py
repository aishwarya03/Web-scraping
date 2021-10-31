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
            url = a['href']
            txtt = a.text.strip()
            #url_lst.append(url)
            url_lst.append({"TEXT":txtt, "URLA":url})
#df=pd.DataFrame(url_lst, columns=['url'])
df = pd.DataFrame.from_dict(url_lst, orient='columns')
df.to_csv('result.csv')
print(df)