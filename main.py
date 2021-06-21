# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import os
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import json
import http.client
import time
from random import random

import csv
ua = UserAgent()
from urllib.parse import quote
import urllib

random_string=str(time.time()).split(".")[0]
links_json = []
input_file="input.txt"
cur_path = os.path.dirname(__file__)
# query_list=['administrative services trier de mexico s a de c v','aees inc','aees manufactuera s de r l de c v']
# query_list=['harita arc private limited','harita collection services private limited','pt tvs motor company indonesia jakarta','pt tvs motor company indonesia','sundaram auto components limited chennai','sundaram auto components limited','sundaram business development consulting shanghai co limited shanghai','sundaram business development consulting shanghai co limited','sundaram holding usa inc','tvs commodity financial solutions private limited','tvs credit services limited','tvs housing finance private limited','tvs housing limited','tvs micro finance private limited','tvs motor company europe b v amsterdam','tvs motor company europe b v','tvs motor services limited','tvs motor singapore pte limited singapore','tvs motor singapore pte limited','tvs two wheeler mall private limited'
# ]
for dirpath, dirnames, filenames in os.walk("input"):
    # for filename in filenames:
    print(os.path.join(dirpath, filenames[0]))
    input_file=os.path.join(dirpath, filenames[0])



# sheetname=input("sheet name[default is first sheet]: ") or 0
# first_row=int(input("first row :"))-1 
# last_row=int(input("last row:"))-1 

# namecol=input("Name column: ") or 0
# country_col=input("country column: ") or 1


# test

sheetname= 0
first_row=1
last_row=50

namecol='J'
country_col='L'






df=pd.read_excel(input_file, usecols='{},{}'.format(namecol,country_col),header=None).loc[first_row:last_row]
df.columns=["Name","Country"]
df.drop_duplicates(keep='first',inplace=True)
print(df.info)

print(sheetname,first_row,last_row,namecol,country_col)




# for (idx,row) in df.iterrows():
#     print(row)

#     print(row.loc['Name'],"----------------")
#     break


# print(os.walk("input")[0])

# query_list= [line.rstrip('\n') for line in open(input_file)]
# query_list = list(set(query_list))





#google scrap


# for (idx,row) in df.iterrows():
#     print("fetchin {} of {}".format(idx,len(df)))
#     # print(row)
#     links=[]
#     try:
#         query= row.loc["Name"]+" site:\"www.dnb.com\""
#     except:
#         pass
#     # print(query,"-----------===========")
#     query = urllib.parse.quote_plus(query) # Format into URL encoding
#     number_result = 1

#     google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
#     response = requests.get(google_url, {"User-Agent": ua.random})
#     soup = BeautifulSoup(response.text, "html.parser")

#     result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})


#     for r in result_div:
#         # Checks if each element is present, else, raise exception
#         try:
#             link = r.find('a', href = True)
            
#             # Check to make sure everything is present before appending
#             if link != '' : 
#                 links.append(link['href'])

#                 # print(link['href'],"===================================",len(links))
            
                
#         # Next loop if one element is not present
#         except:
#             continue
#     comp_dict={"name":row.loc["Name"],"country":row.loc["Country"],"links":links}
#     links_json.append(comp_dict)

# # print(len(links),"+++++++++++++++++++++++++++++")









#direct dnb link scrap



