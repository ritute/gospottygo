'''

Step #1: URL Sequencer

Grabs all the links from a specified URL file, fixes them up, and generates a
URL sequence to be passed to the Crawler.

'''

import urllib2
import urlparse

class URLSequencer(object):

    def __init__(self, urlFile):
        '''Generate sequence of URL's from the specified file *urlFile*.'''
        self._URLSequence = []
        try:
            with open(urlFile, 'r') as f:
                for line in f:
                    self._URLSequence.append((self._fixURL(line.strip(), "")))
        except IOError:
            print "Error reading file!\n"
  
    #TODO: figure out if rel is really needed here!!!  
    def _fixURL(self, currentURL, rel):
      '''Given the current URL *currentURL* and either something relative to that
      URL or another URL *rel*, return a properly parsed URL.'''
      lRel = rel.lower()
      if lRel.startswith('http://') or lRel.startswith('https://'):
          currentURL, rel = rel, ''
      
      # Compute the new URL based on import
      currentURL = urlparse.urldefrag(currentURL)[0]
      parsedURL = urlparse.urlparse(currentURL)
    
      return urlparse.urljoin(parsedURL.geturl(), rel)

    def get_urls(self):
        return self._URLSequence
