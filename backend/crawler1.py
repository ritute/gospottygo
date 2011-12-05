import urllib2
from BeautifulSoup import *
from urlparse import urljoin
from pysqlite2 import dbapi2 as sqlite

IGNOREWORDS = {'the':1,'of':1,'to':1,'and':1,'a':1,'in':1,'is':1,'it':1}

class crawler(object): 
    def __init__(self):
        self.is_indexed = {} # remember if a page has been indexed
        # Create and open database connection
        self.con = sqlite.connect("repo.db")  
        self.cur = self.con.cursor()
        # Create tables
        self.cur.execute('''create table lexicon (
                              id integer primary key asc autoincrement, 
                              word varchar(100) unique not null
                          )''')
        self.cur.execute('''create table document (
                              id integer primary key asc autoincrement, 
                              uri varchar(255) unique not null
                          )''')
        self.con.commit()


    #=== GET TEXT ONLY ===========================================================
    def _get_text_only(self, soup):
        v = soup.string
        if v == None:   
            c = soup.contents
            resulttext = ''
            for t in c:
                subtext = self._get_text_only(t)
                resulttext += subtext + '\n'
            return resulttext
        else:
            return v.strip()
  
  
    #=== SEPARATE WORDS ========================================================== 
    def _separate_words(self, text):
        splitter = re.compile('\\W*')
        return [s.lower() for s in splitter.split(text) if s != '']


    #=== INDEX THE PAGE ==========================================================
    def _index_page(self, page, soup):
        if page in self.is_indexed:
            return
        self.is_indexed[page] = True

        # Add page to document table
        self.cur.execute('insert into document (uri) values (?)', [(page)])

        text = self._get_text_only(soup)
        words = self._separate_words(text)

        for word in words:
            if word in IGNOREWORDS : continue
        # TODO: canonocalize ...
        # Add word to lexicon table
        #self.cur.execute('insert into lexicon (word) values (?)', [(word)])

        self.con.commit()


    #=== ADD A LINK ==============================================================
    def _add_link(self, page, url, linktext):
        # modify here to build graph
        print "%s =====================> %s\n" % (page, url)
  
  
    #=== CRAWL THE WEB!! =========================================================
    def crawl(self, depth = 2):
        pages = [line for line in file('urllist.txt')]
        for i in range(depth):
            newpages = {}
            for page in pages:
                try:
                    c = urllib2.urlopen(page)
                except:
                    print "Could not open %s" % page
                    continue
                try:
                    soup = BeautifulSoup(c.read())
                    self._index_page(page, soup)

                    links = soup('a')
                    for link in links:
                        if ('href' in dict(link.attrs)):
                            url = urljoin(page, link['href'])
                        if url.find("'") != -1: continue
                            url = url.split('#')[0]  # remove location portion
                        if url[0:4] == 'http' and url in self.is_indexed:
                            newpages[url] = 1
                        linktext = self._get_text_only(link)
                        self._add_link(page, url, linktext)
                except:
                    print "Could not parse page %s" % page
            pages = newpages
