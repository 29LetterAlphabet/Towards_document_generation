import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from StringIO import StringIO
import time
import operator
import os


filt = "146.231.254.65"
area = 'destination'

def aToList (x, y):
	y.append(x)


def popDict (jStr):																																																	
	d = eval(jStr)
	if (d.get(area) == filt):
		aToList(d.get('time'), lt)
		aToList(d.get('source'), ls)
		aToList(d.get('destination'), ld)
		aToList(d.get('length'), ll)
		aToList(d.get('sourceAdr'), lsp)
		aToList(d.get('destAdr'), ldp)
		aToList(d.get('protocol'), lp)
		

def printToList(d, w):
	for x in d:
		w.write(str(x)+'\n')

input_fnames = [x for x in os.listdir(os.getcwd()) if x.endswith("json")]


for fname in input_fnames:
	lt = []
	ls = []
	ld = []
	ll = []
	lsp = []
	ldp = []
	lp = []


	f = open(fname)

	jsonPkt = ""
	count = 0
	for line in f:
	  jsonPkt += line
	  if line == "}\n":
	#  	print jsonPkt
	  	popDict(jsonPkt)
	  	count += 1
	  	jsonPkt = ""

	a,b = str(fname).split(".j")
	sl = open("%s-timeListOr.lst" % (a), "w")
	printToList(lt,sl)
	sl.close
	sl = open("%s-sourceIPList.lst" % (a), "w")
	printToList(ls,sl)
	sl.close
	sl = open("%s-destinationIPList.lst" % (a), "w")
	printToList(ld,sl)
	sl.close
	sl = open("%s-lengthList.lst" % (a), "w")
	printToList(ll,sl)
	sl.close
	sl = open("%s-sourcePortList.lst" % (a), "w")
	printToList(lsp,sl)
	sl.close
	sl = open("%s-dPortList.lst" % (a), "w")
	printToList(ldp,sl)
	sl.close
	sl = open("%s-protocolList.lst" % (a), "w")
	printToList(lp,sl)
	sl.close



	




# #df = pd.read_json('JsonOutput.json')
# with open('JsonOutput.json') as f:
# 	s = f.read()
# pythonOb = json.load(s)
# z = pythonOb.get('source')
# print z















