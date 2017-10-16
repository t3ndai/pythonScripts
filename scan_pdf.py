#! /usr/bin/env python3.4
#Scan for files ending with a certain extension

import os, os.path
import re

def print_pdf (root, dir, files):
	for file in files:
		path = os.path.join(root,file)
		path = os.path.normcase(path)
		if re.search(r".*\.pdf", path):
			print(path)

for root, dirs, files in os.walk('.'):