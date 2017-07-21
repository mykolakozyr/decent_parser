# -*- coding: utf-8 -*-

import os


def csv_creator(num):

	file = 'data/temp_' + str(num) + '.txt'

	if int(os.path.getsize(file)) > 2000: # files with passport data
		file_parsed = open(file, 'r')
		lines = file_parsed.readlines()
		file_csv.write(str(100 + num))
		for line in lines:
			if line != lines[-1]: # all linex except the last one
				line = line.strip()
				line_list = line.split('|')
				file_csv.write('|' + str(line_list[1]))
			else: #last line
				line = line.strip()
				line_list = line.split('|')
				file_csv.write('|' + str(line_list[1]) + '\n')


file_csv = open('data_csv.csv','w')

id = 1
for i in range(1,395): # number of OTGs
	csv_creator(i)