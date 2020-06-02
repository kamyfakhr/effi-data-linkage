import os
import random
import datetime
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import textdistance
import re



with open("amazon_google_truth.csv", "r") as f:
    true_data = f.read()
amazon_df = pd.read_csv("amazon.csv")
google_df = pd.read_csv("google.csv")


special_chars = [',', '/', '?', '!', '[', ']', '()', '(', ')', '@', '#', '$', '%', '&', '*', '.', '.', '-', 
                 '_', '=', '+']


amazon_block = []
for i in range(len(amazon_df['title'])):
    for j in (amazon_df['title'][i]).split():
        if j not in special_chars:
        #amazon_block_dic[j] = amazon_df['idAmazon'][i]
            amazon_block.append(list((j, amazon_df['idAmazon'][i])))


    
#print(amazon_block)
amazon_blocks_file = []
amazon_blocks_file.append(list(('block_key', 'product_id')))
amazon_blocks_file.extend(amazon_block)

amazon_blocks_file = "\n".join([ ",".join(x) for x in amazon_blocks_file]) + "\n"


with open("amazon_blocks.csv", "w") as f:
    f.write(amazon_blocks_file)

 
        
#google_block_dic = {}  
google_block = []
for i in range(len(google_df['name'])):
    for j in (google_df['name'][i]).split():
        if j not in special_chars:
        #google_block_dic[j] = google_df['idGoogleBase'][i]
            google_block.append(list((j, google_df['id'][i])))




google_blocks_file = []
google_blocks_file.append(list(('block_key', 'product_id')))
google_blocks_file.extend(google_block)

google_blocks_file = "\n".join([ ",".join(x) for x in google_blocks_file]) + "\n"

with open("google_blocks.csv", "w") as f:
    f.write(google_blocks_file)