for (idx,row) in df.iterrows():
    print("fetchin {} of {}".format(idx,len(df)))
    # print(row)
    links=[]
    
    conn = http.client.HTTPSConnection("www.dnb.com")
    payload = ''
    headers = {
                'authority': 'www.dnb.com',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
  'accept': '*/*',
  'sec-gpc': '1',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.dnb.com/business-directory/top-results.html?term=marico&page=1',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'chosen_visitorFrom_cookie_new=DIR; HID=1622213872486; drift_aid=fd01f143-56e2-4af3-80f1-37b95896ac7e; driftt_aid=fd01f143-56e2-4af3-80f1-37b95896ac7e; DMCP=1; _bcvm_vrid_2775810355515379163=648726101229444880T6742C0D0B425ECB757510091BC42867E6A799D64629757287E89CD272F8EA87346D5CF123FD01D3EC8FE1A02739C2F02578B2CF21FA53BC943315EC219E9C85D; SSLB=0; AMCVS_8E4767C25245B0B80A490D4C%40AdobeOrg=1; drift_campaign_refresh=5811a12a-c27a-426f-bb2c-6e479be1d4e5; AMCV_8E4767C25245B0B80A490D4C%40AdobeOrg=-1124106680%7CMCIDTS%7C18799%7CMCMID%7C75832162905368450318841924916097556759%7CMCOPTOUT-1624299187s%7CNONE%7CvVersion%7C5.2.0; AWSALB=/0ngSj1IM1BaTeF+tgjO038mwspJtScOteqDf+bUJGDwP94tzcaWJau/5Es2kYiTW7GheMgQ6IaDdp4AplXrsCgbgjZnwN+17tYZtSShpXC9LXhVC03j11pxoLS2; AWSALBCORS=/0ngSj1IM1BaTeF+tgjO038mwspJtScOteqDf+bUJGDwP94tzcaWJau/5Es2kYiTW7GheMgQ6IaDdp4AplXrsCgbgjZnwN+17tYZtSShpXC9LXhVC03j11pxoLS2; ak_bmsc=DB4D2CE3F6FFE64CDAD68DF6984C0B7E~000000000000000000000000000000~YAAQbI0sMcE16hd6AQAAx4ZsLwzvusqIGAyUDJA2FIEkB7+EPwcZVIwER1PdzLQA4ys6ObF3elr7ndsH7KRiiWrM+NM9LCidr0m5muIjUysCbQ8mTCS7z6kKrfsq/ye1i5kuL0qkf7XS8kZ/RSM+mcN46fhT1NWm/uCwpP12fZbvjcFRv8sjNw+EQvZGCDM/LSPnK6oex02Yy/bEyJ6bfbp/Ix6T5e0WaHMpLWLChggLru+sCiTWCExHzxPIHPjo7G/Bb/ob5YDBEKecxdpEHxrp4lSGK068oZnL1QStuYBuEB44Yn4SCH2pH+BtIGYhWQntLGwudL7DPy0Qu5SpTWs3bQpUJmQMZnz8jrSmztnnaUI5IvjD8IQajqY/7fhJxMtPGVi2jw==; SSLB=0; AWSALB=qTLyihsOTrS0BYFD1MuhfM3Pyw2FHF9cp1a+n4M31yVFKPCsF9g20ima0XsJaGFeSb9CNViQ84EvGP9AXhRljT9+Z5JxmUufgqBuvhttdrQEWLw9uW4DQXO6k2K9; AWSALBCORS=qTLyihsOTrS0BYFD1MuhfM3Pyw2FHF9cp1a+n4M31yVFKPCsF9g20ima0XsJaGFeSb9CNViQ84EvGP9AXhRljT9+Z5JxmUufgqBuvhttdrQEWLw9uW4DQXO6k2K9; bm_sv=3A7947F27987AB3BDFF67BB1E649668D~1uygBY7MgupR0SmFxX9VYngD3/eR+4kF5P1D5XxIJ0uhpxOrRtqDCGeD2Oi1Y/xd0w3Z3+hfp/2GfVG11FMOhPQtTBbmaN7yyNERyxt1GWzSMnkwL7vCoRuHbogFOpbtqysLl0ITPLj2cT1OrVOtKg=='
  }
    conn.request("GET", "/apps/dnb/thirdparty/dnbdirectutil?limited=false&captchaDone=true&pageSize=5&pageNumber=1&criteriasearch=true&searchTerm={}".format(quote(row.loc["Name"])), payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    try:
        first_comp=json.loads(data.decode("utf-8"))["searchCandidates"][0]["organization"]
    except:
        print(data.decode("utf-8"))
    # print(first_comp)
    base_link="https://www.dnb.com/business-directory/company-profiles."
    
    link=base_link+first_comp["primaryNameForUrl"]+"."+first_comp["duns"]+".html"
    
    print(link)
    links.append(link)
    time.sleep(random() * 2)













    # for r in result_div:
    #     # Checks if each element is present, else, raise exception
    #     try:
    #         link = r.find('a', href = True)
            
    #         # Check to make sure everything is present before appending
    #         if link != '' : 
    #             links.append(link['href'])

    #             # print(link['href'],"===================================",len(links))
            
                
    #     # Next loop if one element is not present
    #     except:
    #         continue
    comp_dict={"name":row.loc["Name"],"country":row.loc["Country"],"links":links}
    print(comp_dict)
    links_json.append(comp_dict)














#no check needed 


# for link in links:
#     print(link)
# with open(cur_path+r"dnbv2/temp/dnb.txt", 'w+',encoding="utf-8") as f:
# for unit in links_json:
#     newlinks=[]
#     # print(link)
#     for link in unit["links"]:
#         if "dnb" and "/url?" not in link:
#             # unit["links"].remove(link)
#             # print("no")
#             continue

#         try:
#             link=link.split("?q=")[-1].split("&sa")[0]
#         except:
#             # print("no")
#             unit["links"].remove(link)

#             continue
        
#         # print(link)
#         print(link)
#         newlinks.append(link)
#         # f.write(link+"\n")
#     unit["links"]=newlinks






jsonString = json.dumps(links_json,indent=4)
jsonFile = open(cur_path+r"dnbv2/temp/dnb{}.json".format(random_string), "w")
# print(jsonString)
jsonFile.write(jsonString)
jsonFile.close()

comm=['scrapy','crawl','data','-O','output.json','-a','file=dnb{}'.format(random_string)]
os.system(" ".join(comm))


print("done")


f = open("output.json",)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# # list
# for i in data:
#     print(i["country"])

df = pd.DataFrame.from_dict(data, orient='columns')
df=df.dropna(thresh=7)
# df=df.drop(df[df['excel_country'].str.lower()!=df['country'].str.lower()].index)

print(df.info)
# Closing file
df.to_excel('output{}.xlsx'.format(random_string),index=False)
f.close()





