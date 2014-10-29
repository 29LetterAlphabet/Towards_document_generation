import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import re
from StringIO import StringIO
import time
import os
import operator
from collections import defaultdict
from itertools import cycle, islice
import numpy as np
import datetime as dt
import ipaddr

portF = '24785'
portG = '22'

input_fnames = [x for x in os.listdir(os.getcwd()) if x.endswith("lst")]

fontsize = 20
lc = []
lt = []
ls = []
ld = []
ll = []
lsp =[]
ldp = []
lp = []
lTimeHits = [0 for i in range(30)]

for name in input_fnames:
	if "time" in name:
		f = open(name)
		for line in f:
			val = line.rstrip()
			z = time.strptime(val, "%d-%m-%Y %H:%M:%S")
			val = dt.datetime(z.tm_year, z.tm_mon, z.tm_mday, z.tm_hour, z.tm_min, z.tm_sec)
			lt.append(val)
	if "destination" in name:
		f = open(name)
		for line in f:
			val = line.rstrip()
			ld.append(val)
	elif "dPort" in name:
		f = open(name)
		for line in f:
			val = line.rstrip()
			ldp.append(val)
	elif "length" in name:
		f = open(name)
		for line in f:
			val = line.rstrip()
			ll.append(val)
	elif "protocol" in name:
		f = open(name)
		for line in f:
			val = line.rstrip()
			lp.append(val)
	elif "sourceIP" in name:
		f = open(name)
		for line in f:
			val = line.rstrip()
			ls.append(val)
	elif "sourcePo" in name:
		f = open(name)
		for line in f:
			val = line.rstrip()
			lsp.append(val)


dayArr = np.array([dt.datetime(2013, 12, i, 23, 59, 59) for i in range(1,31)])

c1 = 0

for q in lt:
	if c1 ==0:
		c1 = int(q.day)
	z = int(c1)-1

	if int(q.day) > c1 and c1 != 30:
		c1 = int(q.day)
		z += 1
		lTimeHits[z] += 1
	else:
		lTimeHits[z] += 1


df = pd.Series(lTimeHits, index = dayArr)
plt.figure()
ax =df.plot()
ax.set_xlabel('Time (days)', fontsize=fontsize)
ax.set_ylabel('Number of packets per day', fontsize=fontsize)
ax.set_title('Time series of packets received', fontsize=fontsize)
plt.tight_layout()
plt.savefig('TimeSeries')
plt.clf()

lTimeHitsC = [0 for i in range(1,31)]
cou = 0
val = 0
for x in lTimeHits:
	val += x
	lTimeHitsC[cou] = val
	cou += 1
	


df = pd.Series(lTimeHitsC, index = dayArr)
plt.figure()
ax =df.plot()
ax.set_xlabel('Time (days)', fontsize=fontsize)
ax.set_ylabel('Number of packets per day', fontsize=fontsize)
ax.set_title('Time series of packets received - Cumulative', fontsize=fontsize)
plt.tight_layout()
plt.savefig('TimeSeriesCumulative')
plt.clf()


y_val = [int(x) for x in ldp]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(lt,y_val,color="green",marker=".",s=0.5)
# ax =df.plot()
ax.set_xlabel('Time (days)', fontsize=fontsize)
ax.set_ylabel('Destination port of packet', fontsize=fontsize)
ax.set_ybound(lower=0)
ax.set_title('Time series of destination port hits', fontsize=fontsize)
plt.tight_layout()
plt.savefig('DportvsTime')
plt.clf()


time = []
countr = -1
for i in ldp:
	countr += 1
	if i == portF:
		time.append(lt[countr])

c1 = 0
lTimeHits2 = [0 for i in range(30)]
for q in time:
	if c1 ==0:
		c1 = int(q.day)
	z = int(c1)-1

	if int(q.day) > c1 and c1 != 30:
		c1 = int(q.day)
		z += 1
		lTimeHits2[z] += 1
	else:
		lTimeHits2[z] += 1

df = pd.Series(lTimeHits2, index = dayArr)
plt.figure()
ax =df.plot()
ax.set_xlabel('Time', fontsize=fontsize)
ax.set_ylabel('Number of packets per day', fontsize=fontsize)
ax.set_title('Packets sent to destination port '+portF, fontsize=fontsize)
plt.tight_layout()
plt.savefig('port'+portF+'vsTime')
plt.clf()

time = []
countr = -1
for i in ldp:
	countr += 1
	if i == portG:
		time.append(lt[countr])

c1 = 0
lTimeHits3 = [0 for i in range(30)]
for q in time:
	if c1 ==0:
		c1 = int(q.day)
	z = int(c1)-1

	if int(q.day) > c1 and c1 != 30:
		c1 = int(q.day)
		z += 1
		lTimeHits3[z] += 1
	else:
		lTimeHits3[z] += 1

df = pd.Series(lTimeHits3, index = dayArr)
plt.figure()
ax =df.plot()
ax.set_xlabel('Time', fontsize=fontsize)
ax.set_ylabel('Number of packets per day', fontsize=fontsize)
ax.set_title('Packets sent to destination port '+portG, fontsize=fontsize)
plt.tight_layout()
plt.savefig('port'+portG+'vsTime')
plt.clf()

