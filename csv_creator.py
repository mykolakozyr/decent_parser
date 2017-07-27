# -*- coding: utf-8 -*-

import os
import time


def csv_creator(num):

	file = 'data/temp_' + str(num) + '.txt'

	if int(os.path.getsize(file)) > 0: # near 2000 for files with passport data
		file_parsed = open(file, 'r')
		lines = file_parsed.readlines()
		file_csv.write(str(100 + num))
		for line in lines:
			if line != lines[-1]: # all lines except the last one
				line = line.strip()
				line_list = line.split('|')
				if line_list[1] == '"':
					line_list[1] = 'sometext'
				if line_list[1] == '':
					continue
				file_csv.write('|' + str(line_list[1]))
			else: #last line in temp_num file
				line = line.strip()
				line_list = line.split('|')
				file_csv.write('|' + str(line_list[1]) + '\n')


file_csv = open('data_csv.csv','w')

#write attributes names
file_csv.write('id_int|name|region|id_txt|url|shit|shit_2|population|children|pupils|settl_num|revenue|rev_budg_ua|budget|dotation|dot_reverse|area|inst_num|school_1-3|school_1-2|school_1|kindergart|extracur|culture|physical|med_assist|dispensary|clinic|ambulance|build_gen|court|civil_prop|retirement|social_prot|fire_secur|treasury|local_govern\n')

animation = "|/-\\"
idx = 1

for i in range(1,395): # number of OTGs
	csv_creator(i)
	print 'packing files...', animation[idx % len(animation)] + "\r",
	idx += 1
	time.sleep(0.005) #just for being nice

print '\nDone!'