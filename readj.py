
# Python program to read
# json file
import pandas as pd
  
import json
import os
cur_path = os.path.dirname(__file__)
# Opening JSON file
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
df.to_excel('l.xlsx',index=False)
f.close()