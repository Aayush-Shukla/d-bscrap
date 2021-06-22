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
# input_file="input.txt"
cur_path = os.path.dirname(__file__)
# query_list=['administrative services trier de mexico s a de c v','aees inc','aees manufactuera s de r l de c v']
# query_list=['harita arc private limited','harita collection services private limited','pt tvs motor company indonesia jakarta','pt tvs motor company indonesia','sundaram auto components limited chennai','sundaram auto components limited','sundaram business development consulting shanghai co limited shanghai','sundaram business development consulting shanghai co limited','sundaram holding usa inc','tvs commodity financial solutions private limited','tvs credit services limited','tvs housing finance private limited','tvs housing limited','tvs micro finance private limited','tvs motor company europe b v amsterdam','tvs motor company europe b v','tvs motor services limited','tvs motor singapore pte limited singapore','tvs motor singapore pte limited','tvs two wheeler mall private limited'
# ]
for dirpath, dirnames, filenames in os.walk("input"):
    # for filename in filenames:
    print(os.path.join(dirpath, filenames[0]))
    input_file=os.path.join(dirpath, filenames[0])



sheetname=input("sheet name[default is first sheet]: ") or 0
first_row=int(input("first row :"))-1 
last_row=int(input("last row:"))-1 

namecol=input("Name column: ") or 0
country_col=input("country column: ") or 1


# test

# sheetname= 0
# first_row=1
# last_row=50

