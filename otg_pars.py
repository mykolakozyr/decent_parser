# -*- coding: utf-8 -*-

import pandas as pd
import time
from random import randint

print '-----Pandas Environment are set-----\n-----We are ready to parse-----'
time.sleep(2)

file = open('url_real.txt', 'r') # open file with real urls

def search_otg(url,num):

	print 'Parsing the OTG number ' + str(num)

	tables = pd.read_html(url) # Returns list of all tables on page
	passport_table = tables[0] # Takes certain table from page

	# write the .csv file with the '|' separator and 'utf-8' encoding
	# create separate file for every otg
	passport_table.to_csv('data/otg_'+str(num) + '.csv', header=True, index=False, encoding='utf-8', sep='|')

	interval = randint(0,3)
	time.sleep(interval)

id = 1

#loop for all the regions
for line in file:
	if id == 5: # for testing purposes
		break
	search_otg(line, id)
	id = id + 1