import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from StringIO import StringIO
import time
import operator
import os




def aToList (x, y):
	if len(y) == 0:
		y[x] = 1
	elif x not in y:
		y[x] = 1
	else: 
		y[x] += 1

filt = "155.232.248.25"
area = "destination"
def popDict (jStr):																																																	
	d = eval(jStr)
	if (d.get(area) == filt):
		aToList(d.get('source'), ls)
		aToList(d.get('destination'), ld)
		aToList(d.get('length'), ll)
		aToList(d.get('sourceAdr'), lsp)
		if 'TCP' in d.get('type'):
			aToList(d.get('destAdr'), ldpT)
			aToList(d.get('protocol'), lpT)
		if 'UDP' in d.get('type'):
			aToList(d.get('destAdr'), ldpU)
			aToList(d.get('protocol'), lpU)

input_fnames = [x for x in os.listdir(os.getcwd()) if x.endswith("json")]


for fname in input_fnames:
	ls = {}
	ld = {}
	ll = {}
	lsp = {}
	ldpT = {}
	ldpU = {}
	lpT = {}
	lpU = {}

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
	sourceIt = sorted(ls.iteritems(), key=operator.itemgetter(1), reverse=True)
	sl = open("%s-sourceIPList.txt" % (a), "w")
	sl.write(str(sourceIt))
	sl.close
	sourceIt = sorted(ld.iteritems(), key=operator.itemgetter(1), reverse=True)
	sl = open("%s-destinationIPList.txt" % (a), "w")
	sl.write(str(sourceIt))
	sl.close
	sourceIt = sorted(ll.iteritems(), key=operator.itemgetter(1), reverse=True)
	sl = open("%s-lengthList.txt" % (a), "w")
	sl.write(str(sourceIt))
	sl.close
	sourceIt = sorted(lsp.iteritems(), key=operator.itemgetter(1), reverse=True)
	sl = open("%s-sourcePortList.txt" % (a), "w")
	sl.write(str(sourceIt))
	sl.close
	sourceIt = sorted(ldpT.iteritems(), key=operator.itemgetter(1), reverse=True)
	sl = open("%s-dPortListTCP.txt" % (a), "w")
	sl.write(str(sourceIt))
	sl.close
	sourceIt = sorted(lpT.iteritems(), key=operator.itemgetter(1), reverse=True)
	sl = open("%s-protocolListTCP.txt" % (a), "w")
	sl.write(str(sourceIt))
	sourceIt = sorted(ldpU.iteritems(), key=operator.itemgetter(1), reverse=True)
	sl = open("%s-dPortListUDP.txt" % (a), "w")
	sl.write(str(sourceIt))
	sl.close
	sourceIt = sorted(lpU.iteritems(), key=operator.itemgetter(1), reverse=True)
	sl = open("%s-protocolListUDP.txt" % (a), "w")
	sl.write(str(sourceIt))
	sl.close



	




# #df = pd.read_json('JsonOutput.json')
# with open('JsonOutput.json') as f:
# 	s = f.read()
# pythonOb = json.load(s)
# z = pythonOb.get('source')
# print z















