import urllib2
import sys, os, string
import re
from BeautifulSoup import BeautifulSoup

def global_variance():
	global dic
	dic = os.getcwd()

def coauthors(url, currentAuthor):
	
	contents = urllib2.urlopen(url).read()
	soup = BeautifulSoup(contents)
	publ_list = soup.findAll('ul', attrs = {'class':'publ-list'})
	strip_tag_pat = re.compile('</?\w+[^>]*>')
	authorList = []
	writeFile = open(dic + "\coauthors.dat", 'a')

	for pl in publ_list:
		s = str(BeautifulSoup(str(pl)).prettify())
		temp = 1
		last_index = 0
		year_count = 0
		if year_count < 15:
			y = 0
			for m in re.finditer('<li class="year">', s):
				all_coAuthors_list = []
				all_html_list = []
				coAuthorAndHtml = dict()
				year = BeautifulSoup(s[temp:m.start()]).findAll('li', attrs = {'class':'year'})
				coAuthor = BeautifulSoup(s[temp:m.start()]).findAll('span', attrs = {'itemprop':'author'})
				
				for y in year:
					y0 = re.sub(strip_tag_pat,' ',str(y))
					#print y0
					y = y0.strip(' \t\n\r')
					#writeFile.writelines(y0 + '\n')
				print url + "_" + str(y) 
				for ca in coAuthor:
					name = ca.findAll('span', attrs = {'itemprop':'name'})
					coAuthorUrl = ca.findAll('a', attrs = {'itemprop':'url'})
					for c in name:
						c0 = re.sub(strip_tag_pat,' ',str(c))
						if currentAuthor not in (str(c0).strip('\n')).strip():
							#print c0
							authorList.append(c0.strip(' \t\n\r'))

			year_count = year_count + 1
	#writeFile.close()
	coauthors = set(authorList)
	writeFile.writelines(currentAuthor+',')
	for c in coauthors:
		writeFile.writelines(c+'	')
	writeFile.writelines('\n')

def coauthor_coauthor(currentAuthor,url,specific_year):
	
	contents = urllib2.urlopen(url).read()
	soup = BeautifulSoup(contents)
	publ_list = soup.findAll('ul', attrs = {'class':'publ-list'})
	strip_tag_pat = re.compile('</?\w+[^>]*>')
	all_coAuthors_list = []

	for pl in publ_list:
		s = str(BeautifulSoup(str(pl)).prettify())
		temp = 1
		last_index = 0
		year_count = 0
		y = 0
		for m in re.finditer('<li class="year">', s):
			
			year = BeautifulSoup(s[temp:m.start()]).findAll('li', attrs = {'class':'year'})
			#print year
			#print "--##-"
			for y in year:
				y0 = re.sub(strip_tag_pat,' ',str(y))
				#print y0
				y = y0.strip(' \t\n\r')
			if str(y) in specific_year:
				print y
				coAuthor = BeautifulSoup(s[temp:m.start()]).findAll('span', attrs = {'itemprop':'author'})
				for ca in coAuthor:
					name = ca.findAll('span', attrs = {'itemprop':'name'})
					for c in name:
						c0 = re.sub(strip_tag_pat,' ',str(c))
						if currentAuthor not in (str(c0).strip('\n')).strip():
							#print c0
							all_coAuthors_list.append(c0.strip(' \t\n\r'))
						
					temp = m.start()
	#print all_coAuthors_list
	return all_coAuthors_list

if __name__ == "__main__":
	global_variance()
	authors_file = open(dic + '\\all_authors_without_repeat_Copy.dat')
	authors = authors_file.readlines()
	for author in authors:
		coauthors(author.strip().split('	')[1],author.strip().split('	')[0])