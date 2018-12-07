# This script pulls computer part info from multiple sites and compares them
# CNA 330
# Group Project with PSwift
# Nathan Wick, ncwick@student.rtc.edu/ncwick96@gmail.com
# parker Swift, pdswift@stundent.rtc.edu
# Code referenced from: https://github.com/RTCedu/CNA330/JobHunter/JobHunter.py
# https://github.com/RTCedu/CNA336/Spring2018/Sql.py

import mysql.connector
import bs4
import sys
import json
import urllib.request
import urllib3
import urllib
import os
import time
import requests
import urlopen

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='Computer_Parts')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Computer_Parts(id INTEGER PRIMARY KEY AUTO_INCREMENT, Date DATE, "
          "Name TEXT, Class TEXT, Quantity INTEGER, Model INTEGER,Manufacturer TEXT, Price INTEGER, Site TEXT)")


# Creates test entry to ensure things are going as they should be.
respones = requests.get ("http://www.mouser.com")
print (respones.content)
c.execute("INSERT INTO Computer_Parts(Date, Name, Site) "
          "Values(NOW(),'Corsair Vengeance LPX ','http://www.mouser.com')")
#c.close()


# {                 Planning on using these in boolean ops later, may delete if better method found
#Classes for db table, and var assignment for later processing
#a = "RAM"; b = "Heat_Sink"; c = "CPU"; d = "PSU"; e = "Mother_Board"

# Sites for db table, and var assignment for later processing
#eb = "Ebay"; me = "Mouser_Electronics"; ppp = "Pc_Part_Picker"; ne = "New_Egg"
# }

# Runs with exit code 0, no errors, and now creates and writes to the db/table
#Work in progress below

counter = int
query = "https://www.newegg.com/Processors-Desktops/SubCategory/ID-343"
try:
    #query = 1
   contents = urllib.request.urlopen(query)
   response = contents.read()
   with open('python_respones.txt', 'w') as w:
    print(response, file=w)
    #jsonpage = json.load(response)
   pass
   time.sleep(1)
  # data = json.dumps(jsonpage(c))
  # for i in data:
  #     conn.c(
  #         "INSERT INTO Computer_Parts(#VAR STUFF HERE#+#TABLE VALUES/DATA#)"
   #    )
finally:
   print("FIN")