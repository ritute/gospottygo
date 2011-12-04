from bottle import *

# @route('/')
# def index():
#   send_file('index.html', root="resources/public/")
@route('/static/:path#.+#', name='static')
def static(path):
  return static_file(path, root='static')

@route('/')
@view('index')
def index():
  return {'get_url': get_url}

# @route('/<filename>')
# def serve_html(filename):
#   send_file(filename, root="resources/public/")



run(host='localhost', port=8080)