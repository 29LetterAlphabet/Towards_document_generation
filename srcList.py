import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from StringIO import StringIO
import time
import os
import operator
from collections import defaultdict

input_fnames = [x for x in os.listdir(os.getcwd()) if x.endswith("sourceIPList.txt")]

for name in input_fnames:
	c = str(name)[:-16]
	f = open(c+'.hlb', 'w')
	g = open(name)
	s = g.read()
	tu = eval(s)
	for x,y in tu:
		f.write(x+'\n')

	g.close()
	f.close()

