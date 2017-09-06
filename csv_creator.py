# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import time


def name(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')
		value = a[0]
		if 'name' in value:
			return str(a[1])
def region(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'region' in value:
			return str(a[1])
def id(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'id' in value:
			return str(a[1])
def link(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'link' in value:
			return str(a[1])				
def population(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'Чисельність' in value:
			return str(a[1])
def settl_num(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'населених пунктів' in value:
			return str(a[1])
def children(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'дошкільного' in value:
			return str(a[1])
def pupils(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if value.startswith('шкільного'):
			return str(a[1])
def revenue(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'Обсяг доходів' in value:
			return str(a[1])
def rev_budg_ua(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'Бюджетного кодексу' in value:
			return str(a[1])	
def budget(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'бюджету розвитку' in value:
			return str(a[1])	
def dotation(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'базової дотації' in value:
			return str(a[1])	
def dot_reverse(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'реверсної дотації' in value:
			return str(a[1])	
def area(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'Площа території' in value:
			return str(a[1])		
def inst_num(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'Кількість закладів' in value:
			return str(a[1])
def school_13(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'I—III' in value:
			return str(a[1])	
def school_12(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'I—II ' in value:
			return str(a[1])	
def school_1(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if ' I ступен' in value:
			return str(a[1])	
def kindergart(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'дошкільних' in value:
			return str(a[1])	
def extracur(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'позашкільної' in value:
			return str(a[1])	
def culture(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'закладів культури' in value:
			return str(a[1])	
def physical(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'фізичної культури' in value:
			return str(a[1])	
def med_assist(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'акушерських ' in value:
			return str(a[1])	
def dispensary(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'амбулаторій' in value:
			return str(a[1])	
def clinic(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'лікарень' in value:
			return str(a[1])	
def ambulance(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'швидкої допомоги' in value:
			return str(a[1])	
def build_gen(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'розміщення державних органів' in value:
			return str(a[1])
def court(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'правоохоронної' in value:
			return str(a[1])	
def civil_prop(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'актів цивільного' in value:
			return str(a[1])	
def retirement(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'пенсійного ' in value:
			return str(a[1])	
def social_prot(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'соціального' in value:
			return str(a[1])	
def fire_secur(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'пожежної' in value:
			return str(a[1])	
def treasury(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')	
		value = a[0]
		if 'казначейського' in value:
			return str(a[1])	
def local_govern(file):
	file_parsed = open(file, 'r')
	lines = file_parsed.readlines()
	for line in lines:
		line = line.strip()
		a = line.split('|')
		value = a[0]
		if 'розміщення органів місцевого' in value:
			return str(a[1])	

def csv_creator(num):

	file = 'data/temp_' + str(num) + '.txt'

	if int(os.path.getsize(file)) > 0: # near 2000 for files with passport data
		
		# create variables for data collecting
		name_str =  name(file)
		region_str = region(file)
		link_str = link(file)
		population_str = population(file)
		children_str = children(file)
		pupils_str = pupils(file)
		settl_num_str = settl_num(file)
		revenue_str = revenue(file)
		rev_budg_ua_str = rev_budg_ua(file)
		budget_str = budget(file)
		dotation_str = dotation(file)
		dot_reverse_str = dot_reverse(file)
		area_str = area(file)
		inst_num_str = inst_num(file)
		school_13_str = school_13(file)
		school_12_str = school_12(file)
		school_1_str = school_1(file)
		kindergart_str = kindergart(file)
		extracur_str = extracur(file)
		culture_str = culture(file)
		physical_str = physical(file)
		med_assist_str = med_assist(file)
		dispensary_str = dispensary(file)
		clinic_str = clinic(file)
		ambulance_str = ambulance(file)
		build_gen_str = build_gen(file)
		court_str = court(file)
		civil_prop_str = civil_prop(file)
		retirement_str = retirement(file)
		social_prot_str = social_prot(file)
		fire_secur_str = fire_secur(file)
		treasury_str = treasury(file)
		local_govern_str = local_govern(file)
		

		lst = ['name','region','link','population','children','pupils','settl_num','revenue','rev_budg_ua','budget','dotation','dot_reverse','area','inst_num','school_13','school_12','school_1','kindergart','extracur','culture','physical','med_assist','dispensary','clinic','ambulance','build_gen','court','civil_prop','retirement','social_prot','fire_secur','treasury','local_govern']

		for i in lst:
			# print locals()[i+'_str']
			if locals()[i+'_str'] is not None: # creates variable from string
				file_csv.write(locals()[i+'_str'] + '|')
			else:
			 	file_csv.write('|')				
		file_csv.write('\n')


file_csv = open('data_csv.csv','w')

#write attributes names
file_csv.write('name|region|link|population|children|pupils|settl_num|revenue|rev_budg_ua|budget|dotation|dot_reverse|area|inst_num|school_13|school_12|school_1|kindergart|extracur|culture|physical|med_assist|dispensary|clinic|ambulance|build_gen|court|civil_prop|retirement|social_prot|fire_secur|treasury|local_govern\n')

animation = "|/-\\"
idx = 1

for i in range(1,395): # number of OTGs
	csv_creator(i) 
	print 'packing files...', animation[idx % len(animation)] + "\r",
	idx += 1
	time.sleep(0.005) #just for being nice

print '\nDone!'