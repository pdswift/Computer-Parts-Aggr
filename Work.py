# This script pulls computer part info from multiple sites and compares them
# CNA 330
# Group Project with PSwift
# Nathan Wick, ncwick@student.rtc.edu/ncwick96@gmail.com
#
# Code referenced from: https://github.com/RTCedu/CNA330
#
import mysql.connector
import sys
import json
import urllib.request
import os
import time


def connect_to_sql():
    conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='cna330')


def create_tables(cursor, Computer_Parts):

    cursor.execute('''CREATE TABLE "Computer_Parts" (id INT PRIMARY KEY AUTOINCREMENT, Date DATE, Class TEXT,
    Name TEXT, Model INT, Manufacturer TEXT, Quantity INT, Price FLOAT, Site TEXT);''')

    cursor.execute("INSERT INTO Jobs(id, Date, Class, Name, Model, Manufacturer, Quantity, Price, Site)"""
                   " VALUES(0,'11/8/18', 'RAM', 'Corsair 64gb RAM 3200', '224873', 'Corsair', '64',"
                   " '550.98', 'Amazon') ;")
    cursor.close()
    return cursor
