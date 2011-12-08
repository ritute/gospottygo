import __init__
from bottle import static_file, route, get, view, run, request
from backend.backendInterface import *
from time import time

# Server static files on server
@route('/static/:path#.+#', name='static')
def static(path):
  return static_file(path, root='static')

# Index view
@get('/')
@view('index')
def index():
  return {}

# Results view
@get('/results')
@view('results')
def results():
  keyword = request.GET.get('keyword') # get keyword searched for from GET param
  start_time = time()
  results = search_query(keyword) # obtain search results
  print "results", results
  end_time = time()
  elapsed_time = "%.4f" % (end_time - start_time) # elapsed time to obtain results in seconds
  return dict(keyword=keyword, results=results, time=elapsed_time)

run(host='localhost', port=8080)