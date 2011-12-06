from bottle import static_file, route, get, view, run, request

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
  keyword = request.GET.get('keyword')
  return dict(keyword=keyword, val=6)

run(host='localhost', port=8080)