import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from StringIO import StringIO
import time
import os
import operator
from collections import defaultdict

input_fnames = [x for x in os.listdir(os.getcwd()) if x.endswith(".hlb")]
for name in input_fnames:
	bob = "/home/iggy/ipv4-heatmap/ipv4-heatmap -o "+ str(name)[:-4] +"Hilbert.png -a /home/iggy/ipv4-heatmap/labels/iana/iana-labels.txt < "+str(name)
	os.system(bob)


