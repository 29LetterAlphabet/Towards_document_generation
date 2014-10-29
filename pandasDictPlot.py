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

input_fnames = [x for x in os.listdir(os.getcwd()) if x.endswith("txt")]


total = 1


def build_dict_gareth(fname):
	global total
	with open(fname) as f:
		s = f.read()
		tu = eval(s)
		global numPackets
		numPackets = sum([x[1] for x in tu])
		total = numPackets
		first20 = tu[:20]
		d = dict(first20)
		if "-1" in d.keys():
			del d['-1']
		return d



def figures(ld):
	fontsize = 20
	global total
	dList = build_dict_gareth(ld)
	srt = sorted(dList.iteritems(), key=operator.itemgetter(1), reverse=True)

	lpk = [ x[0] for x in  srt]
	lpv = [ (float(x[1])/float(total))*100 for x in srt]
	lpp = [ x[1] for x in srt]

	df = pd.Series(lpv, index = lpk)
	my_colours = list(islice(cycle(['b', 'r', 'g', 'y', 'k', 'm', 'c']), None, len(df)))
	ax = df.plot(kind='bar', color=my_colours)
	naming = str(ld)
	title = ""
	f = ""
	if ("destinationIP" in naming):
		title = "Destination IP address packet distribution"
		f = "Desitnation IP address of packet"
	elif ("dPort" in naming and "TCP" in naming):
		title = "Destination port packet distribution for TCP packets"
		f = "Desitnation port of packet"
	elif ("protocol" in naming and "TCP" in naming):
		title = "Packet protocol distribution for TCP packets"
		f = "Protocol of packet"
	elif ("dPort" in naming and "UDP" in naming):
		title = "Destination port packet distribution for UDP packets"
		f = "Desitnation port of packet"
	elif ("protocol" in naming and "UDP" in naming):
		title = "Packet protocol distribution for UDP packets"
		f = "Protocol of packet"
	elif ("sourceIP" in naming):
		title = "Source IP packet distribution"
		f = "Source IP address of packet"
	elif ("sourcePort" in naming):
		title = "Source port packet distribution"
		f = "Source port of packet"
	elif ("length" in naming):
		title = "Packet length distribution"
		f = "Length of packet"
	elif ("Country" in naming):
		title = "Unique source IP frequency by country"
		f = "Country of source IP"
	ax.set_xlabel(f, fontsize=fontsize)
	if "Country" in naming:
		ax.set_ylabel('Percentage of unique IP addresses', fontsize=fontsize)
	else:
		ax.set_ylabel('Percentage of total packets', fontsize=fontsize)
	
	ax.set_title(title, fontsize=fontsize)
	plt.tight_layout()
	figName = ""+str(ld)+"Bar.png"
	plt.savefig(figName)
	plt.clf()
	of = open(""+str(ld)[:11]+str(title)+'_top20_table.txt', 'w')
	of.write(str(title)+"\n")

	ccr = 0
	ccrr = 0
	
	for i in range (0,len(lpk)):
		of.write(""+str(lpk[i]))
		of.write("\t"+str(lpp[i]))
		ccr += int(lpp[i])
		of.write("\t"+str(lpv[i])+"%\n")
		ccrr += int(lpv[i])
	of.write('Total:\t')
	of.write(str(ccr)+'\t')
	ccr = 0
	of.write(str(ccrr)+'\n')
	ccrr = 0
	of.write('Number of unique hits:\t'+str(numPackets))
	of.close()


for name in input_fnames:
	figures(name)



# totalPackets = res[1]

# print totalPackets
# makeDict(buildDict(fSource), ls)
# makeDict(buildDict(fLength), ll)
# makeDict(buildDict(fSport), lsp)
# makeDict(buildDict(fDport), ldp)
#makeDict(buildDict(fProt), lp)