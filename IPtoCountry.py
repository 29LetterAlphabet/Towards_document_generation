import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from StringIO import StringIO
import time
import os
import operator
from collections import defaultdict
from itertools import cycle, islice
import pygeoip

gi = pygeoip.GeoIP('/home/iggy/Desktop/Repository/GeoIP.dat')

def aToList (x, y):
	if len(y) == 0:
		y[x] = 1
	elif x not in y:
		y[x] = 1
	else: 
		y[x] += 1

input_fnames = [x for x in os.listdir(os.getcwd()) if x.endswith(".hlb")]

for name in input_fnames:
	d = {}
	x = open(name)
	for line in x:
		val = line.rstrip()
		aToList(gi.country_name_by_addr(val), d)
	a,b = str(name).split('.h')
	sourceIt = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)
	sl = open("%s-IPCountryList.txt" % (a), "w")
	sl.write(str(sourceIt))
	sl.close
