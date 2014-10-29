import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from StringIO import StringIO
import time
import operator
import datetime
import os

input_fnames = [x for x in os.listdir(os.getcwd()) if x.endswith("json")]

for fname in input_fnames:
  z,x = "", ""
  f = ""
  g = ""
  a,b = 0, 0
  f = open(fname)
  counter = 0
  for line in f:
    if "time" in line:
      a,b = str(line).split(" : ")
      b = b.rstrip()
      b = b.lstrip()
      b = b.replace(',','')
      b = b.replace('"', '')
      setDate = datetime.datetime.strptime(b, '%d-%m-%Y %H:%M:%S').date()
      f.close()
      print str(setDate)+" "+str(fname)
      break



  name = fname
  f = open(name)
  z,x = str(name).split(".j")
  g = open(str(setDate)+"-"+z+".json", 'w')
  jsonPkt = ""
  count = 0

  for line in f:
    jsonPkt += line
    if "time" in line:
      a,b = line.split(" : ")
      b = b.rstrip()
      b = b.lstrip()
      b = b.replace(',','')
      b = b.replace('"', '')
      date =  datetime.datetime.strptime(b, '%d-%m-%Y %H:%M:%S').date()
      year = date.year
      month = date.month
      if year > setDate.year or (year == setDate.year and month > setDate.month):
        g.close()
        g = open(str(date)+"-"+z+".json", 'w')
        setDate = date

    if line == "}\n":
      g.write(jsonPkt) #write to file here

      count += 1
      if count % 50000 == 0:
        print count
      jsonPkt = ""

  f.close()
  g.close()
