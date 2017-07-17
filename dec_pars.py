import urllib2
from bs4 import BeautifulSoup
import re

file_output = open('url.txt', 'w')

def search_otg(id):
	print 'Preparing the GET request.....\nID number ' + str(id)

	#set the url for parsing links to otg in every region
	url = "http://decentralization.gov.ua/region/item/id/" + str(id)
	response = urllib2.urlopen(url)

	html = response.read()

	print 'Received Response..... Preparing to parse'

	#print html

	soup = BeautifulSoup(html, 'html.parser')

	print 'Created a Soup. Getting ready for findAll'

	for a in soup.findAll('a', href=True):
		if re.search('region/common', str(a['href'])):
			link = a['href']
			if link in d:
				print 'Found the existing value'
				continue
			else:
				print 'Found the unique value'
				d.append(link)
				file_output.write('http://decentralization.gov.ua'+link+'\n')
	print 'Finished with region number ' + str(id)

id = 1
d = list()

#loop for all he regions
while True:
	if id == 26:
		break
	search_otg(id)
	id = id + 1