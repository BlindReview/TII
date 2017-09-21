import urllib2
import sys, os, string
import re
from BeautifulSoup import BeautifulSoup

def global_variance():
	global dic
	dic = os.getcwd()

def usage():
	print u'''
	help: dblp.py <authors file name>
	[authos file name]: Option, a file with all the authors 

	Example: python dblp.py authors.dat
	'''

def getUrl():
	authorFile = sys.argv[1]
	authorUrlArr = []
	auts = []
	readFile = open(dic + '\\' + authorFile)
	line = readFile.readlines()
	#print line
	for eachAuthor in line:
		firstName = ""
		secondName = ""
		newEachWord = ''
		part2 = ""
		count = 0
		authorUrl = ""
		splitedAuthor = eachAuthor.split(" ") # first name and second name
		#print splitedAuthor[0:len(splitedAuthor)-1]
		part1 = splitedAuthor[len(splitedAuthor)-1][0].lower()
		for eachWord in splitedAuthor[len(splitedAuthor)-1].strip('\n'): # first name
			for letter in eachWord:
				if re.match('[a-zA-Z]', letter):
					firstName = firstName + letter
				else:
					firstName = firstName + "="
		firstName = firstName + ":"
		part2 = part2 + firstName

		for eachWord in splitedAuthor[0:len(splitedAuthor)-1]: # second name
			count = count + 1
			if count == 1:
				newEachWord = eachWord.strip()
			else:
				newEachWord = newEachWord + " " + eachWord.strip()

		for letter in newEachWord:
			if re.match('[a-zA-Z]', letter):
				secondName = secondName + letter
			elif re.match(' ', letter):
				secondName = secondName + "_"
			else:
				secondName = secondName + "="
		part2 = part2 + secondName
		authorUrl = part1 + "/" + part2
		#print authorUrl
		authorUrlArr.append(authorUrl)
		auts.append(eachAuthor)
	readFile.close()
	return [authorUrlArr, auts]

def getData(urlSuffix, currentAuthor):
	all_coAuthors_list = []
	all_html_list = []
	coAuthorAndHtml = dict()
	print currentAuthor
	authorName = ''
	secondNameLoc = urlSuffix.index(":")
	for l in urlSuffix[secondNameLoc:]:
		if l.isalpha():
			authorName = authorName + l
	fileName = authorName + ".dat"
	print fileName
	writeFile = open(fileName, 'w')

	urlPrefix = "http://dblp.uni-trier.de/pers/hd/"
	url = urlPrefix + urlSuffix
	contents = urllib2.urlopen(url).read()
	soup = BeautifulSoup(contents)
	publ_list = soup.findAll('ul', attrs = {'class':'publ-list'})
	strip_tag_pat = re.compile('</?\w+[^>]*>') 

	for pl in publ_list:
		s = str(BeautifulSoup(str(pl)).prettify())
		temp = 1
		last_index = 0
		for m in re.finditer('<li class="year">', s):
			year = BeautifulSoup(s[temp:m.start()]).findAll('li', attrs = {'class':'year'})
			coAuthor = BeautifulSoup(s[temp:m.start()]).findAll('span', attrs = {'itemprop':'author'})
			authorList = []
			htmlList = []
			authorAndNum1 = []
			for y in year:
				y0 = re.sub(strip_tag_pat,' ',str(y))
				print y0
				writeFile.writelines(y0 + '\n')
			for ca in coAuthor:
				name = ca.findAll('span', attrs = {'itemprop':'name'})
				coAuthorUrl = ca.findAll('a', attrs = {'itemprop':'url'})
				for authorUrls in coAuthorUrl:
					i0 = re.sub(strip_tag_pat,' ',str(authorUrls))
					i1 = str(authorUrls).split(' ')
					html = i1[1][6:-1] 
					if "dblp.uni-trier.de/pers/hd" in html:
						print html
						all_html_list.append(html)
						number = calcPaperNo(html)
						htmlList.append(number)
				for c in name:
					c0 = re.sub(strip_tag_pat,' ',str(c))
					if currentAuthor not in (str(c0).strip('\n')).strip():
						print c0
						all_coAuthors_list.append(c0)
						authorList.append(c0)
				temp = m.start()
			for index1 in range(0, len(htmlList)):
				authorAndNum1.append(authorList[index1].rstrip('\n')+"    "+str(htmlList[index1]).strip())
			last_index = m.start() 
			new_authorAndNum1 = list(set(authorAndNum1))
			for authors in range(0, len(new_authorAndNum1)):
				writeFile.writelines(str(new_authorAndNum1[authors]).strip()+'\n')

		year = BeautifulSoup(s[last_index-10:last_index+10]).findAll('li', attrs = {'class':'year'})
		#coAuthor = BeautifulSoup(str(pl)[last_index:len(str(pl))]).findAll('span', attrs = {'itemprop':'author'})
		coAuthor2 = coAuthor = BeautifulSoup(s[last_index:len(s)]).findAll('span', attrs = {'itemprop':'author'})
		coAuthorUrl = BeautifulSoup(s[last_index-10:last_index+10]).findAll('a', attrs = {'itemprop':'url'})
		print re.sub(strip_tag_pat, ' ', str(s[last_index-10:last_index+30]))
		writeFile.writelines(re.sub(strip_tag_pat, ' ', str(s[last_index-5:last_index+30])) + '\n')
		for y in year:
			y0 = re.sub(strip_tag_pat,' ',str(y))
			print y0
			
		authorList2 = []
		htmlList2 = []
		authorAndNum = []
		for ca in coAuthor2:
			name = ca.findAll('span', attrs = {'itemprop':'name'})
			coAuthorUrl = ca.findAll('a', attrs = {'itemprop':'url'})
			for authorUrls in coAuthorUrl:
				i0 = re.sub(strip_tag_pat,' ',str(authorUrls))
				i1 = str(authorUrls).split(' ')
				html = i1[1][6:-1] 
				if "dblp.uni-trier.de/pers/hd" in html:
					print html
					number = calcPaperNo(html)
					print number
					all_html_list.append(html)
					htmlList2.append(number)
			for c in name:
				c0 = re.sub(strip_tag_pat,' ',str(c))
				if currentAuthor not in (str(c0).strip('\n')).strip():
					print c0
					all_coAuthors_list.append(c0)
					authorList2.append(c0)
		for index in range(0, len(htmlList2)):
			authorAndNum.append(authorList2[index].lstrip('\n')+"    "+str(htmlList2[index]).strip())
		#new_authorList2 = list(set(authorList2))
		#new_htmlList2 = list(set(htmlList2))
		new_authorAndNum = list(set(authorAndNum))
		for authors2 in range(0, len(new_authorAndNum)):
				writeFile.writelines(str(new_authorAndNum[authors2])+'\n')
		print "===================="
	for ind in range(0, len(all_html_list)):
		coAuthorAndHtml[all_coAuthors_list[ind]] = all_html_list[ind]
	print coAuthorAndHtml
	writeFile.close()
	return coAuthorAndHtml