# namecol='J'
# country_col='L'






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
    print("fetchin \"{}\" of {}".format(row.loc["Name"],len(df)))
    # print(row)
    links=[]
    # print(ua.random)
    
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
  'referer': 'https://www.dnb.com/business-directory/top-results.html?term=alphabet&page=1',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'chosen_visitorFrom_cookie_new=DIR; HID=1622213872486; drift_aid=fd01f143-56e2-4af3-80f1-37b95896ac7e; driftt_aid=fd01f143-56e2-4af3-80f1-37b95896ac7e; DMCP=1; _bcvm_vrid_2775810355515379163=648726101229444880T6742C0D0B425ECB757510091BC42867E6A799D64629757287E89CD272F8EA87346D5CF123FD01D3EC8FE1A02739C2F02578B2CF21FA53BC943315EC219E9C85D; SSLB=0; ak_bmsc=4C15E8204A7EAB6450D336418140EBBA~000000000000000000000000000000~YAAQJ40sMRUFTux5AQAA0Qq0MQxt5GVPbVe9ciBgcACJhOkOk03VPIUIVWG1s0wgc/BSib00i77yPl3oybravFJbSm22bdsr2/mrhTyZZfF8HE/9IDAMp2nfw+NfrlD5puAc1et4pXwCaifncrAj4q/IDHI3RZPiWQkCslw32iscAyHjygEkBJaRltuip8EzcQMZCPiyAkvX7rDS4D5mW/aHNFmXMfKCOeNtUqKYLUUnYQuXIZvIwdfrAF9501ZxpFBRzjSb9qTQjOquKUD3/a7C8YZtnRzJOqsNr6n8tHYoWfGdjGr/ORtFifhQv15BGCxJrSNt5xW44kg367xsweBgUScOBoHKZNUYVem/qV8g/PZj8Y21KWhm9CST0vxqGr6nx1/r; AMCVS_8E4767C25245B0B80A490D4C%40AdobeOrg=1; drift_campaign_refresh=50799ad7-6046-499d-b950-5fa218ded004; integrated_search_query=alphabet; bm_mi=189B9331BA57C51D28572BD60F56C38A~Tn7vEBZovI2Dd2hZD9TH0bmwDL9uBbZig7yCoiiH2rhY95Yow7GwzIH8q5KeqWFCIQok6Kp6l1AkAJt6HbN/o7eOIN2USvWSHxrnEkWRSms4EiosjAirwEyFu4TNbvZ/7rOMy2TfB644PotgLaC1+tN+/k44CjaTPLuZEd9f6IMG/Dx8K7A2zpQjyPy4Jwy2zhQ+P/MBJ2vPo4OPNN/v7zsN1p2zUytpW50hbQ9PTIVeI/oj0UvkboiaQCkyxUbgRii4DNxfZh/5xv4Ttbfd0g==; AWSALB=mU4et1H7GawHknCnOY8dBmsG8pgtHthzxOl5zjC6zTgVEUwQWgs31CNO0NdMYha44BsPfFotqb+Lo94XHtl2Q6iuga8gbMEtHtN8BeuZMFg7pLgsjgLgQC8Gp8OA; AWSALBCORS=mU4et1H7GawHknCnOY8dBmsG8pgtHthzxOl5zjC6zTgVEUwQWgs31CNO0NdMYha44BsPfFotqb+Lo94XHtl2Q6iuga8gbMEtHtN8BeuZMFg7pLgsjgLgQC8Gp8OA; bm_sv=E563E561D67B35391BEC8F8C4134EFFE~Xi6qfE/e00tTtqdx+e29SoVKZUCsSqFQ92Do4UkeGH4Ukafg0Rk4F6yMXNqEzwlDueOfR3A4whLmIr771fbGNgNiFmui23s2dmRj3HRRooHoDypzaUV/gBKMF7K6VI+7jgJK9+dnFq650ehqKiOHcg==; AMCV_8E4767C25245B0B80A490D4C%40AdobeOrg=-1124106680%7CMCIDTS%7C18801%7CMCMID%7C75832162905368450318841924916097556759%7CMCOPTOUT-1624338735s%7CNONE%7CvVersion%7C5.2.0; ak_bmsc=4C15E8204A7EAB6450D336418140EBBA~000000000000000000000000000000~YAAQJ40sMSMGTux5AQAAnhS7MQz2CDTJBR8ir1SDDWenDUvmScAB/f23z4aFH0bv4YsFWOZhhUcJwcT4UgTidKvlD1rrNTD4pYHsuq2uW3df2Rmsoh4Wcg5XiYQTAZngdqFRzVKfXIH1TKJao+UMgc42E0opkZ7ErrZtutmGWgpdgS/ioOd+1lj4Pwe43P8Vs0CNBuh0K0jiEPdfhLjvbT7qGnJ02JPDzrwaT09vXGlST+iktoERiYgbhTwLzOWM3mk38m2XK2w0fSNiaR2U0Vigd2aQW8Sp2sxEMNHn4I6gfU1Fje4Dgevfu+T16VJZP7CwmVX8esR8am15oapjer008PDlSjwnABduTjQ96R/KX76Trkv2TDB+GPTdbBP//m7BBx0PV/o=; AWSALB=2Y9NEMPDpqYp+vB5QacNwpOE0aphUpksDtwKkgciBEfbfnWAWmXyBYB1wGiecpJuCk/7o5fED7SmJy6v0nNG5OJXLME77Nm1AyeMKuQIFYmDnQBePuxw4BiQsk3J; AWSALBCORS=2Y9NEMPDpqYp+vB5QacNwpOE0aphUpksDtwKkgciBEfbfnWAWmXyBYB1wGiecpJuCk/7o5fED7SmJy6v0nNG5OJXLME77Nm1AyeMKuQIFYmDnQBePuxw4BiQsk3J; bm_sv=E563E561D67B35391BEC8F8C4134EFFE~Xi6qfE/e00tTtqdx+e29SoVKZUCsSqFQ92Do4UkeGH4Ukafg0Rk4F6yMXNqEzwlDueOfR3A4whLmIr771fbGNgNiFmui23s2dmRj3HRRooG0xhDud7TFzsfhczTmKYJHiDL4qVsgYJci25ypu5KDMg=='
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
    
    try:

        link=base_link+first_comp["primaryNameForUrl"]+"."+first_comp["duns"]+".html"
    except: 
        continue
    
    print(link,"\n")
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
    # print(comp_dict)
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
clean_df=df.drop(df[df['excel_country'].str.lower()!=df['country'].str.lower()].index)

print(df.info)
# Closing file


with pd.ExcelWriter(os.path.join('output','output{}.xlsx'.format(random_string))) as writer:  
    clean_df.to_excel(writer, sheet_name='filtered',index=False)
    df.to_excel(writer, sheet_name='unfiltered',index=False)


# clean_df.to_excel('output{}.xlsx'.format(random_string),index=False,sheet_name='filtered')
# df.to_excel('output{}.xlsx'.format(random_string),index=False,sheet_name='unfiltered')

f.close()





