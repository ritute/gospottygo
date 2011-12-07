import __init__
import urllib2
from helpers.BeautifulSoup import *
from urlparse import urljoin
import sqlite3 
import cursorhelpers as db

#IGNOREWORDS = {'the':1,'of':1,'to':1,'and':1,'a':1,'in':1,'is':1,'it':1}
IGNOREWORDS = {}

class crawler(object): 
    def __init__(self):
        self.is_indexed = {} # remember if a page has been indexed
    
        #reset tables
        db.DataBase.drop_tables()
        db.DataBase.create_tables()


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

        # add page to document table
        document_id = db.Document.get_word_id_add(page)

        # get the document title
        title = soup('title')[0].string

        # get a description of the document (using either meta tag or paragraph)
        metas = soup('meta')
        paras = soup('p')
        if len(metas):
            # use meta description tag if it's there
            for meta in metas:
                if ('name' in dict(meta.attrs)):
                    descrip = meta['content']
        elif len(paras):
            # find first paragraph
            descrip = paras[0].findAll(text=True)[0]
        else:
            descrip = "" # blank description
        
        # add title and description to document table
        db.Document.add_title_and_description(document_id, title, descrip)
        
        text = self._get_text_only(soup)
        words = self._separate_words(text)

        for word in words:
            if word in IGNOREWORDS : continue

            word_id = db.Lexicon.get_word_id_add(word)

            db.DocWordIndex.increment_and_get_freq(document_id,word_id)

    #=== ADD A LINK ==============================================================
    def _add_link(self, page, url, linktext):
        id1 = db.Document.get_word_id_add(page)
        id2 = db.Document.get_word_id_add(url)

        freq = db.Link.increment_and_get_freq(id1, id2)

  
    #=== CRAWL THE WEB!! =========================================================
    def crawl(self, depth = 2):
        pages = [line.split("|")[0] for line in file('../db/urllist.txt')]
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
                        if url[0:4] == 'http' and url not in self.is_indexed:
                            newpages[url] = 1
                        linktext = self._get_text_only(link)
                        self._add_link(page, url, linktext)
                except:
                    print "Could not parse page %s" % page
            pages = newpages

if __name__=="__main__":
    print "STARTING CRAWLER..."
    
    crawler().crawl()

    print "CRAWLER FINISHED"
    
    print "BEGINNING PAGERANK ALGORITHM"
    
    #index
    import pagerank
    pagerank.connection = db.connection
    pagerank.populate_page_rank()
