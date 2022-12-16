# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:55:12 2022

@author: Rishabh Arora
"""
#Importing necessary packages
!pip install "pymongo[srv]"

#Data manipulation realted imports
import pandas as pdx
import numpy as npx
from datetime import datetime

import pymongo
from pymongo import MongoClient
import os

from urllib.parse import quote_plus
from pprint import pprint

#Other main imports
import requests
from bs4 import BeautifulSoup
import time;import json
import lxml

#Extra feature imports
from random import randint
import winsound

try:
    
    s_time = datetime.now()
    
    #Creating a blankk dataframe
    r_df = pdx.DataFrame()
    print(r_df) 
    
    #Capture response data coming from URL
    #Default count of companies is 100 but this can be changed by just replacing the number in the end of the URL
    print('Getting data from URL...')
    r_url='https://finance.yahoo.com/most-active?offset=0&count=100'
    
    #Specifying headers
    r_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    
    #Capturing response in variable
    r_response=requests.get(r_url,headers=r_headers)
    
    #Printing the response status
    print("response.ok : {} , response.status_code : {}".format(r_response.ok , r_response.status_code))
    
    
    #Checking if response is okay or not. In case the response is not 'OK' then program will auto-quit.
    if r_response.status_code == 200:
        print('Website respone ok')
    else:
        print('Website respone NOT ok')
        print('Quitting the program')
        exit()
    
    #Printing response
    #Showing entire content that has been captured from the request
    print(r_response)
    
    #Parsing response data(content) into a variable
    soup=BeautifulSoup(r_response.content,'lxml')
    
    
    #Starting a loop so that each row of table data can be iterated. Each iteration will capture data for the new company
    for item in soup.select('.simpTblRow'):
        
        #Data will be captured in dictionary
        my_dict = {"SYMBOL" : item.select('[aria-label=Symbol]')[0].get_text(),
                  "NAME":item.select('[aria-label=Name]')[0].get_text(),
                  "PRICE":item.select('[aria-label*=Price]')[0].get_text(),
                  "CHANGE":item.select('[aria-label=Change]')[0].get_text(),
                  "CHANGE_P":item.select('[aria-label="% Change"]')[0].get_text(),
                  "M_CAP":item.select('[aria-label="Market Cap"]')[0].get_text(),
                  "AVERAGE VOLUME":item.select('[aria-label*="Avg Vol (3 month)"]')[0].get_text(),
                  "PE_RATIO":item.select('[aria-label*="PE Ratio (TTM)"]')[0].get_text()}
        
        #Data that was captured in dictionary is now being appended to the dataframe
        r_df = r_df.append(my_dict,ignore_index=True)
    
    
    #Printing dataframe to see the captured or recorded data
    print(r_df)
    
    
    #Database loading part
    username = "Rishabh_connection"
    password = "Rish@9090#"
    host = "@cluster0.ov5lnlw.mongodb.net/?retryWrites=true&w=majority"
    
    import urllib    
    from pymongo.server_api import ServerApi
    uri = "mongodb+srv://%s:%s@%s"%(urllib.parse.quote_plus("Rishabh_connection"),urllib.parse.quote_plus("Rish@9090#"),host)
    client = MongoClient(uri)
    server_api = ServerApi('1')

    client = pymongo.MongoClient("mongodb+srv://Rishabh_connection:<password>@cluster0.ov5lnlw.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    db = client.test
    print(db)

        
    client = pymongo.MongoClient("mongodb+srv://paul:E1IDRHJLFJbM5Q8z@cluster0.pudqg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    client = pymongo.MongoClient("mongodb+srv://Rishabh_connection:Rish@9090#@cluster0.ov5lnlw.mongodb.net/?retryWrites=true&w=majority")
    
    db = client["mydata"]
    collection=db['listings']
    
    
    print(client.list_database_names())
    print(collection)
    
    #import pypyodbc
    #connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};''Server=34.140.29.246;''Database=master;''encrypt=yes;''TrustServerCertificate=yes;''UID=sa;''PWD=Pr0gramming!',autocommit = True)
    #connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};''Server=34.140.29.246;''Database=Customer;''encrypt=yes;''TrustServerCertificate=yes;''UID=sa;''PWD=Pr0gramming!',autocommit = True)
    
    #cursor = connection.cursor()
    #SQLCommand = ("CREATE TABLE stock(ID INT);")
    #cursor.execute(SQLCommand)
    #SQLCommand = ("INSERT INTO stock VALUES(?);")
    #cursor.execute(SQLCommand,40)
    #SQLCommand = ("INSERT INTO stock VALUES(my_dict);")
    #cursor.execute(SQLCommand)
    #SQLCommand = ("SELECT * FROM stock;")
    #cursor.execute(SQLCommand)
    #results = cursor.fetchone()
    #print('First result is:',results[0])
    #results = cursor.fetchone()
    #print('Next result is:',results[0])
    #print('done')
    
    #Notify user by playing 3 beep sounds
    freq = 5000
    duration = 500
    winsound.Beep(freq,duration)
    x = 1
    
    for x in range(2):
        winsound.Beep(freq,duration)
        time.sleep(0.2)
    
    print('Time taken :',str(datetime.now()-s_time).split('.')[0])

except:
    print('Unknown error in program')

