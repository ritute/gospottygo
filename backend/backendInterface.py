'''

Index Server

'''

import Crawler
import URLSequencer

def searchQuery():
  u = URLSequencer.URLSequencer('urllist.txt')
  c = Crawler.Crawler(u._URLSequence)