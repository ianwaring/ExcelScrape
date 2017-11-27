from bs4 import BeautifulSoup
import urllib2

site= "http://www.ceoemail.com/index.php"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site,headers=hdr)


response=urllib2.urlopen(req)
htmlpage = response.read()
htmltree = BeautifulSoup(htmlpage)
print (htmltree.prettify)
