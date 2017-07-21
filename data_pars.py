# -*- coding: utf-8 -*-

import os
import re

def data_pars(num):
	file = open('data/otg_' + str(num) + '.csv', 'r')

	file_output = open('data/temp_' + str(num) + '.txt','w')
	print 'Parsing OTG with the code number ', num

	for line in file:
		line = line.strip()
		list = line.split('|')
		try:
			if line[0].isdigit(): #main values
				#print list[1].rstrip(':'),list[2]
				file_output.write(list[1].rstrip(':') + '|' + list[2] + '\n')
			elif line[0].startswith('N'): #some other values
				#print list[1].rstrip(':'), list[2]
				file_output.write(list[1].rstrip(':') + '|' + list[2] + '\n')
			elif line[0].startswith('|'): #some other values
				#print list[1].rstrip(':'), list[2]
				file_output.write(list[1].rstrip(':') + '|' + list[2] + '\n')
			else: #additional values
				#print list[0].rstrip(':'), list[1]
				file_output.write(list[0].rstrip(':') + '|' + list[1] + '\n')
		except IndexError:
			print 'Data cannot be parsed'

for i in range(1,395):
	data_pars(i)