def coAuthorList(coauthors):
	for author in coauthors.keys():
		print 'author=%s, html=%s' % (author, coauthors[author])
		paperNo_eachYear(author, coauthors[author])

def paperNo_eachYear(author, url):
	#contents = urllib2.urlopen(url).read()
	wf = open("coauthors.dat", "a")
	contents = urllib2.urlopen(url).read()
	soup = BeautifulSoup(contents)
	publ_list = soup.findAll('ul', attrs = {'class':'publ-list'})
	strip_tag_pat = re.compile('</?\w+[^>]*>') 
	wf.writelines(author)

	for pl in publ_list:
		s = str(BeautifulSoup(str(pl)).prettify())
		temp = 1
		last_index = 0
		for m in re.finditer('<li class="year">', s):
			year = BeautifulSoup(s[temp:m.start()]).findAll('li', attrs = {'class':'year'})
			paperTile = BeautifulSoup(s[temp:m.start()]).findAll('span', attrs = {'class':'title'})
			count = 0
			count2 = 0

			for y in year:
				y0 = re.sub(strip_tag_pat,' ',str(y))
				print y0
				wf.writelines(y0)
			for paper in paperTile:
				paperName = re.sub(strip_tag_pat,' ',str(paper))
				print paperName
				count = count + 1
				print count
				temp = m.start()
			wf.writelines(str(count)+'\n')

			last_index = m.end() 

		year = BeautifulSoup(s[last_index-15:last_index+27]).findAll('li', attrs = {'class':'year'})
		print s[last_index-10:last_index+20] + "--------"
		wf.writelines(str(s[last_index-10:last_index+20])+'\n')
		paperTile2 = BeautifulSoup(s[last_index:len(s)]).findAll('span', attrs = {'class':'title'})

		for y in year:
			y0 = re.sub(strip_tag_pat,' ',str(y))
			print y0
			#wf.writelines(y0)
		for paper in paperTile2:
			paperName = re.sub(strip_tag_pat,' ',str(paper))
			print paperName
			count2 = count2 + 1
			print count2
		wf.writelines(str(count2) + '\n')
	wf.writelines("********************************")
	wf.close()


def calcPaperNo(authorURL):
	contents = urllib2.urlopen(authorURL).read()
	soup = BeautifulSoup(contents)
	strip_tag_pat = re.compile('</?\w+[^>]*>') 
	count = 0
	paperTile = soup.findAll('span', attrs = {'class':'title'})
	for paper in paperTile:
		paperName = re.sub(strip_tag_pat,' ',str(paper))
		count = count + 1
	print count
	return count

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
		sys.exit(1)
	global_variance()
	[urls, aut] = getUrl()
	for urlSuffix in range (0, len(urls)):
		dic_authors = getData(urls[urlSuffix], aut[urlSuffix])
		coAuthorList(dic_authors)
