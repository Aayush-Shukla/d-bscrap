import os
cur_path = os.path.dirname(__file__)

with open(os.path.join(cur_path,"temp","dnb.txt"), 'r', encoding='utf-8') as f:
    # open('textfr', 'r', encoding='utf-8')
  
    for line in f:
        print(line)
