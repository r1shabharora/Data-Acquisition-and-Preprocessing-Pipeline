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


#Extra feature imports
from random import randint
import winsound

#The URL from where data needs to be pulled
rURL = 'https://www.google.com'

#Capture response data coming from URL
rdata = requests.get(rURL)
