import urllib
import re

USERNAME = ""
PASSWORD = ""

def check( domain ):

	try:
		sock = urllib.urlopen(domain)
		htmlSource = sock.read()
		htmlSourcel = htmlSource.lower()
		sock.close()
		regex = re.compile('<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)
		title = regex.search(htmlSource).group(1)
		if "expired" in htmlSourcel:
			title = title + " EXPIRED"
		if "domain for sale" in htmlSourcel:
        	        title = title + " FOR SALE1"
		if "this domain" in htmlSourcel:
        	        title = title + " FOR SALE2"

	except:
		title = "Can't open"
	return unicode(title, "utf-8")


import delicious
d = delicious.open(USERNAME,PASSWORD)
posts = d["posts"]
f = open('output', 'w')
c = 0
for post in posts:
	try:
		c += 1
		i = check( post['href'] )
		f.write(post['href'] + ";" + i + '\n')
		f.flush()
	except:
		pass

f.close
print "Done"
