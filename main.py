# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import os
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import json

import csv
ua = UserAgent()

import urllib

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



sheetname=input("sheet name[default is first sheet]: ") or 0
first_row=int(input("first row :"))-1 
last_row=int(input("last row:"))-1 

namecol=input("Name column: ") or 0
country_col=input("country column: ") or 1


#test

# sheetname= 0
# first_row=1
# last_row=4

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
for (idx,row) in df.iterrows():
    print("fetchin {} of {}".format(idx,len(df)))
    # print(row)
    links=[]
    try:
        query= row.loc["Name"]+" site:\"www.dnb.com\""
    except:
        pass
    # print(query,"-----------===========")
    query = urllib.parse.quote_plus(query) # Format into URL encoding
    number_result = 1

    google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")

    result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})


    for r in result_div:
        # Checks if each element is present, else, raise exception
        try:
            link = r.find('a', href = True)
            
            # Check to make sure everything is present before appending
            if link != '' : 
                links.append(link['href'])

                # print(link['href'],"===================================",len(links))
            
                
        # Next loop if one element is not present
        except:
            continue
    comp_dict={"name":row.loc["Name"],"country":row.loc["Country"],"links":links}
    links_json.append(comp_dict)

# print(len(links),"+++++++++++++++++++++++++++++")


# for link in links:
#     print(link)
# with open(cur_path+r"dnbv2/temp/dnb.txt", 'w+',encoding="utf-8") as f:
for unit in links_json:
    newlinks=[]
    # print(link)
    for link in unit["links"]:
        if "dnb" and "/url?" not in link:
            # unit["links"].remove(link)
            # print("no")
            continue

        try:
            link=link.split("?q=")[-1].split("&sa")[0]
        except:
            # print("no")
            unit["links"].remove(link)

            continue
        
        # print(link)
        print(link)
        newlinks.append(link)
        # f.write(link+"\n")
    unit["links"]=newlinks
jsonString = json.dumps(links_json,indent=4)
jsonFile = open(cur_path+r"dnbv2/temp/dnb.json", "w")
# print(jsonString)
jsonFile.write(jsonString)
jsonFile.close()

comm=['scrapy','crawl','data','-O','output.json','-a','file=dnb']
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
df.to_excel('ll.xlsx',index=False)
f.close()





