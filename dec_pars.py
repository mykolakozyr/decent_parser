import urllib2
from bs4 import BeautifulSoup
import re

file_output = open('url_real.txt', 'w')

def search_otg(id):
	print 'Preparing the GET request.....ID number ' + str(id)

	#set the url for parsing links to otg in every region
	url = "http://decentralization.gov.ua/region/item/id/" + str(id) + '#tab1'
	response = urllib2.urlopen(url)
	html = response.read()

	print 'Received Response..... Preparing to parse'

	soup = BeautifulSoup(html, 'html.parser')

	print 'Created a Soup. Getting ready for findAll'

	divclass = soup.findAll(id = "tab1")

	for tag in divclass:
		aTags = tag.findAll('a', href=True)
		for tag in aTags:
		 if re.search('region/common', str(tag['href'])):
		 	link = tag['href']
		 	print link
		# 	if link in d: #check if it is not a duplicate
		# 		continue
		# 	else:
		# 		d.append(link)
		 	file_output.write('http://decentralization.gov.ua'+link+'\n')
	print 'Finished with region number ' + str(id)

id = 1
d = list() #list for avoiding duplicate links

#loop for all the regions
while True:
	if id == 25:
		break
	search_otg(id)
	id = id + 1