# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:55:12 2022

@author: Rishabh Arora
"""
#Importing necessary packages

#Data manipulation realted imports
import pandas as pdx
import numpy as npx
from datetime import datetime

#Other main imports
import requests
from bs4 import BeautifulSoup
import time;import json
import lxml

#Extra feature imports
from random import randint
import winsound

r_df = pdx.DataFrame()
print(r_df)

#Capture response data coming from URL
print('Getting data from URL...')
r_url='https://finance.yahoo.com/most-active?offset=0&count=100'

#Specifying headers
r_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

#Capturing response in variable
r_response=requests.get(r_url,headers=r_headers)

print("response.ok : {} , response.status_code : {}".format(r_response.ok , r_response.status_code))

#Checking if response is okay or not
if r_response.status_code == 200:
    print('Website respone ok')
else:
    print('Website respone NOT ok')

#Printing response
#Showing entire content that has been captured from the request
print(r_response)

#Parsing response data(content) into a variable
soup=BeautifulSoup(r_response.content,'lxml')


#Starting a loop so that each row of table data can be iterated. Each iteration will capture data for the new company
for item in soup.select('.simpTblRow'):
    
    my_dict = {"SYMBOL" : item.select('[aria-label=Symbol]')[0].get_text(),
              "NAME":item.select('[aria-label=Name]')[0].get_text(),
              "PRICE":item.select('[aria-label*=Price]')[0].get_text(),
              "CHANGE":item.select('[aria-label=Change]')[0].get_text(),
              "CHANGE_P":item.select('[aria-label="% Change"]')[0].get_text(),
              "M_CAP":item.select('[aria-label="Market Cap"]')[0].get_text(),
              "AVERAGE VOLUME":item.select('[aria-label*="Avg Vol (3 month)"]')[0].get_text(),
              "PE_RATIO":item.select('[aria-label*="PE Ratio (TTM)"]')[0].get_text()}
    
    r_df = r_df.append(my_dict,ignore_index=True)


#Printing dataframe to see the captured or recorded data
print(r_df)






