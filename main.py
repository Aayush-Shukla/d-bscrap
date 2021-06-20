# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import pandas as pd
import requests
import os
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

import csv
ua = UserAgent()

import urllib

links = []
input_file="input.txt"
cur_path = os.path.dirname(__file__)
# query_list=['administrative services trier de mexico s a de c v','aees inc','aees manufactuera s de r l de c v']
# query_list=['harita arc private limited','harita collection services private limited','pt tvs motor company indonesia jakarta','pt tvs motor company indonesia','sundaram auto components limited chennai','sundaram auto components limited','sundaram business development consulting shanghai co limited shanghai','sundaram business development consulting shanghai co limited','sundaram holding usa inc','tvs commodity financial solutions private limited','tvs credit services limited','tvs housing finance private limited','tvs housing limited','tvs micro finance private limited','tvs motor company europe b v amsterdam','tvs motor company europe b v','tvs motor services limited','tvs motor singapore pte limited singapore','tvs motor singapore pte limited','tvs two wheeler mall private limited'
# ]

query_list= [line.rstrip('\n') for line in open(input_file)]
query_list = list(set(query_list))
for count,query_c in enumerate(query_list,start=1):
    print("fetchin {} of {}".format(count,len(query_list)))
    query= query_c+" dnb"
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

# print(len(links),"+++++++++++++++++++++++++++++")


# for link in links:
#     print(link)
with open(cur_path+r"dnbv2/temp/dnb.txt", 'w+',encoding="utf-8") as f:
    for link in links:
        # print(link)

        if "dnb" and "/url?" not in link:
            # print("no")
            continue

        try:
            link=link.split("?q=")[-1].split("&sa")[0]
        except:
            # print("no")

            continue
        
        # print(link)
        print(link)
        f.write(link+"\n")

comm=['scrapy','crawl','data','-O','output.json','-a','file=dnb']
os.system(" ".join(comm))


print("done")



