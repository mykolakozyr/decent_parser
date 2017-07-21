# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pandas as pd
import time
from random import randint
from bs4 import BeautifulSoup
import urllib2


print '-----Pandas Environment are set-----\n-----We are ready to parse-----'
time.sleep(2)

file = open('url_real.txt', 'r') # open file with real urls

def search_otg(url,num):

	print 'Parsing the OTG number ' + str(num)

	# create separate file for every otg
	f = open('data/otg_'+str(num) + '.csv', 'w')

	# read html for parsing the name of OTG
	response = urllib2.urlopen(url)
	html = response.read()

	# add name and region (stored in title) to the attribute table
	soup = BeautifulSoup(html, 'html.parser')
	title = soup.title.string
	title_list = title.split(' - ')
	#print title_list[0], title_list[1]

	f.write('name|' + title_list[0] + '\nregion|' + title_list[1] + '\n')


	tables = pd.read_html(url) # Returns list of all tables on page
	passport_table = tables[0] # Takes certain table from page

	# write the .csv file with the '|' separator and 'utf-8' encoding
	f.write('id|' + str(100 + int(num)) + '\nlink|' + str(url))
	passport_table.to_csv(f, header=True, index=False, encoding='utf-8', sep='|')

	# add interval for looking like a human :)
	interval = randint(0,3)
	time.sleep(interval)

	#f.close()

id = 1
#loop for all the regions
for line in file:
	search_otg(line, id)
	id = id + 1