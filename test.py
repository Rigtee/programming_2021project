# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:32:17 2021

@author: gaeta
"""
import csv
import pandas as pd
from datetime import datetime




with open('log_chatbox.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    
try:
    df = pd.read_csv('log_chatbox.txt')
except FileNotFoundError:
    df = pd.DataFrame(columns=['Input', 'Output','Time','Date', 'Intents_predicted','Probability prediction','Status','Language']) 

new_row = {'Input':'Geo',  'Output':'Hello','Time':datetime.time(datetime.now()),'Date':datetime.date(datetime.now()), 'Intents_predicted':92,'Probability prediction':92, 'Status':97, 'Language':'EN'}
#append row to the dataframe
df = df.append(new_row, ignore_index=True)
df.to_csv('log_chatbox.txt',index=False)

try:
    df = pd.read_csv('log_chatbox.txt')
except FileNotFoundError:
    df = pd.DataFrame(columns=['Input', 'Output','Time','Date', 'Intents_predicted','Status','Language']) 

df1 = pd.DataFrame(columns=['Input', 'Output','Time','Date', 'Intents_predicted','Status','Language']) 
df.to_csv('log_chatbox1.txt',index=False) 