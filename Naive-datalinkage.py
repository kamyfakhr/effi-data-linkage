# Define empty list for further operations
import os
import random
import datetime
import pandas as pd
from fuzzywuzzy import fuzz
import numpy as np
import textdistance



with open("amazon_google_truth_small.csv", "r") as f:
    true_data = f.read()
amazon_df = pd.read_csv("amazon_small.csv")
google_df = pd.read_csv("google_small.csv")



#print("Selecting {} true data linkages and {} random pairs".format(true_rows, other_rows))
    

google_ids = google_df['idGoogleBase'].values
amazon_ids = amazon_df['idAmazon'].values
match_list = []

for i in range(len(amazon_df['idAmazon'])):
    ratio_list = []
    for j in range(len(google_df['idGoogleBase'])):
        ratio = fuzz.partial_ratio(amazon_df['title'][i].lower(), google_df['name'][j].lower())
        if ratio > 60:
            ratio_list.append((ratio, google_df['idGoogleBase'][j]))
        
    if len(ratio_list) > 0:
        max_ratio = max(ratio_list)
    
        match_list.append(list((amazon_df['idAmazon'][i], max_ratio[1])))


    
        


#other_row_segment = [[aid, gid] for aid, gid in zip(amazon_id_other, google_id_other) if [aid, gid] not in true_segment]

task1a_file = []
task1a_file.append(list(('idAmazon', 'idGoogleBase')))
task1a_file.extend(match_list)
task1a_file = "\n".join([ ",".join(x) for x in task1a_file ]) + "\n"

with open("task1a.csv", "w") as f:
    f.write(task1a_file)
    