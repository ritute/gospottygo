import urllib2
from BeautifulSoup import *
from urlparse import urljoin
from pysqlite2 import dbapi2 as sqlite

IGNOREWORDS={'the':1,'of':1,'to':1,'and':1,'a':1,'in':1,'is':1,'it':1}

class crawler( object ) : 
  def __init__( self ) :
    self.is_indexed = {} # remember if a page has been indexed

  def gettextonly(self,soup):
    v=soup.string
    if v==None:   
      c=soup.contents
      resulttext=''
      for t in c:
        subtext=self.gettextonly(t)
        resulttext+=subtext+'\n'
      return resulttext
    else:
      return v.strip()
   
  def separatewords(self,text):
    splitter=re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if s!='']

  def index_page(self,page,soup):
    if page in self.is_indexed:
      return
    self.is_indexed[page] = True

    text=self.gettextonly(soup)
    words=self.separatewords(text)
    # modify here to index page
    for word in words:
      if word in IGNOREWORDS : continue
      print word
    print '\n'

  def add_link(self,page,url,linktext) :
    # modify here to build graph
    print "%s =====================> %s\n" % (page,url)
    
  def crawl(self,depth=2):
    pages=[line for line in file('urllist.txt')]
   for i in range(depth):
      newpages={}
      for page in pages:
        try:
          c=urllib2.urlopen(page)
        except:
          print "Could not open %s" % page
          continue
        try:
	  soup=BeautifulSoup(c.read())
	  self.index_page(page,soup)

	  links=soup('a')
	  for link in links:
	    if ('href' in dict(link.attrs)):
	      url=urljoin(page,link['href'])
	      if url.find("'")!=-1: continue
	      url=url.split('#')[0]  # remove location portion
	      if url[0:4]=='http' and url in self.is_indexed:
	        newpages[url]=1
	      linktext=self.gettextonly(link)
	      self.add_link(page,url,linktext)

        except:
          print "Could not parse page %s" % page
      pages=newpages
