# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# chcp 65001 for command line

file = open('data_csv.csv','r')
file_output = open('data_cleaned.csv','w')

def cleaner(a):
	a.strip()
	if a.decode('utf-8').lower() in true_words:
		a = 'true'
	elif a.decode('utf-8').lower() in false_words:
		a = 'false'
	elif a.endswith(",0") or a.endswith(".0"):
		a = a[:-2]
	file_output.write(str(a)+'|') #write value to the output file

true_words = ['так', 'є', 'в наявності', 'наявне', '+']
false_words = ['ні', 'немає', '-', 'ні']

for line in file:
	line = line.rstrip()
	line = line.split('|')
	for cell in line:
		cleaner(cell)
	file_output.write('\n')
